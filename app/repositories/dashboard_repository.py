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


def buscar_veiculo_maior_custo_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            v.placa,
            COALESCE(a.total_combustivel, 0) +
            COALESCE(m.total_manutencao, 0) AS custo_total
        FROM veiculos v

        LEFT JOIN (
            SELECT
                veiculo_id,
                SUM(valor_total) AS total_combustivel
            FROM abastecimentos
            GROUP BY veiculo_id
        ) a ON a.veiculo_id = v.id

        LEFT JOIN (
            SELECT
                veiculo_id,
                SUM(valor) AS total_manutencao
            FROM manutencoes
            GROUP BY veiculo_id
        ) m ON m.veiculo_id = v.id

        ORDER BY custo_total DESC
        LIMIT 1
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado


def buscar_ranking_custos_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            v.placa,
            COALESCE(a.total_combustivel, 0) +
            COALESCE(m.total_manutencao, 0) +
            COALESCE(o.total_troca_oleo, 0) AS custo_total

        FROM veiculos v

        LEFT JOIN (
            SELECT
                veiculo_id,
                SUM(valor_total) AS total_combustivel
            FROM abastecimentos
            GROUP BY veiculo_id
        ) a ON a.veiculo_id = v.id

        LEFT JOIN (
            SELECT
                veiculo_id,
                SUM(valor) AS total_manutencao
            FROM manutencoes
            GROUP BY veiculo_id
        ) m ON m.veiculo_id = v.id

        LEFT JOIN (
            SELECT
                veiculo_id,
                SUM(valor) AS total_troca_oleo
            FROM trocas_oleo
            GROUP BY veiculo_id
        ) o ON o.veiculo_id = v.id

        ORDER BY custo_total DESC
    """)

    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def buscar_manutencoes_por_veiculo_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            v.placa,
            COUNT(m.id) AS total_manutencoes
        FROM veiculos v

        LEFT JOIN manutencoes m
            ON m.veiculo_id = v.id

        GROUP BY v.id, v.placa

        ORDER BY total_manutencoes DESC
    """)

    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def buscar_media_consumo_por_veiculo_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            v.placa,
            AVG(a.media_consumo) AS media_consumo
        FROM veiculos v

        LEFT JOIN abastecimentos a
            ON a.veiculo_id = v.id

        GROUP BY v.id, v.placa

        ORDER BY media_consumo DESC
    """)

    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def buscar_resumo_trocas_oleo_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            SUM(valor)
        FROM trocas_oleo
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado







