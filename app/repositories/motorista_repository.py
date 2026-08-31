def adicionar_motorista(motoristas, novo_motorista):
    motoristas.append(novo_motorista)
    return novo_motorista


def buscar_cpf(motoristas, cpf_procurado):
    for motorista in motoristas:
        if motorista.cpf == cpf_procurado:
            return motorista
    return None


def motoristas_cadastrados(motoristas):
    return motoristas
        