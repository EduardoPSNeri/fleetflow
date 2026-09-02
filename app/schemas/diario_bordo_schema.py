from typing import Optional
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
    
    
class DiarioBordoResponse(BaseModel):
    id: int
    veiculo_id: int
    motorista_id: int
    data: str
    hora_saida: str
    km_saida: float
    hora_chegada: Optional[str]
    km_chegada: Optional[float]
    
    