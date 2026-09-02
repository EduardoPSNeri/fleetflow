from pydantic import BaseModel


class ManutencaoCreate(BaseModel):
    placa: str
    tipo: str
    descricao: str
    data: str
    km: float
    valor: float
    
    
    