from app.repositories.troca_oleo_repository import (
    adicionar_troca_oleo_banco,
    listar_trocas_oleo_banco,
    trocas_oleo_por_veiculo_banco
)

from app.repositories.veiculo_repository import buscar_placa_banco


def cadastrar_troca_oleo(
    placa,
    data,
    km,
    tipo_oleo,
    proxima_troca_km,
    valor
):
    veiculo = buscar_placa_banco(placa)

    if not veiculo:
        return "Veículo não encontrado"

    km_atual = veiculo[5]

    if km > km_atual:
        return "KM da troca inválido"

    if proxima_troca_km <= km:
        return "Próxima troca inválida"

    if valor < 0:
        return "Valor inválido"

    veiculo_id = veiculo[0]

    adicionar_troca_oleo_banco(
        veiculo_id,
        data,
        km,
        tipo_oleo,
        proxima_troca_km,
        valor
    )

    return "Troca de óleo cadastrada com sucesso"


def listar_trocas_oleo():
    trocas = listar_trocas_oleo_banco()

    resultado = []

    for troca in trocas:
        resultado.append({
            "id": troca[0],
            "veiculo_id": troca[1],
            "data": troca[2],
            "km": troca[3],
            "tipo_oleo": troca[4],
            "proxima_troca_km": troca[5],
            "valor": troca[6]
        })

    return resultado


def historico_trocas_oleo(placa):
    veiculo = buscar_placa_banco(placa)

    if not veiculo:
        return "Veículo não encontrado"

    veiculo_id = veiculo[0]

    trocas = trocas_oleo_por_veiculo_banco(veiculo_id)

    resultado = []

    for troca in trocas:
        resultado.append({
            "id": troca[0],
            "veiculo_id": troca[1],
            "data": troca[2],
            "km": troca[3],
            "tipo_oleo": troca[4],
            "proxima_troca_km": troca[5],
            "valor": troca[6]
        })

    return resultado




