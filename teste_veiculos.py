from app.services.veiculo_service import (
    cadastrar_veiculo, inativar_veiculo, ativar_veiculo)

veiculos = []

resultado1 = cadastrar_veiculo(veiculos, "ABC-1234", "Fiat", "palio", 130000)


print(resultado1)
print(veiculos[0].ativo)

resultado1 = inativar_veiculo(veiculos, "ABC-1234")
print(resultado1)
print(veiculos[0].ativo)

resultado1= ativar_veiculo(veiculos, "ABC-1234")
print(resultado1)
print(veiculos[0].ativo)

resultado1= ativar_veiculo(veiculos, "ABC-1234")
print(resultado1)
print(veiculos[0].ativo)

print("Quantidade de veiculos cadastrados: ", len(veiculos))



