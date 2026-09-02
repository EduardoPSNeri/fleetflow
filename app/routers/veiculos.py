from fastapi import APIRouter

from app.services.veiculo_service import (
    listar_veiculos, cadastrar_veiculo, buscar_veiculo, ativar_veiculo, inativar_veiculo, atualizar_km_veiculo, 
)

from app.schemas.veiculo_schema import (VeiculoCreate, VeiculoResponse)


router = APIRouter(
    prefix="/veiculos",
    tags=["Veículos"]
)


@router.get("/", response_model=list[VeiculoResponse])
def listar():
    return listar_veiculos()


@router.get("/{placa}", response_model=VeiculoResponse)
def buscar(placa: str):
    return buscar_veiculo(placa)


@router.post("/")
def cadastrar(veiculo: VeiculoCreate):
    return cadastrar_veiculo(
        veiculo.placa,
        veiculo.marca,
        veiculo.modelo,
        veiculo.km,
        veiculo.combustiveis
    )
    
    
@router.patch("/{placa}/inativar")
def inativar(placa: str):
    return inativar_veiculo(placa.upper())


@router.patch("/{placa}/ativar")
def ativar(placa: str):
    return ativar_veiculo(placa.upper())    
    
    
@router.patch("/{placa}/km/{novo_km}")
def atualizar_km(placa: str, novo_km: float):
    return atualizar_km_veiculo(
        placa.upper(),
        novo_km
    )    
    
    
    
    
    
    
    
    