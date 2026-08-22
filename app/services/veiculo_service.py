from app.models.veiculo_model import Veiculo
from app.repositories.veiculo_repository import (
    buscar_placa, buscar_ultimo_numero_frota, adicionar_veiculo)

## validações 

def gerar_numero_frota(ultimo_numero_frota):
    if ultimo_numero_frota is None:
        return 1

    return ultimo_numero_frota + 1


def validar_placa_antiga(placa):

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


def validar_km(km):
    if km <= 0:
        return False, "KM invalido"
    return True, "KM Válido"

## açoes - cadastro, atualizaçoes

def cadastrar_veiculo(veiculos, placa, marca, modelo, km):
    
    placa = placa.upper()
    
    #1 - Validações dos dados recebidos
    placa_valida_antiga, mensagem_antiga = validar_placa_antiga(placa)
    placa_mercosul_valida, mensagem_mercosul = validar_mercosul(placa)
    
    if not (placa_valida_antiga or placa_mercosul_valida):
        return (mensagem_antiga or mensagem_mercosul)
    
    km_valido, mensagem = validar_km(km)
    
    if not km_valido:
        return mensagem
    
    #2 - Consulta o Repository
    veiculo_existente = buscar_placa(veiculos, placa)

    if veiculo_existente is not None:
        return "Veículo já cadastrado"
    
    #3 - Gera o numero da frota 
    ultimo_numero_frota = buscar_ultimo_numero_frota(veiculos)
    proximo_numero = gerar_numero_frota(ultimo_numero_frota)

    #4 - salva o objeto
    novo_veiculo = Veiculo(proximo_numero, placa, marca, modelo, km)
  
    adicionar_veiculo(veiculos, novo_veiculo)

    return "Veículo cadastrado com sucesso"


def inativar_veiculo(veiculos, placa):
    veiculo_encontrado = buscar_placa(veiculos, placa)
    if not veiculo_encontrado:
        return "Veiculo não encontrado"

    return veiculo_encontrado.inativar()

    
def ativar_veiculo(veiculos, placa):
    veiculo_informado = buscar_placa(veiculos, placa)
    if not veiculo_informado:
        return "veiculo nao encontrado"
    
    return veiculo_informado.ativar()
    
    
def atualizar_km_veiculo (veiculos, placa, novo_km):
    veiculo_encontrado = buscar_placa(veiculos, placa)
    if not veiculo_encontrado:
        return "Veiculo não encontrado"
    return veiculo_encontrado.atualizar_km(novo_km)