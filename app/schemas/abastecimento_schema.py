from pydantic import BaseModel


class AbastecimentoCreate(BaseModel):
    placa: str
    data: str
    km: float
    combustivel: str
    valor_litro: float
    quantidade_litro: float
    
    
    
    
    