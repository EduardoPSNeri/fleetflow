from app.models.abastecimento_model import (Abastecimento, validar_combustivel)
from app.repositories.abastecimento_repository import (adicionar_abastecimento_banco, buscar_ultimo_abastecimento_banco,
atualizar_custo_por_km_banco, abastecimentos_por_veiculo_banco)
from app.repositories.veiculo_repository import (buscar_placa_banco, atualizar_km_banco)


def validar_valor_litro(valor_litro):
    if valor_litro <= 0:
        return False, "Valor litro invalido"
    return True, "valor do litro válido"


def validar_quantidade_litro(quantidade_litro):
    if quantidade_litro <= 0:
        return False, "Quantidade de Litros invalida"
    return True, "Quantidade de Litros valida"


def cadastrar_abastecimento(placa,data,km,combustivel,valor_litro,quantidade_litro):

    veiculo_encontrado = buscar_placa_banco(placa)

    if not veiculo_encontrado:
        return "Veículo não encontrado"

    veiculo_id = veiculo_encontrado[0]
    km_atual = veiculo_encontrado[5]

    if km <= km_atual:
        return "KM de abastecimento inválido"

    combustivel_valido, mensagem = validar_combustivel(combustivel)

    if not combustivel_valido:
        return mensagem

    valor_total = valor_litro * quantidade_litro

    ultimo_abastecimento = buscar_ultimo_abastecimento_banco(veiculo_id)

    media_consumo = None

    if ultimo_abastecimento is not None:
        ultimo_abastecimento_id = ultimo_abastecimento[0]
        ultimo_km = ultimo_abastecimento[3]
        ultimo_valor_total = ultimo_abastecimento[7]

        distancia_percorrida = km - ultimo_km

        media_consumo = distancia_percorrida / quantidade_litro
        
        custo_por_km = ultimo_valor_total / distancia_percorrida
        
        atualizar_custo_por_km_banco(ultimo_abastecimento_id,custo_por_km)
        

    adicionar_abastecimento_banco(
        veiculo_id,
        data,
        km,
        combustivel,
        valor_litro,
        quantidade_litro,
        valor_total,
        media_consumo,
        None
    )

    atualizar_km_banco(placa, km)

    return "Abastecimento cadastrado com sucesso"


def historico_abastecimento_veiculo(placa):
    veiculo_encontrado = buscar_placa_banco(placa)

    if not veiculo_encontrado:
        return "Veículo não encontrado"

    veiculo_id = veiculo_encontrado[0]

    historico = abastecimentos_por_veiculo_banco(veiculo_id)

    if not historico:
        return "Nenhum abastecimento registrado"

    return historico
   

def calcular_media_consumo_geral(historico):

    soma_medias = 0
    quantidade_medias = 0

    for abastecimento in historico:
        
        if  abastecimento[8] is not None:
            soma_medias += abastecimento[8]
            quantidade_medias += 1
            
    if quantidade_medias == 0:
        return None
           
    return soma_medias / quantidade_medias
    
    
def calcular_total_gasto(historico):
    
    total  = 0
    
    for abastecimento in historico:
        total = total + abastecimento[7]
        
    return total
    
    
def calcular_total_litros(historico):
    
    total = 0
    
    
    for abastecimento in historico:
        total = total + abastecimento[6]
        
    return total
    
    
def quantidade_abastecimento(historico):
    total = len(historico)
    return total


def calcular_distancia_historico(historico):
    
    if len(historico) < 2:
        return None
    
    inicial_km = historico[0][3]
    ultimo_km =  historico[-1][3]
 
    distancia_percorrida = ultimo_km - inicial_km
    
    return distancia_percorrida


def calcular_media_custo_por_km(historico):

    soma_custos = 0
    quantidade = 0

    for abastecimento in historico:

        if abastecimento[9] is not None:
            soma_custos += abastecimento[9]
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
    
    
def resumo_abastecimento_veiculo(placa):

    historico = historico_abastecimento_veiculo(placa)

    if isinstance(historico, str):
        return historico

    return gerar_resumo_abastecimento(historico)



      
      
        