from pydantic import BaseModel


class ManutencaoCreate(BaseModel):
    placa: str
    tipo: str
    descricao: str
    data: str
    km: float
    valor: float


class ManutencaoResponse(BaseModel):
    id: int
    veiculo_id: int
    tipo: str
    descricao: str
    data: str
    km: float
    valor: float
    
    
    