from app.repositories.dashboard_repository import (buscar_resumo_veiculos_banco, buscar_resumo_abastecimentos_banco,
buscar_resumo_manutencoes_banco, buscar_resumo_motoristas_banco, buscar_veiculo_maior_custo_banco,
buscar_ranking_custos_banco, buscar_manutencoes_por_veiculo_banco, buscar_media_consumo_por_veiculo_banco, buscar_resumo_trocas_oleo_banco )
from app.services.manutencao_service import (listar_alertas_manutencao)
from app.services.troca_oleo_service import (listar_alertas_troca_oleo)


def resumo_dashboard():
    veiculos = buscar_resumo_veiculos_banco()
    motoristas = buscar_resumo_motoristas_banco()
    abastecimentos = buscar_resumo_abastecimentos_banco()
    manutencoes = buscar_resumo_manutencoes_banco()
    veiculo_maior_custo = buscar_veiculo_maior_custo_banco()
    ranking_custos = buscar_ranking_custos_banco()
    manutencoes_por_veiculo = buscar_manutencoes_por_veiculo_banco()
    media_consumo_por_veiculo = buscar_media_consumo_por_veiculo_banco()
    alertas_manutencao = listar_alertas_manutencao()
    alertas_troca_oleo = listar_alertas_troca_oleo()
    trocas_oleo = buscar_resumo_trocas_oleo_banco()

    total_combustivel = abastecimentos[1] or 0
    total_manutencoes = manutencoes[1] or 0
    total_trocas_oleo = trocas_oleo[1] or 0
    custo_total_frota = total_combustivel + total_manutencoes + total_trocas_oleo
    

    if veiculos[0] > 0:
        custo_medio_por_veiculo = round(custo_total_frota / veiculos[0], 2)
    else:
        custo_medio_por_veiculo = 0

    ranking_formatado = []

    for veiculo in ranking_custos:
        ranking_formatado.append({
            "placa": veiculo[0],
            "custo_total": round(veiculo[1], 2)
        })
        
    manutencoes_formatadas = []

    for veiculo in manutencoes_por_veiculo:
        manutencoes_formatadas.append({
            "placa": veiculo[0],
            "total_manutencoes": veiculo[1]
        })
        
        media_consumo_formatada = []

    for veiculo in media_consumo_por_veiculo:
        media_consumo_formatada.append({
            "placa": veiculo[0],
            "media_consumo": round(veiculo[1], 2) if veiculo[1] is not None else None
        })
        
        veiculos_com_media = []

    for veiculo in media_consumo_formatada:
        if veiculo["media_consumo"] is not None:
            veiculos_com_media.append(veiculo)
            
        if veiculos_com_media:
            melhor_consumo = veiculos_com_media[0]
            pior_consumo = veiculos_com_media[-1]
        else:
            melhor_consumo = None
            pior_consumo = None
                
    total_ok = 0
    total_proximos = 0
    total_vencidos = 0

    for alerta in alertas_manutencao:
        if alerta["status"] == "OK":
            total_ok += 1

        elif alerta["status"] == "Próximo":
            total_proximos += 1

        elif alerta["status"] == "Vencida":
            total_vencidos += 1
        
    oleo_ok = 0
    oleo_proximos = 0
    oleo_vencidos = 0

    for alerta in alertas_troca_oleo:
        if alerta["status"] == "OK":
            oleo_ok += 1

        elif alerta["status"] == "Próximo":
            oleo_proximos += 1

        elif alerta["status"] == "Vencida":
            oleo_vencidos += 1    
            
            
                     
    return {
        "total_veiculos": veiculos[0],
        "veiculos_ativos": veiculos[1] or 0,
        "veiculos_inativos": veiculos[2] or 0,
        "total_motoristas": motoristas,
        "total_abastecimentos": abastecimentos[0],
        "total_gasto_combustivel": total_combustivel,
        "total_manutencoes": manutencoes[0],
        "total_gasto_manutencoes": total_manutencoes,
        "custo_total_frota": custo_total_frota,
        "total_trocas_oleo": trocas_oleo[0],
        "total_gasto_trocas_oleo": total_trocas_oleo,
        "custo_medio_por_veiculo": custo_medio_por_veiculo,
        "media_consumo_por_veiculo": media_consumo_formatada,
        "melhor_consumo": melhor_consumo,
        "pior_consumo": pior_consumo,
        "alertas_manutencao": {
        "ok": total_ok,
        "proximos": total_proximos,
        "vencidos": total_vencidos
},
    "alertas_troca_oleo": {
    "ok": oleo_ok,
    "proximos": oleo_proximos,
    "vencidos": oleo_vencidos
},
        
        "manutencoes_por_veiculo": manutencoes_formatadas,
        

        "veiculo_maior_custo": {
            "placa": veiculo_maior_custo[0],
            "custo_total": round(veiculo_maior_custo[1], 2)
        } if veiculo_maior_custo else None,

        "ranking_custos": ranking_formatado
    }
    
    
    
    
    
    
    
    