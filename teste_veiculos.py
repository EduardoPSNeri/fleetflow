from app.services.veiculo_service import (cadastrar_veiculo)

veiculos = []

resultado1 = cadastrar_veiculo(veiculos, "ABC-12X4", "Fiat", "palio", 130000)

print(resultado1)

print("Quantidade de veiculos cadastrados: ", len(veiculos))
print(veiculos[0].numero_frota)
print(veiculos[0].placa)
print(veiculos[0].marca)
print(veiculos[0].modelo)
print(veiculos[0].km)
print(veiculos[0].ativo)




