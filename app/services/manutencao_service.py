from app.repositories.manutencao_repository import (
    adicionar_manutencao_banco, manutencoes_por_veiculo_banco, listar_manutencoes_banco)
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
    valor
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
        valor
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
        return "Nenhuma manutenção registrada"

    return historico


def listar_manutencoes():
    return listar_manutencoes_banco()


