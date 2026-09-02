from app.database.database import conectar


def adicionar_manutencao_banco(
    veiculo_id,
    tipo,
    descricao,
    data,
    km,
    valor
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
            valor
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        veiculo_id,
        tipo,
        descricao,
        data,
        km,
        valor
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






