from pydantic import BaseModel
from typing import Optional


class AbastecimentoCreate(BaseModel):
    placa: str
    data: str
    km: float
    combustivel: str
    valor_litro: float
    quantidade_litro: float


class AbastecimentoResponse(BaseModel):
    id: int
    veiculo_id: int
    data: str
    km: float
    combustivel: str
    valor_litro: float
    quantidade_litro: float
    valor_total: float
    media_consumo: Optional[float]
    custo_por_km: Optional[float]
    
    
    