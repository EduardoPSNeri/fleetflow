from app.repositories.diario_bordo_repository import (adicionar_saida_banco,buscar_diario_aberto_banco,
    buscar_diario_aberto_motorista_banco,finalizar_diario_banco, listar_diarios_banco)
from app.repositories.veiculo_repository import (buscar_placa_banco,atualizar_km_banco)
from app.repositories.motorista_repository import (buscar_cpf_banco)


def registrar_saida(
    placa,
    cpf,
    data,
    hora_saida,
    km_saida
):
    veiculo = buscar_placa_banco(placa)

    if not veiculo:
        return "Veículo não encontrado"

    motorista = buscar_cpf_banco(cpf)

    if not motorista:
        return "Motorista não encontrado"

    veiculo_id = veiculo[0]
    motorista_id = motorista[0]

    diario_aberto = buscar_diario_aberto_banco(veiculo_id)

    if diario_aberto:
        return "Veículo já possui uma saída em aberto"

    diario_motorista_aberto = buscar_diario_aberto_motorista_banco(
        motorista_id
    )

    if diario_motorista_aberto:
        return "Motorista já possui uma saída em aberto"

    km_atual = veiculo[5]

    if km_saida < km_atual:
        return "KM de saída inválido"

    adicionar_saida_banco(
        veiculo_id,
        motorista_id,
        data,
        hora_saida,
        km_saida
    )

    return "Saída registrada com sucesso"


def registrar_chegada(
    placa,
    hora_chegada,
    km_chegada
):
    veiculo = buscar_placa_banco(placa)

    if not veiculo:
        return "Veículo não encontrado"

    veiculo_id = veiculo[0]

    diario_aberto = buscar_diario_aberto_banco(veiculo_id)

    if not diario_aberto:
        return "Nenhuma saída em aberto para este veículo"

    diario_id = diario_aberto[0]
    km_saida = diario_aberto[5]

    if km_chegada < km_saida:
        return "KM de chegada inválido"

    finalizar_diario_banco(
        diario_id,
        hora_chegada,
        km_chegada
    )

    atualizar_km_banco(
        placa,
        km_chegada
    )

    return "Chegada registrada com sucesso"


def listar_diarios():
    diarios = listar_diarios_banco()

    resultado = []

    for diario in diarios:
        resultado.append({
            "id": diario[0],
            "veiculo_id": diario[1],
            "motorista_id": diario[2],
            "data": diario[3],
            "hora_saida": diario[4],
            "km_saida": diario[5],
            "hora_chegada": diario[6],
            "km_chegada": diario[7]
        })

    return resultado





