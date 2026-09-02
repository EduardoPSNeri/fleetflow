from fastapi import APIRouter, HTTPException

from app.schemas.diario_bordo_schema import (
    SaidaCreate, ChegadaCreate, DiarioBordoResponse)

from app.services.diario_bordo_service import (
    registrar_saida,
    registrar_chegada,
    listar_diarios
)


router = APIRouter(
    prefix="/diario-bordo",
    tags=["Diário de Bordo"]
)


@router.get("/", response_model=list[DiarioBordoResponse])
def listar():
    return listar_diarios()


@router.post("/saida", status_code=201)
def saida(dados: SaidaCreate):
    resultado = registrar_saida(
        dados.placa.upper(),
        dados.cpf,
        dados.data,
        dados.hora_saida,
        dados.km_saida
    )

    if resultado in [
        "Veículo não encontrado",
        "Motorista não encontrado"
    ]:
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado in [
        "Veículo já possui uma saída em aberto",
        "Motorista já possui uma saída em aberto",
        "KM de saída inválido"
    ]:
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}


@router.patch("/chegada")
def chegada(dados: ChegadaCreate):
    resultado = registrar_chegada(
        dados.placa.upper(),
        dados.hora_chegada,
        dados.km_chegada
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado in [
        "Nenhuma saída em aberto para este veículo",
        "KM de chegada inválido"
    ]:
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado} 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    