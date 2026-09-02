from app.models.motorista_model import Motorista
from app.repositories.motorista_repository import (
    adicionar_motorista_banco, buscar_cpf_banco, atualizar_status_motorista_banco, listar_motoristas_banco
)


def cadastro_motorista(nome, cpf, cnh, categoria_cnh):

    motorista_existente = buscar_cpf_banco(cpf)

    if motorista_existente is not None:
        return "CPF já cadastrado"

    novo_motorista = Motorista(
        nome,
        cpf,
        cnh,
        categoria_cnh
    )

    adicionar_motorista_banco(
        novo_motorista.nome,
        novo_motorista.cpf,
        novo_motorista.cnh,
        novo_motorista.categoria_cnh,
        novo_motorista.ativo
    )

    return "Motorista cadastrado com sucesso"


def inativar_motorista(cpf):

    motorista_encontrado = buscar_cpf_banco(cpf)

    if not motorista_encontrado:
        return "Motorista não encontrado"

    ativo = motorista_encontrado[5]

    if not ativo:
        return "Motorista já está inativo."

    atualizar_status_motorista_banco(cpf, False)

    return "Motorista inativado com sucesso"


def ativar_motorista(cpf):

    motorista_encontrado = buscar_cpf_banco(cpf)

    if not motorista_encontrado:
        return "Motorista não encontrado"

    ativo = motorista_encontrado[5]

    if ativo:
        return "Motorista já está ativo."

    atualizar_status_motorista_banco(cpf, True)

    return "Motorista ativado com sucesso"


def listar_motoristas():
    motoristas = listar_motoristas_banco()

    resultado = []

    for motorista in motoristas:
        resultado.append({
            "id": motorista[0],
            "nome": motorista[1],
            "cpf": motorista[2],
            "cnh": motorista[3],
            "categoria_cnh": motorista[4],
            "ativo": bool(motorista[5])
        })

    return resultado


def buscar_motorista(cpf):
    motorista = buscar_cpf_banco(cpf)

    if not motorista:
        return "Motorista não encontrado"

    return {
        "id": motorista[0],
        "nome": motorista[1],
        "cpf": motorista[2],
        "cnh": motorista[3],
        "categoria_cnh": motorista[4],
        "ativo": bool(motorista[5])
    }




