from fastapi import APIRouter, HTTPException

from app.schemas.troca_oleo_schema import TrocaOleoCreate
from app.services.troca_oleo_service import listar_alertas_troca_oleo

from app.services.troca_oleo_service import (
    cadastrar_troca_oleo,
    listar_trocas_oleo,
    historico_trocas_oleo
)


router = APIRouter(
    prefix="/trocas-oleo",
    tags=["Trocas de óleo"]
)


@router.get("/")
def listar():
    return listar_trocas_oleo()


@router.post("/", status_code=201)
def cadastrar(troca: TrocaOleoCreate):

    resultado = cadastrar_troca_oleo(
        troca.placa.upper(),
        troca.data,
        troca.km,
        troca.tipo_oleo,
        troca.proxima_troca_km,
        troca.valor
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado in [
        "KM da troca inválido",
        "Próxima troca inválida",
        "Valor inválido"
    ]:
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {
        "mensagem": resultado
    }


@router.get("/alertas")
def alertas():
    return listar_alertas_troca_oleo()


@router.get("/{placa}/historico")
def historico(placa: str):

    resultado = historico_trocas_oleo(
        placa.upper()
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    return resultado





