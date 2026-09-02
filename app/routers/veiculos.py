from fastapi import APIRouter , HTTPException


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
    resultado = buscar_veiculo(placa)

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail="Veículo não encontrado"
        )

    return resultado


@router.post("/", status_code=201)
def cadastrar(veiculo: VeiculoCreate):
    resultado = cadastrar_veiculo(
        veiculo.placa,
        veiculo.marca,
        veiculo.modelo,
        veiculo.km,
        veiculo.combustiveis
    )

    if resultado == "Veículo já cadastrado":
        raise HTTPException(
            status_code=400,
            detail="Veículo já cadastrado"
        )

    if resultado in [
        "Placa inválida",
        "Placa Mercosul invalida",
        "KM invalido"
    ]:
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}

    
@router.patch("/{placa}/inativar")
def inativar(placa: str):
    resultado = inativar_veiculo(placa.upper())

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado == "O veículo já está inativo.":
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}


@router.patch("/{placa}/ativar")
def ativar(placa: str):
    resultado = ativar_veiculo(placa.upper())

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado == "O veículo já está ativo.":
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}


@router.patch("/{placa}/km/{novo_km}")
def atualizar_km(placa: str, novo_km: float):
    resultado = atualizar_km_veiculo(
        placa.upper(),
        novo_km
    )

    if resultado == "Veículo não encontrado":
        raise HTTPException(
            status_code=404,
            detail=resultado
        )

    if resultado == "KM inválido":
        raise HTTPException(
            status_code=400,
            detail=resultado
        )

    return {"message": resultado}
    
    
    
    
    
    
    