from app.services.motorista_service import (
    cadastro_motorista,
    inativar_motorista,
    ativar_motorista
)

motoristas = []

print(
    cadastro_motorista(
        motoristas,
        "João Silva",
        "12345678900",
        "123456789",
        "B"
    )
)

print(inativar_motorista(motoristas, "12345678900"))
print(inativar_motorista(motoristas, "12345678900"))

print(ativar_motorista(motoristas, "12345678900"))
print(ativar_motorista(motoristas, "12345678900"))
