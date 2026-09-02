from fastapi import APIRouter

from app.schemas.abastecimento_schema import AbastecimentoCreate
from app.services.abastecimento_service import (
    cadastrar_abastecimento, listar_abastecimentos, historico_abastecimento_veiculo, resumo_abastecimento_veiculo, 
)


router = APIRouter(
    prefix="/abastecimentos",
    tags=["Abastecimentos"]
)


@router.get("/")
def listar():
    return listar_abastecimentos()


@router.post("/")
def cadastrar(abastecimento: AbastecimentoCreate):
    return cadastrar_abastecimento(
        abastecimento.placa,
        abastecimento.data,
        abastecimento.km,
        abastecimento.combustivel,
        abastecimento.valor_litro,
        abastecimento.quantidade_litro
    )
    
    
@router.get("/{placa}/historico")
def historico(placa: str):
    return historico_abastecimento_veiculo(
    placa.upper()
)


@router.get("/{placa}/resumo")
def resumo(placa: str):
    return resumo_abastecimento_veiculo(
        placa.upper()
    )
    
    
    
    
    
    
    
    