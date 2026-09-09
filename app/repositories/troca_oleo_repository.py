from app.database.database import conectar


def adicionar_troca_oleo_banco(
    veiculo_id,
    data,
    km,
    tipo_oleo,
    proxima_troca_km,
    valor
):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO trocas_oleo (
            veiculo_id,
            data,
            km,
            tipo_oleo,
            proxima_troca_km,
            valor
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        veiculo_id,
        data,
        km,
        tipo_oleo,
        proxima_troca_km,
        valor
    ))

    conexao.commit()
    conexao.close()


def listar_trocas_oleo_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM trocas_oleo
        ORDER BY id
    """)

    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def trocas_oleo_por_veiculo_banco(veiculo_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM trocas_oleo
        WHERE veiculo_id = ?
        ORDER BY id
    """, (veiculo_id,))

    resultado = cursor.fetchall()

    conexao.close()

    return resultado













