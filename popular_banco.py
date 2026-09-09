from app.services.veiculo_service import cadastrar_veiculo
from app.services.motorista_service import cadastro_motorista
from app.services.abastecimento_service import cadastrar_abastecimento
from app.services.manutencao_service import cadastrar_manutencao


# =========================
# VEÍCULOS
# =========================

veiculos = [
    ("ABC1D23", "Fiat", "Strada", 52500, ["Gasolina", "Etanol"]),
    ("DEF2G34", "Chevrolet", "S10", 88400, ["DIESEL S10"]),
    ("GHI3J45", "Volkswagen", "Saveiro", 41300, ["Gasolina", "Etanol"]),
    ("JKL4M56", "Toyota", "Hilux", 126500, ["DIESEL S10"])
]

for veiculo in veiculos:
    resultado = cadastrar_veiculo(*veiculo)
    print("VEÍCULO:", resultado)


# =========================
# MOTORISTAS
# =========================

motoristas = [
    ("Carlos Henrique Souza", "11122233344", "12345678901", "B"),
    ("Marcos Vinicius Alves", "22233344455", "23456789012", "D"),
    ("Rafael Mendes Silva", "33344455566", "34567890123", "B")
]

for motorista in motoristas:
    resultado = cadastro_motorista(*motorista)
    print("MOTORISTA:", resultado)


# =========================
# ABASTECIMENTOS
# =========================

abastecimentos = [
    ("ABC1D23", "2026-09-01", 53000, "Gasolina", 6.19, 42),
    ("ABC1D23", "2026-09-05", 53480, "Gasolina", 6.25, 40),

    ("DEF2G34", "2026-09-02", 88900, "DIESEL S10", 6.39, 68),
    ("DEF2G34", "2026-09-07", 89550, "DIESEL S10", 6.42, 70),

    ("GHI3J45", "2026-09-03", 41750, "Gasolina", 6.15, 38),

    ("JKL4M56", "2026-09-04", 127100, "DIESEL S10", 6.45, 75)
]

for abastecimento in abastecimentos:
    resultado = cadastrar_abastecimento(*abastecimento)
    print("ABASTECIMENTO:", resultado)


# =========================
# MANUTENÇÕES
# =========================

manutencoes = [
    (
        "ABC1D23",
        "Preventiva",
        "Troca de óleo e filtro",
        "2026-09-02",
        52900,
        420,
        60000
    ),

    (
        "DEF2G34",
        "Corretiva",
        "Troca de pastilhas de freio",
        "2026-09-04",
        88800,
        980,
        None
    ),

    (
        "GHI3J45",
        "Preventiva",
        "Alinhamento e balanceamento",
        "2026-09-05",
        41700,
        250,
        50000
    ),

    (
        "JKL4M56",
        "Corretiva",
        "Reparo no sistema de suspensão",
        "2026-09-06",
        127000,
        1850,
        None
    )
]

for manutencao in manutencoes:
    resultado = cadastrar_manutencao(*manutencao)
    print("MANUTENÇÃO:", resultado)