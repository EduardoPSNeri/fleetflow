from fastapi import APIRouter

from app.schemas.diario_bordo_schema import (
    SaidaCreate,
    ChegadaCreate
)

from app.services.diario_bordo_service import (
    registrar_saida,
    registrar_chegada,
    listar_diarios
)


router = APIRouter(
    prefix="/diario-bordo",
    tags=["Diário de Bordo"]
)


@router.get("/")
def listar():
    return listar_diarios()


@router.post("/saida")
def saida(dados: SaidaCreate):
    return registrar_saida(
        dados.placa.upper(),
        dados.cpf,
        dados.data,
        dados.hora_saida,
        dados.km_saida
    )


@router.patch("/chegada")
def chegada(dados: ChegadaCreate):
    return registrar_chegada(
        dados.placa.upper(),
        dados.hora_chegada,
        dados.km_chegada
    )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    