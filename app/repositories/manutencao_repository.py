from app.database.database import conectar


def adicionar_manutencao_banco(
    veiculo_id,
    tipo,
    descricao,
    data,
    km,
    valor,
    proximo_km
):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO manutencoes (
            veiculo_id,
            tipo,
            descricao,
            data,
            km,
            valor,
            proximo_km
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        veiculo_id,
        tipo,
        descricao,
        data,
        km,
        valor,
        proximo_km
    ))

    conexao.commit()
    conexao.close()


def manutencoes_por_veiculo_banco(veiculo_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM manutencoes
        WHERE veiculo_id = ?
        ORDER BY id
    """, (veiculo_id,))

    manutencoes = cursor.fetchall()

    conexao.close()

    return manutencoes


def listar_manutencoes_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM manutencoes
        ORDER BY id
    """)

    manutencoes = cursor.fetchall()

    conexao.close()

    return manutencoes


def buscar_alertas_manutencao_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            v.placa,
            v.km,
            m.descricao,
            m.proximo_km
        FROM manutencoes m

        JOIN veiculos v
            ON v.id = m.veiculo_id

        WHERE m.proximo_km IS NOT NULL

        ORDER BY m.proximo_km
    """)

    resultado = cursor.fetchall()

    conexao.close()

    return resultado



