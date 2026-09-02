from fastapi import APIRouter

from app.schemas.motorista_schema import MotoristaCreate
from app.services.motorista_service import (
    cadastro_motorista, listar_motoristas, buscar_motorista, ativar_motorista, inativar_motorista
)


router = APIRouter(
    prefix="/motoristas",
    tags=["Motoristas"]
)


@router.get("/")
def listar():
    return listar_motoristas()


@router.post("/")
def cadastrar(motorista: MotoristaCreate):
    return cadastro_motorista(
        motorista.nome,
        motorista.cpf,
        motorista.cnh,
        motorista.categoria_cnh
    )
    
    
@router.get("/{cpf}")
def buscar(cpf: str):
    return buscar_motorista(cpf)


@router.patch("/{cpf}/inativar")
def inativar(cpf: str):
    return inativar_motorista(cpf)


@router.patch("/{cpf}/ativar")
def ativar(cpf: str):
    return ativar_motorista(cpf)   
    
    
    
    
    
    
    
    
    
    
    
    
    