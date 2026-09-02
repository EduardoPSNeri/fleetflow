from fastapi import APIRouter, HTTPException

from app.schemas.abastecimento_schema import (AbastecimentoCreate, AbastecimentoResponse)
from app.services.abastecimento_service import (
    cadastrar_abastecimento, listar_abastecimentos, historico_abastecimento_veiculo, resumo_abastecimento_veiculo, 
)


router = APIRouter(
    prefix="/abastecimentos",
    tags=["Abastecimentos"]
)


@router.get("/", response_model=list[AbastecimentoResponse])
def listar():
    return listar_abastecimentos()


@router.post("/", status_code=201)
def cadastrar(abastecimento: AbastecimentoCreate):
    resultado = cadastrar_abastecimento(
        abastecimento.placa,
        abastecimento.data,
        abastecimento.km,
        abastecimento.combustivel,
        abastecimento.valor_litro,
        abastecimento.quantidade_litro
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado in [
        "KM de abastecimento inválido",
        "Valor do litro inválido",
        "Quantidade de litros inválida",
        "Combustível inválido"
    ]:
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}   
    
    
@router.get(
    "/{placa}/historico",
    response_model=list[AbastecimentoResponse]
)
def historico(placa: str):
    resultado = historico_abastecimento_veiculo(
        placa.upper()
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    return resultado


@router.get("/{placa}/resumo")
def resumo(placa: str):
    resultado = resumo_abastecimento_veiculo(
        placa.upper()
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    return resultado  
    
    
    
    
    
    
    