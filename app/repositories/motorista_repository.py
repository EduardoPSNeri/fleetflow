from app.database.database import conectar


def adicionar_motorista_banco(nome, cpf, cnh, categoria_cnh, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO motoristas (
            nome,
            cpf,
            cnh,
            categoria_cnh,
            ativo
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        nome,
        cpf,
        cnh,
        categoria_cnh,
        ativo
    ))

    conexao.commit()
    conexao.close()


def buscar_cpf_banco(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM motoristas
        WHERE cpf = ?
    """, (cpf,))

    motorista = cursor.fetchone()

    conexao.close()

    return motorista


def listar_motoristas_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM motoristas
    """)

    motoristas = cursor.fetchall()

    conexao.close()

    return motoristas


def atualizar_status_motorista_banco(cpf, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE motoristas
        SET ativo = ?
        WHERE cpf = ?
    """, (ativo, cpf))

    conexao.commit()
    conexao.close()
