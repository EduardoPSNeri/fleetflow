"""
Contém todas as regras de negócio da aplicação.

Coordena as operações e utiliza o Repository para acessar o banco.
"""

def gerar_numero_frota(ultimo_numero_frota):
    if ultimo_numero_frota is None:
        return 1
    return ultimo_numero_frota +1 

def veiculo_existe (placa):
    if placa is not None:
        return "Já existe um veículo cadastrado com esta placa."
    