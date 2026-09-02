from app.models.veiculo_model import Veiculo
from app.repositories.veiculo_repository import (buscar_placa_banco, adicionar_veiculo_banco, 
buscar_ultimo_numero_frota_banco, atualizar_km_banco, atualizar_status_veiculo_banco, listar_veiculos_banco)

## validações 

def gerar_numero_frota(ultimo_numero_frota):
    if ultimo_numero_frota is None:
        return 1

    return ultimo_numero_frota + 1


def buscar_veiculo(placa):
    veiculo = buscar_placa_banco(placa.upper())

    if not veiculo:
        return "Veículo não encontrado"

    return veiculo


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

def cadastrar_veiculo(placa, marca, modelo, km, combustiveis):
    
    placa = placa.upper()
    
    #1 - Validações dos dados recebidos
    placa_valida_antiga, mensagem_antiga = validar_placa_antiga(placa)
    placa_mercosul_valida, mensagem_mercosul = validar_mercosul(placa)
    
    if not (placa_valida_antiga or placa_mercosul_valida):
        return (mensagem_antiga or mensagem_mercosul)
    
    km_valido, mensagem = validar_km(km)
    
    if not km_valido:
        return mensagem
    

    veiculo_existente = buscar_placa_banco(placa)

    if veiculo_existente is not None:
        return "Veículo já cadastrado"
    

    ultimo_numero_frota = buscar_ultimo_numero_frota_banco()
    proximo_numero = gerar_numero_frota(ultimo_numero_frota)

    
    novo_veiculo = Veiculo(proximo_numero, placa, marca, modelo, km, combustiveis)
    
    adicionar_veiculo_banco(
        novo_veiculo.numero_frota,
        novo_veiculo.placa,
        novo_veiculo.marca,
        novo_veiculo.modelo,
        novo_veiculo.km,
        novo_veiculo.ativo
    )
    return "Veículo cadastrado com sucesso"


def inativar_veiculo(placa):
    veiculo_encontrado = buscar_placa_banco(placa)

    if not veiculo_encontrado:
        return "Veículo não encontrado"

    ativo = veiculo_encontrado[6]

    if not ativo:
        return "O veículo já está inativo."

    atualizar_status_veiculo_banco(placa, False)

    return "Veículo inativado com sucesso"


def ativar_veiculo(placa):
    veiculo_encontrado = buscar_placa_banco(placa)

    if not veiculo_encontrado:
        return "Veículo não encontrado"

    ativo = veiculo_encontrado[6]

    if ativo:
        return "O veículo já está ativo."

    atualizar_status_veiculo_banco(placa, True)

    return "Veículo ativado com sucesso" 
    
    
def atualizar_km_veiculo(placa, novo_km):
    veiculo_encontrado = buscar_placa_banco(placa)

    if not veiculo_encontrado:
        return "Veículo não encontrado"

    km_atual = veiculo_encontrado[5]

    if novo_km <= km_atual:
        return "KM inválido"

    atualizar_km_banco(placa, novo_km)

    return "KM atualizado com sucesso"


def listar_veiculos():
    return listar_veiculos_banco()

