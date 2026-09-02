from app.services.manutencao_service import (
    cadastrar_manutencao,
    historico_manutencoes_veiculo
)

print(cadastrar_manutencao(
    "GHI-7890",
    "Preventiva",
    "Troca de óleo",
    "02/09/2026",
    101150,
    350.00
))

print(historico_manutencoes_veiculo(
    "GHI-7890"
))