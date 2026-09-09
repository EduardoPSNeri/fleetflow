from app.repositories.manutencao_repository import (
    adicionar_manutencao_banco, manutencoes_por_veiculo_banco, listar_manutencoes_banco, buscar_alertas_manutencao_banco)
from app.repositories.veiculo_repository import (
    buscar_placa_banco
)


def validar_tipo_manutencao(tipo):
    tipos_validos = [
        "Preventiva",
        "Corretiva"
    ]

    if tipo not in tipos_validos:
        return False, "Tipo de manutenção inválido"

    return True, "Tipo válido"


def validar_valor_manutencao(valor):
    if valor < 0:
        return False, "Valor de manutenção inválido"

    return True, "Valor válido"


def cadastrar_manutencao(
    placa,
    tipo,
    descricao,
    data,
    km,
    valor,
    proximo_km
    
):
    veiculo = buscar_placa_banco(placa)

    if not veiculo:
        return "Veículo não encontrado"

    tipo_valido, mensagem = validar_tipo_manutencao(tipo)

    if not tipo_valido:
        return mensagem

    valor_valido, mensagem = validar_valor_manutencao(valor)

    if not valor_valido:
        return mensagem

    if proximo_km is not None and proximo_km <= km:
        return "Próximo KM inválido"

    km_atual = veiculo[5]

    if km > km_atual:
        return "KM da manutenção inválido"

    veiculo_id = veiculo[0]

    adicionar_manutencao_banco(
        veiculo_id,
        tipo,
        descricao,
        data,
        km,
        valor,
        proximo_km
    )

    return "Manutenção cadastrada com sucesso"


def historico_manutencoes_veiculo(placa):
    veiculo = buscar_placa_banco(placa)

    if not veiculo:
        return "Veículo não encontrado"

    veiculo_id = veiculo[0]

    historico = manutencoes_por_veiculo_banco(
        veiculo_id
    )

    if not historico:
        return []

    resultado = []

    for manutencao in historico:
        resultado.append({
            "id": manutencao[0],
            "veiculo_id": manutencao[1],
            "tipo": manutencao[2],
            "descricao": manutencao[3],
            "data": manutencao[4],
            "km": manutencao[5],
            "valor": manutencao[6],
            "proximo_km": manutencao[7]
        })

    return resultado


def listar_manutencoes():
    manutencoes = listar_manutencoes_banco()

    resultado = []

    for manutencao in manutencoes:
        resultado.append({
            "id": manutencao[0],
            "veiculo_id": manutencao[1],
            "tipo": manutencao[2],
            "descricao": manutencao[3],
            "data": manutencao[4],
            "km": manutencao[5],
            "valor": manutencao[6],
            "proximo_km":manutencao[7]
        })

    return resultado


def listar_alertas_manutencao():
    manutencoes = buscar_alertas_manutencao_banco()

    alertas = []

    for manutencao in manutencoes:
        placa = manutencao[0]
        km_atual = manutencao[1]
        descricao = manutencao[2]
        proximo_km = manutencao[3]

        km_restantes = proximo_km - km_atual

        if km_restantes <= 0:
            status = "Vencida"

        elif km_restantes <= 1000:
            status = "Próximo"

        else:
            status = "OK"

        alertas.append({
            "placa": placa,
            "descricao": descricao,
            "km_atual": km_atual,
            "proximo_km": proximo_km,
            "km_restantes": km_restantes,
            "status": status
        })

    ordem_status = {
        "Vencida": 0,
        "Próximo": 1,
        "OK": 2
    }

    alertas.sort(
        key=lambda alerta: (
            ordem_status[alerta["status"]],
            alerta["km_restantes"]
        )
    )
    return alertas





