"""
Contém todas as regras de negócio da aplicação.

Coordena as operações e utiliza o Repository para acessar o banco.
"""
from app.models.veiculo_model import Veiculo
from app.repositories.veiculo_repository import *


##GERA O PROXIMO NUMERO DA FROTA 
def gerar_numero_frota(buscar_ultimo_numero_frota):
    if buscar_ultimo_numero_frota is None:
        return 1
    return buscar_ultimo_numero_frota + 1 


##RETORNA SE A PLACA EXISTE OU NAO
def veiculo_existe (placa):
    if placa is not None:
        return "Já existe um veículo cadastrado com esta placa."
    


def cadastrar_veiculo(veiculos, placa, marca, modelo, km):

    veiculo_existente = buscar_placa(veiculos, placa)

    if veiculo_existente is not None:
        return "Veículo já cadastrado"

    ultimo_numero_frota = buscar_ultimo_numero_frota(veiculos)
    proximo_numero = gerar_numero_frota(ultimo_numero_frota)
    
    
    novo_veiculo = Veiculo(proximo_numero, placa, marca, modelo, km)
    
    adicionar_veiculo(veiculos, novo_veiculo)
    return "Veículo cadastrado com sucesso"

    
    








    
    
    
    
    
    
    
    
    
"""
veiculo_existente = buscar_placa(veiculos, placa)
    if veiculo_existente is not None:
        return "Já existe um veículo cadastrado com esta placa." 
"""