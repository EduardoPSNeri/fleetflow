class Abastecimento:
    
    def __init__ (self, data, veiculo, km , combustivel, valor_litro, quantidade_litro):
        self.data = data
        self.veiculo = veiculo
        self.km = km
        self.combustivel = combustivel
        self.valor_litro = valor_litro
        self.quantidade_litro = quantidade_litro
        self.valor_total = valor_litro * quantidade_litro
        self.media_consumo = None
        self.custo_por_km = None
        
        
def validar_combustivel(combustivel):

    combustiveis_validos = {
        "Gasolina",
        "Etanol",
        "DIESEL S10",
        "DIESEL S500",
    }

    combustivel_normalizado = combustivel.strip().lower()

    if combustivel_normalizado not in combustiveis_validos:
        return False, "Combustível inválido"

    return True, combustiveis_validos[combustivel_normalizado]
        
        
        

