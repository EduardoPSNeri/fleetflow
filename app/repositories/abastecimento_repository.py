from app.database.database import conectar

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


def adicionar_abastecimento_banco(
    veiculo_id,
    data,
    km,
    combustivel,
    valor_litro,
    quantidade_litro,
    valor_total,
    media_consumo,
    custo_por_km
):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO abastecimentos (
            veiculo_id,
            data,
            km,
            combustivel,
            valor_litro,
            quantidade_litro,
            valor_total,
            media_consumo,
            custo_por_km
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        veiculo_id,
        data,
        km,
        combustivel,
        valor_litro,
        quantidade_litro,
        valor_total,
        media_consumo,
        custo_por_km
    ))

    conexao.commit()
    conexao.close()


def listar_abastecimentos_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM abastecimentos
    """)

    abastecimentos = cursor.fetchall()

    conexao.close()

    return abastecimentos


def buscar_ultimo_abastecimento_banco(veiculo_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM abastecimentos
        WHERE veiculo_id = ?
        ORDER BY id DESC
        LIMIT 1
    """, (veiculo_id,))

    abastecimento = cursor.fetchone()

    conexao.close()

    return abastecimento


def atualizar_custo_por_km_banco(abastecimento_id, custo_por_km):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE abastecimentos
        SET custo_por_km = ?
        WHERE id = ?
    """, (custo_por_km, abastecimento_id))

    conexao.commit()
    conexao.close()


def abastecimentos_por_veiculo_banco(veiculo_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM abastecimentos
        WHERE veiculo_id = ?
        ORDER BY id
    """, (veiculo_id,))

    abastecimentos = cursor.fetchall()

    conexao.close()

    return abastecimentos




