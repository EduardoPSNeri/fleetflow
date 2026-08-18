from app.models.veiculo_model import Veiculo
from app.repositories.veiculo_repository import (buscar_placa, buscar_ultimo_numero_frota, adicionar_veiculo)


def gerar_numero_frota(ultimo_numero_frota):
    if ultimo_numero_frota is None:
        return 1

    return ultimo_numero_frota + 1


def cadastrar_veiculo(veiculos, placa, marca, modelo, km):

    veiculo_existente = buscar_placa(veiculos, placa)

    if veiculo_existente is not None:
        return "Veículo já cadastrado"

    ultimo_numero_frota = buscar_ultimo_numero_frota(veiculos)
    proximo_numero = gerar_numero_frota(ultimo_numero_frota)

    novo_veiculo = Veiculo(
        proximo_numero,
        placa,
        marca,
        modelo,
        km
    )

    adicionar_veiculo(veiculos, novo_veiculo)

    return "Veículo cadastrado com sucesso"





    
    
    
    
