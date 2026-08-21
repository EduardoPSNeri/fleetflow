"""
Responsável pelo acesso ao banco de dados.

Executa consultas, inserções, atualizações e exclusões.
Não contém regras de negócio.
"""

veiculos = []

##CONSULTA MAIOR NUMERO DE FROTA
def buscar_ultimo_numero_frota(veiculos):

    if not veiculos:
        return None

    maior_numero = 0

    for veiculo in veiculos:
        if veiculo.numero_frota > maior_numero:
            maior_numero = veiculo.numero_frota
    
    return maior_numero


##BUSCA SE JÁ EXISTE A PLACA CADASTRADA
def buscar_placa(veiculos, placa_procurada):
    
    for veiculo in veiculos:
        if veiculo.placa == placa_procurada:
            return veiculo
    return None
    

##ADICIONA UM VEICULO
def adicionar_veiculo(veiculos, novo_veiculo):
    veiculos.append(novo_veiculo)
    
    

