from app.database.database import conectar


def adicionar_saida_banco(
    veiculo_id,
    motorista_id,
    data,
    hora_saida,
    km_saida
):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO diario_bordo (
            veiculo_id,
            motorista_id,
            data,
            hora_saida,
            km_saida,
            hora_chegada,
            km_chegada
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        veiculo_id,
        motorista_id,
        data,
        hora_saida,
        km_saida,
        None,
        None
    ))

    conexao.commit()
    conexao.close()


def buscar_diario_aberto_banco(veiculo_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM diario_bordo
        WHERE veiculo_id = ?
        AND hora_chegada IS NULL
        ORDER BY id DESC
        LIMIT 1
    """, (veiculo_id,))

    diario = cursor.fetchone()

    conexao.close()

    return diario


def finalizar_diario_banco(
    diario_id,
    hora_chegada,
    km_chegada
):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE diario_bordo
        SET hora_chegada = ?,
            km_chegada = ?
        WHERE id = ?
    """, (
        hora_chegada,
        km_chegada,
        diario_id
    ))

    conexao.commit()
    conexao.close()


def listar_diarios_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM diario_bordo
        ORDER BY id
    """)

    diarios = cursor.fetchall()

    conexao.close()

    return diarios


def buscar_diario_aberto_motorista_banco(motorista_id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM diario_bordo
        WHERE motorista_id = ?
        AND hora_chegada IS NULL
        ORDER BY id DESC
        LIMIT 1
    """, (motorista_id,))

    diario = cursor.fetchone()

    conexao.close()

    return diario



