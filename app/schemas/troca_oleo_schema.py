from pydantic import BaseModel


class TrocaOleoCreate(BaseModel):
    placa: str
    data: str
    km: float
    tipo_oleo: str
    proxima_troca_km: float
    valor: float


class TrocaOleoResponse(BaseModel):
    id: int
    veiculo_id: int
    data: str
    km: float
    tipo_oleo: str
    proxima_troca_km: float
    valor: float
    
    
    
    
    