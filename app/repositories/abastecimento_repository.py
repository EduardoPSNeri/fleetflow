

def adicionar_abastecimento(abastecimentos, novo_abastecimento):
    abastecimentos.append(novo_abastecimento)
    return novo_abastecimento
    
    
def buscar_ultimo_abastecimento(abastecimentos, veiculo):

    ultimo_abastecimento = None

    for abastecimento in abastecimentos:
        if abastecimento.veiculo == veiculo:
            ultimo_abastecimento = abastecimento

    return ultimo_abastecimento


def abastecimento_por_veiculo(abastecimentos, veiculo):
    
    abastecimentos_encontrados = []
    
    for abastecimento in abastecimentos:
        
        if abastecimento.veiculo == veiculo:
            abastecimentos_encontrados.append(abastecimento)
            
    return abastecimentos_encontrados



