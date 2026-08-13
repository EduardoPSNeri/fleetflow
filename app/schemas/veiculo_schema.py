"""
Schema é responsavel por definir a estrutura dos dados que serão recebidos e enviados pela API.
Define os campos obrigatórios, tipos de dados e validações.

"""

from pydantic import BaseModel

class VeiculoCreate(BaseModel):
    numero_frota: int
    placa:  str
    marca: str
    modelo: str
    ano_fabricacao: int
    ano_modelo: int

class VeiculoUpdate(BaseModel):
    numero_frota: int
   
class VeiculoResponse(BaseModel):
    numero_frota: int

class VeiculoList(BaseModel):
    numero_frota: int

