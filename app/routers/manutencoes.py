from fastapi import APIRouter

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


@router.post("/")
def cadastrar(manutencao: ManutencaoCreate):
    return cadastrar_manutencao(
        manutencao.placa.upper(),
        manutencao.tipo,
        manutencao.descricao,
        manutencao.data,
        manutencao.km,
        manutencao.valor
    )


@router.get("/{placa}/historico")
def historico(placa: str):
    return historico_manutencoes_veiculo(
        placa.upper()
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    