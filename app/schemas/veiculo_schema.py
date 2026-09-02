from pydantic import BaseModel


class VeiculoCreate(BaseModel):
    placa: str
    marca: str
    modelo: str
    km: float
    combustiveis: list[str]