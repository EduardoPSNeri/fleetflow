"""
Contém todas as regras de negócio da aplicação.

Coordena as operações e utiliza o Repository para acessar o banco.
"""
from app.repositories.veiculo_repository import *

def gerar_numero_frota(buscar_ultimo_numero_frota,):
    if buscar_ultimo_numero_frota is None:
        return 1
    return buscar_ultimo_numero_frota + 1 

def veiculo_existe (placa):
    if placa is not None:
        return "Já existe um veículo cadastrado com esta placa."
    
    
    
    
    
    
    
    
    
    
'''    veiculo_existente = buscar_placa(veiculos, placa)

    if veiculo_existente is not None:
        return "Já existe um veículo cadastrado com esta placa."'''