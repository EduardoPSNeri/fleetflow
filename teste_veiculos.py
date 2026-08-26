from app.services.veiculo_service import (
cadastrar_veiculo)
from app.services.abastecimento_service import (cadastrar_abastecimento, historico_abastecimento_veiculo,
resumo_abastecimento_veiculo)

veiculos = []
abastecimentos = []
resultado = cadastrar_veiculo(veiculos, "ABC-1234", "Fiat", "palio", 130000)


resultado1 = cadastrar_abastecimento(abastecimentos,veiculos,"ABC-1234","25/08/2026",131000,"Gasolina Comum",6.00,50)
#resultado2 = cadastrar_abastecimento(abastecimentos,veiculos,"ABC-1234","25/08/2026",131500,"Gasolina",6.00,50)
#resultado2 = cadastrar_abastecimento(abastecimentos,veiculos,"ABC-1234","25/08/2026",132000,"Gasolina",6.00,50)

resumo = resumo_abastecimento_veiculo(veiculos, abastecimentos, "ABC-1234")
print(resultado1)
print(resumo)
print("Custo/km primeiro:", abastecimentos[0].custo_por_km)
print("Custo/km segundo:", abastecimentos[1].custo_por_km) 
print("Custo/km segundo:", abastecimentos[2].custo_por_km)

