from app.services.veiculo_service import (cadastrar_veiculo)

veiculos = []

resultado1 = cadastrar_veiculo(veiculos, "ABC-1234", "Fiat", "palio", -130000)
'''resultado2 = cadastrar_veiculo(veiculos, "ABC1D23", "Fiat", "palio", 0)
resultado3 = cadastrar_veiculo(veiculos, "ABC123", "Fiat", "palio", 130000)'''

print(resultado1)
"""print(resultado2)
print(resultado3)"""

print("Quantidade de veiculos cadastrados: ", len(veiculos))
"""print(veiculos[0].numero_frota)
print(veiculos[0].placa)
print(veiculos[0].marca)
print(veiculos[0].modelo)
print(veiculos[0].km)
print(veiculos[0].ativo)"""




