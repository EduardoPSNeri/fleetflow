from app.models.motorista_model import Motorista
from app.repositories.motorista_repository import(adicionar_motorista, buscar_cpf,motoristas_cadastrados )


def cadastro_motorista(motoristas, nome, cpf, cnh, categoria_cnh):
    
    cpf_existente = buscar_cpf(motoristas, cpf)

    if cpf_existente is not None:
        return "CPF já cadastrado"

    novo_motorista = Motorista(nome, cpf, cnh, categoria_cnh)

    adicionar_motorista(motoristas, novo_motorista)

    return "Motorista cadastrado com sucesso"


def inativar_motorista(motoristas, cpf):
    motorista_encontrado = buscar_cpf(motoristas, cpf)

    if not motorista_encontrado:
        return "Motorista não encontrado"

    return motorista_encontrado.inativar()


def ativar_motorista(motoristas, cpf):
    motorista_encontrado = buscar_cpf(motoristas, cpf)

    if not motorista_encontrado:
        return "Motorista não encontrado"

    return motorista_encontrado.ativar()


