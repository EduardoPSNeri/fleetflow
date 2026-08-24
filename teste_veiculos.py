from app.services.veiculo_service import (
cadastrar_veiculo)
from app.services.abastecimento_service import (cadastrar_abastecimento, historico_abastecimento_veiculo,
resumo_abastecimento_veiculo)

veiculos = []
abastecimentos = []

resultado1 = cadastrar_veiculo(veiculos, "ABC-1234", "Fiat", "palio", 130000)
resultado2 = cadastrar_abastecimento(abastecimentos,veiculos,"ABC-1234","23/08/2026",140000,"Gasolina",    6.00,    50)
resultado3 = cadastrar_abastecimento(abastecimentos,     veiculos,    "ABC-1234",   "23/08/2026",    145000,    "Gasolina",    6.00,    50)

historico = historico_abastecimento_veiculo(veiculos, abastecimentos, "ABC-1234")
resumo = resumo_abastecimento_veiculo(veiculos, abastecimentos, "ABC-1234")


print()
print(resumo)
print()
print( "================================================================================================")

