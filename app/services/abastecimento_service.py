from app.models.abastecimento_model import Abastecimento
from app.repositories.abastecimento_repository import (adicionar_abastecimento, buscar_ultimo_abastecimento, abastecimento_por_veiculo)
from app.services.veiculo_service import (buscar_placa)



    
def validar_valor_litro(valor_litro):
    if valor_litro <= 0:
        return False, "Valor litro invalido"
    return True, "valor do litro válido"

def validar_quantidade_litro(quantidade_litro):
    if quantidade_litro <= 0:
        return False, "Quantidade de Litros invalida"
    return True, "Quantidade de Litros valida"




def cadastrar_abastecimento(abastecimentos,veiculos,placa,data,km,combustivel,valor_litro,quantidade_litro):

    veiculo_encontrado = buscar_placa(veiculos, placa)
    
    if not veiculo_encontrado:
        return "Veiculo não encontrado"
    
    valor_litro_valido, mensagem = validar_valor_litro(valor_litro)
    
    if not valor_litro_valido:
        return mensagem
    
    quantidade_litro_valida, mensagem = validar_quantidade_litro(quantidade_litro)
    
    if not quantidade_litro_valida:
        return mensagem
    
    if km <= veiculo_encontrado.km:
        return "km de abastecimento Invalido"
    
    ultimo_abastecimento = buscar_ultimo_abastecimento(abastecimentos,veiculo_encontrado)

    if ultimo_abastecimento is None:
        media_consumo = None
    else:
        distancia_percorrida = km - ultimo_abastecimento.km
        media_consumo = distancia_percorrida / quantidade_litro

    novo_abastecimento = Abastecimento(data,veiculo_encontrado,km,combustivel,valor_litro,quantidade_litro)

    novo_abastecimento.media_consumo = media_consumo

    adicionar_abastecimento(abastecimentos, novo_abastecimento)

    veiculo_encontrado.atualizar_km(km)

    return "Abastecimento cadastrado com sucesso"


def historio_abastecimento_veiculo(veiculo, abastecimento, placa):
    
    veiculo_encontrado = buscar_placa(veiculos, placa)
    
    if not veiculo_encontrado:
        return "Veiculo não encontrado"
    
    historico = abastecimento_por_veiculo(Abastecimento, veiculo_encontrado)
    
    if not historico:
        return "Nenhum abastecimento Registrado"
    
    return historico
    
    
    