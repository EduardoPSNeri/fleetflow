from app.services.veiculo_service import (
cadastrar_veiculo, inativar_veiculo, ativar_veiculo, atualizar_km_veiculo)
from app.services.abastecimento_service import (cadastrar_abastecimento)

veiculos = []
abastecimentos = []

resultado1 = cadastrar_veiculo(veiculos, "ABC-1234", "Fiat", "palio", 130000)


print(resultado1)
print(veiculos[0].km)

resultado = cadastrar_abastecimento(abastecimentos,     veiculos,    "ABC-1234",   "23/08/2026",    131500,    "Gasolina",    6.00,    50)
resultado2 = cadastrar_abastecimento(abastecimentos,     veiculos,    "ABC-1234",   "23/08/2026",    140000,    "Gasolina",    6.00,    50)
print(resultado)
print(resultado2)
print("Quantidade de abastecimentos:", len(abastecimentos))
print("Valor total:", abastecimentos[0].media_consumo)
print("Valor total:", abastecimentos[1].media_consumo)

print("Novo KM do veículo:", veiculos[0].km)



