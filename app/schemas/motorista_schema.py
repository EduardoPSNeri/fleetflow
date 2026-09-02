from pydantic import BaseModel


class MotoristaCreate(BaseModel):
    nome: str
    cpf: str
    cnh: str
    categoria_cnh: str


class MotoristaResponse(BaseModel):
    id: int
    nome: str
    cpf: str
    cnh: str
    categoria_cnh: str
    ativo: bool
    
    
    