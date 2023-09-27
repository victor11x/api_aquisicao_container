from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError
from datetime import datetime
from schema.error import *
from schema.aquisicao import *
from model import Session, novos_produtos
from flask_cors import CORS

info = Info(title="API Aquisicao de Novos Produtos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
aquisicao_tag = Tag(name="Aquisicao", description="Adição, visualização e remoção de produtos novos")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
  
@app.post('/aquisicoes', tags=[aquisicao_tag],
          responses={"200": AquisicaoViewSchema, "409": ErrorSchema, "400": ErrorSchema})


def add_aquisicao(form: AquisicaoSchema):
    """Aquisição de produtos novos no estoque à base de dados

    Retorna detalhes do Inventario.
    """
    aquisicao = Aquisicoes(

            nome_produto = form.nome_produto,
            categoria = form.categoria,
            pratileira = form.pratileira,
            posicao = form.posicao,
            quantidade = form.quantidade,
            valor_total = form.valor_total,
            imagem_produto = form.imagem_produto
        )
    try:

        session = Session()

        session.add(aquisicao)

        session.commit()
        return apresenta_aquisicao(aquisicao), 200

    except IntegrityError as e:

        error_msg = "Produto foi adicionado de mesmo nome já foi salvo na base :/"
        return {"mesage": error_msg}, 409

    except Exception as e:

        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400


# Metodo GET
@app.get('/aquisicoes', tags=[aquisicao_tag],
         responses={"200": ListagemAquisicaoSchema, "404": ErrorSchema})


def get_aquisicao():
    """Faz a busca todos produto novos.

    Retorna uma representação de produtos novos.
    """

    session = Session()

    aquisicoes = session.query(Aquisicoes).all()

    if not aquisicoes:
        return {"aquisicoes": []}, 200
    else:
        print(aquisicoes)
        return apresenta_aquisicoes(aquisicoes), 200
