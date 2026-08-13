"""
Responsável pelo acesso ao banco de dados.

Executa consultas, inserções, atualizações e exclusões.
Não contém regras de negócio.
"""

veiculos = []

def buscar_ultimo_numero_frota(veiculos):
    if not veiculos:
        return None

    ultimo_veiculo = veiculos[-1]
    return ultimo_veiculo.numero_frota