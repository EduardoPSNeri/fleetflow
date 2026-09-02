from pydantic import BaseModel


class SaidaCreate(BaseModel):
    placa: str
    cpf: str
    data: str
    hora_saida: str
    km_saida: float


class ChegadaCreate(BaseModel):
    placa: str
    hora_chegada: str
    km_chegada: float
    
    
    