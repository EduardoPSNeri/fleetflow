from pydantic import BaseModel


class VeiculoCreate(BaseModel):
    placa: str
    marca: str
    modelo: str
    km: float
    combustiveis: list[str]
    
    
class VeiculoResponse(BaseModel):
    id: int
    numero_frota: int
    placa: str
    marca: str
    modelo: str
    km: float
    ativo: bool
    
    
    
    
    