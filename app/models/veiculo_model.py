"""
Representa a estrutura da tabela no banco de dados.

Define colunas, tipos de dados e relacionamentos entre tabelas.
"""

class Veiculo:

    def __init__(self, numero_frota, placa, marca, modelo, km):
        self.numero_frota = numero_frota
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.km = km