"""
Contém todas as regras de negócio da aplicação.

Coordena as operações e utiliza o Repository para acessar o banco.
"""
from app.models.veiculo_model import Veiculo
from app.repositories.veiculo_repository import (
    veiculos,
    buscar_placa,
    buscar_ultimo_numero_frota
)


def gerar_numero_frota(buscar_ultimo_numero_frota,):
    if buscar_ultimo_numero_frota is None:
        return 1
    return buscar_ultimo_numero_frota + 1 

def veiculo_existe (placa):
    if placa is not None:
        return "Já existe um veículo cadastrado com esta placa."
    

def cadastrar_veiculo(veiculos):
    








    
    
    
    
    
    
    
    
    
"""
veiculo_existente = buscar_placa(veiculos, placa)
    if veiculo_existente is not None:
        return "Já existe um veículo cadastrado com esta placa." 
"""