from app.database.database import conectar


def buscar_resumo_veiculos_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(CASE WHEN ativo = 1 THEN 1 ELSE 0 END),
            SUM(CASE WHEN ativo = 0 THEN 1 ELSE 0 END)
        FROM veiculos
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado


def buscar_resumo_motoristas_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM motoristas
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado[0]


def buscar_resumo_abastecimentos_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor_total)
        FROM abastecimentos
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado


def buscar_resumo_manutencoes_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor)
        FROM manutencoes
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado




