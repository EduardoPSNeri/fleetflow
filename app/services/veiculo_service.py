from app.models.veiculo_model import Veiculo
from app.repositories.veiculo_repository import (buscar_placa, buscar_ultimo_numero_frota, adicionar_veiculo)


def gerar_numero_frota(ultimo_numero_frota):
    if ultimo_numero_frota is None:
        return 1

    return ultimo_numero_frota + 1


def validar_placa(placa):

    if len(placa) != 8:
        return False, "Placa inválida"

    if not placa[0:3].isalpha():
        return False, "Placa inválida"

    if placa[3] != "-":
        return False, "Placa inválida"

    if not placa[4:].isdigit():
        return False, "Placa inválida"

    return True, "Placa Válida"


def validar_mercosul(placa):
    
    if len(placa) != 7:
        return False, "Placa Mercosul invalida"
    
    if not placa[0:3].isalpha():
        return False, "Placa Mercosul invalida"
    
    if not placa[3].isdigit():
        return False, "Placa Mercosul invalida"

    if not placa[4].isalpha():
        return False, "Placa Mercosul invalida"

    if not placa[5:7].isdigit():
        return False, "Placa Mercosul invalida"
    
    return True, "Placa Mercosul valida"
    


def cadastrar_veiculo(veiculos, placa, marca, modelo, km):
    
    placa = placa.upper()
    
    placa_valida, mensagem = validar_placa(placa)
    if not placa_valida:
        return mensagem
    

    veiculo_existente = buscar_placa(veiculos, placa)

    if veiculo_existente is not None:
        return "Veículo já cadastrado"

    ultimo_numero_frota = buscar_ultimo_numero_frota(veiculos)
    proximo_numero = gerar_numero_frota(ultimo_numero_frota)

    novo_veiculo = Veiculo(proximo_numero, placa, marca, modelo, km)
  
    adicionar_veiculo(veiculos, novo_veiculo)

    return "Veículo cadastrado com sucesso"





    
    
    
    
