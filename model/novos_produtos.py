from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime,date
from typing import Union

from model import Base

class Aquisicoes(Base):
    __tablename__ = 'novos_produtos'

    id_produto = Column("pk_produto", Integer, primary_key=True)
    nome_produto = Column(String(140))
    categoria = Column(String(140)) 
    preco_unitario = Column(String(140)) 
    pratileira = Column(String(4))
    posicao = Column(String(20))
    quantidade = Column(Integer)
    valor_total = Column(Integer)
    imagem_produto = Column(String(150))
    data_insercao = Column(DateTime, default=datetime.now())
    
    
def __init__(self, nome_produto:str, categoria:str, preco_unitario:int, pratileira: str, posicao: str,quantidade:int,valor_total:int,imagem_produto:str, data_insercao:Union[DateTime, None] = None):
        """
        Produtos faltantes no estoque 

        Arguments:
  
        """
        self.nome_produto = nome_produto
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.pratileira = pratileira
        self.posicao = posicao
        self.quantidade = quantidade
        self.valor_total = valor_total
        self.imagem_produto = imagem_produto
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
        