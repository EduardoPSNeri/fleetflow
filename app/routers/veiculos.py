import select
from typing_extensions import Annotated
from fastapi import APIRouter, HTTPException, Query
from app.models.veiculo_model import Veiculo_table
from app.schemas.veiculo_schema import *
from app.services.veiculo_service import SessionDep

router = APIRouter(
    prefix="/veiculos",
    tags=["veiculos"]
)


@router.get("/")
def list_veiculos():
    return {"message": "Veiculo deleted successfully"}
    


@router.get("/")
def create_veiculo():
    return {"message": "Veiculo deleted successfully"}

@router.put("/")
def update_veiculo():
    return {"message": "Veiculo deleted successfully"}


@router.delete("/")
def delete_veiculo():
    return {"message": "Veiculo deleted successfully"}