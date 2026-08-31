from app.repositories.veiculo_repository import buscar_placa_banco
from app.repositories.abastecimento_repository import adicionar_abastecimento_banco

"""veiculo = buscar_placa_banco("GHI-7890")

print(veiculo)

veiculo_id = veiculo[0]

adicionar_abastecimento_banco(
    veiculo_id,
    "31/08/2026",
    98000,
    "Gasolina",
    6.00,
    50,
    300.00,
    None,
    None
)

print("Abastecimento salvo com sucesso")

veiculo_id = veiculo[0]

adicionar_abastecimento_banco(
    veiculo_id,
    "31/08/2026",
    100000,
    "Gasolina",
    6.00,
    50,
    300.00,
    None,
    None
)

print("Abastecimento salvo com sucesso")"""

from app.repositories.abastecimento_repository import listar_abastecimentos_banco

abastecimentos = listar_abastecimentos_banco()

print(abastecimentos)