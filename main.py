from app.repositories.veiculo_repository import veiculos
from app.services.veiculo_service import cadastrar_veiculo

resultado = cadastrar_veiculo(veiculos, "ABC-1234", "FIAT", "MOBI", 190000)
print(resultado)
print(veiculos)