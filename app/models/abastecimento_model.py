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
        
        
        

