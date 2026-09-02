from fastapi import APIRouter, HTTPException

from app.schemas.motorista_schema import (MotoristaCreate, MotoristaResponse)
from app.services.motorista_service import (
    cadastro_motorista, listar_motoristas, buscar_motorista, ativar_motorista, inativar_motorista,
)


router = APIRouter(
    prefix="/motoristas",
    tags=["Motoristas"]
)


@router.post("/", status_code=201)
def cadastrar(motorista: MotoristaCreate):
    resultado = cadastro_motorista(
        motorista.nome,
        motorista.cpf,
        motorista.cnh,
        motorista.categoria_cnh
    )

    if resultado == "CPF já cadastrado":
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}


@router.get("/{cpf}", response_model=MotoristaResponse)
def buscar(cpf: str):
    resultado = buscar_motorista(cpf)

    if resultado == "Motorista não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    return resultado


@router.patch("/{cpf}/inativar")
def inativar(cpf: str):
    resultado = inativar_motorista(cpf)

    if resultado == "Motorista não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado == "Motorista já está inativo.":
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}


@router.patch("/{cpf}/ativar")
def ativar(cpf: str):
    resultado = ativar_motorista(cpf)

    if resultado == "Motorista não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado == "Motorista já está ativo.":
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}
    
    
    
    
    
    
    
    