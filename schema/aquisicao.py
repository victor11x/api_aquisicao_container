from pydantic import BaseModel
from typing import Optional, List
from datetime import date
from model.novos_produtos import Aquisicoes


class AquisicaoSchema(BaseModel):
    """ Define como um novo registro de auditoria de inventarios produtos faltantes no estoque
    """
    
    nome_produto : str = "Camisa Polo G"
    categoria : str = "Camisa"
    pratileira : str =  "120"
    posicao : str =  "12"
    quantidade : int = "5"       
    valor_total = int = "200"
    imagem_produto = "xxxx.jpg"

class AquisicaoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com nome do produto.
    """
    nome_produto: str = "Digite nome produto"


class ListagemAquisicaoSchema(BaseModel):
    """ Define como uma listagem de produtos que teve auditoria.
    """
    aquisicoes:List[AquisicaoSchema]


def apresenta_aquisicoes(aquisicoes: List[Aquisicoes]):
    """ Retorna uma representação de produtos auditados seguindo o schema definido em
        InventarioViewSchema.
    """
    result = []
    for aquisicao in aquisicoes:
        result.append({
            "nome_produto":aquisicao.nome_produto,
            "categoria":aquisicao.categoria,
            "pratileira":aquisicao.pratileira,
            "posicao":aquisicao.posicao,
            "quantidade": aquisicao.quantidade,
            "data_aquisicao":aquisicao.data_insercao,
            "valor_total" : aquisicao.valor_total,
            "imagem_produto":aquisicao.imagem_produto
        })

    return {"aquisicoes": result}


class AquisicaoViewSchema(BaseModel):
    """ Define como um auditoria será retornado: descrição de produtos auditados).
    """
        
    id_aquisicao: int = 1    
    nome_produto : str = "Camisa Polo G"
    categoria : str = "Camisa"
    pratileira : str =  "120"
    posicao : str =  "12"
    quantidade : int = "5"
    data_insercao : str = "12/03/2023"
    valor_total : str = "220"
    imagem_produto : str = "xxxx.jpg"


class AquisicaoDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome_produto: str

def apresenta_aquisicao(aquisicao: Aquisicoes):
    """ Retorna uma representação da auditoria seguindo o schema definido em
        AquisicaoViewSchema.
    """
    return {   
        
            "nome_produto":aquisicao.nome_produto,
            "categoria":aquisicao.categoria,
            "pratileira":aquisicao.pratileira,
            "posicao":aquisicao.posicao,
            "quantidade": aquisicao.quantidade,
            "data_aquisicao":aquisicao.data_insercao,
            "valor_total" : aquisicao.valor_total,
            "imagem_produto":aquisicao.imagem_produto     
    }