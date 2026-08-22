from app.services.veiculo_service import (
    cadastrar_veiculo, inativar_veiculo, ativar_veiculo, atualizar_km_veiculo)

veiculos = []

resultado1 = cadastrar_veiculo(veiculos, "ABC-1234", "Fiat", "palio", 130000)


print(resultado1)
print(veiculos[0].km)

resultado1 = atualizar_km_veiculo(veiculos, "ABC-1234", 135000)
print(resultado1)
print(veiculos[0].km)

resultado1= atualizar_km_veiculo(veiculos, "ABC-1234", 130000)
print(resultado1)
print(veiculos[0].km)

resultado1= atualizar_km_veiculo(veiculos, "ABC-1234", 120000)
print(resultado1)
print(veiculos[0].km)

print("Quantidade de veiculos cadastrados: ", len(veiculos))



