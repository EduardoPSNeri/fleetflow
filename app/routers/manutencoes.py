from fastapi import APIRouter, HTTPException

from app.schemas.manutencao_schema import (ManutencaoCreate, ManutencaoResponse)
from app.services.manutencao_service import (
    cadastrar_manutencao, listar_manutencoes, historico_manutencoes_veiculo)


router = APIRouter(
    prefix="/manutencoes",
    tags=["Manutenções"]
)


@router.get("/")
def listar():
    return listar_manutencoes()


@router.post("/", status_code=201)
def cadastrar(manutencao: ManutencaoCreate):
    resultado = cadastrar_manutencao(
        manutencao.placa.upper(),
        manutencao.tipo,
        manutencao.descricao,
        manutencao.data,
        manutencao.km,
        manutencao.valor
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado in [
        "Tipo de manutenção inválido",
        "Valor de manutenção inválido",
        "KM da manutenção inválido"
    ]:
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}


@router.get("/{placa}/historico")
def historico(placa: str):
    return historico_manutencoes_veiculo(
        placa.upper()
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    