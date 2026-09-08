from app.repositories.dashboard_repository import (buscar_resumo_veiculos_banco, buscar_resumo_abastecimentos_banco,
buscar_resumo_manutencoes_banco, buscar_resumo_motoristas_banco)


def resumo_dashboard():
    veiculos = buscar_resumo_veiculos_banco()
    motoristas = buscar_resumo_motoristas_banco()
    abastecimentos = buscar_resumo_abastecimentos_banco()
    manutencoes = buscar_resumo_manutencoes_banco()

    return {
        "total_veiculos": veiculos[0],
        "veiculos_ativos": veiculos[1] or 0,
        "veiculos_inativos": veiculos[2] or 0,
        "total_motoristas": motoristas,
        "total_abastecimentos": abastecimentos[0],
        "total_gasto_combustivel": abastecimentos[1] or 0,
        "total_manutencoes": manutencoes[0],
        "total_gasto_manutencoes": manutencoes[1] or 0
    }
    
    
    
    
    
    
    
    