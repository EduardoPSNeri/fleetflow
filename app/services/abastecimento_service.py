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
        custo_por_km_anterior = (ultimo_abastecimento.valor_total / distancia_percorrida)

        ultimo_abastecimento.custo_por_km = custo_por_km_anterior
        
        

    novo_abastecimento = Abastecimento(data,veiculo_encontrado,km,combustivel,valor_litro,quantidade_litro)

    novo_abastecimento.media_consumo = media_consumo

    adicionar_abastecimento(abastecimentos, novo_abastecimento)

    veiculo_encontrado.atualizar_km(km)

    return "Abastecimento cadastrado com sucesso"


def historico_abastecimento_veiculo(veiculos, abastecimentos, placa):
    
    veiculo_encontrado = buscar_placa(veiculos, placa)
    
    if not veiculo_encontrado:
        return "Veiculo não encontrado"
    
    historico = abastecimento_por_veiculo(abastecimentos, veiculo_encontrado)
    
    if not historico:
        return "Nenhum abastecimento Registrado"
    
    return historico
   

def calcular_media_consumo_geral(historico):

    soma_medias = 0
    quantidade_medias = 0

    for abastecimento in historico:
        
        if  abastecimento.media_consumo is not None:
            soma_medias += abastecimento.media_consumo 
            quantidade_medias += 1
            
    if quantidade_medias == 0:
        return None
           
    return soma_medias / quantidade_medias
    
    
def calcular_total_gasto(historico):
    
    total  = 0
    
    for abastecimento in historico:
        total = total + abastecimento.valor_total
        
    return total
    
    
def calcular_total_litros(historico):
    
    total = 0
    
    
    for abastecimento in historico:
        total = total + abastecimento.quantidade_litro
        
    return total
    
    
def quantidade_abastecimento(historico):
    total = len(historico)
    return total


def calcular_distancia_historico(historico):
    
    if len(historico) < 2:
        return None
    
    inicial_km = historico[0].km
    ultimo_km =  historico[-1].km
 
    distancia_percorrida = ultimo_km - inicial_km
    
    return distancia_percorrida


def calcular_media_custo_por_km(historico):

    soma_custos = 0
    quantidade = 0

    for abastecimento in historico:

        if abastecimento.custo_por_km is not None:
            soma_custos += abastecimento.custo_por_km
            quantidade += 1
            
    if quantidade == 0 :
         return None
        
    return soma_custos / quantidade
        
    
    
    
    
    
    
    

#relatorios
def gerar_resumo_abastecimento(historico):
    
    total_gasto = calcular_total_gasto(historico)
    total_litros = calcular_total_litros(historico)
    quantidade = quantidade_abastecimento(historico)
    media_consumo =calcular_media_consumo_geral(historico)
    media_custo_km = calcular_media_custo_por_km(historico)
    
    return{
        "Total_Gasto": total_gasto,
        "Total_abastecido": total_litros,
        "Quantidade_abastecimento":quantidade,
        "Media_Consumo":media_consumo,
        "Media_Custo_KM": media_custo_km,
        
    }
    
    
def resumo_abastecimento_veiculo(veiculos, abastecimentos, placa):
    
    historico = historico_abastecimento_veiculo(veiculos, abastecimentos, placa)    
    if isinstance (historico, str):
        return historico
    
    return gerar_resumo_abastecimento(historico)
        
        


      
      
        