"""
Responsável pela configuração do banco de dados.

Cria a conexão, fornece sessões e inicializa as tabelas.
"""
import sqlite3


def conectar():
    conexao = sqlite3.connect("fleetflow.db")
    return conexao


def criar_tabela_veiculos():
    conexao = conectar()
    
#envia um comando SQL para o SQLite
    cursor = conexao.cursor()
    
#cria a tabela apenas se ela ainda não existir
    cursor.execute("""CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_frota INTEGER,
            placa TEXT,
            marca TEXT,
            modelo TEXT,
            km REAL,
            ativo INTEGER
        )
    """)
#confirma a alteração
    conexao.commit()
    
#encerra a conexão.
    conexao.close()
    

def criar_tabela_abastecimentos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS abastecimentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            veiculo_id INTEGER,
            data TEXT,
            km REAL,
            combustivel TEXT,
            valor_litro REAL,
            quantidade_litro REAL,
            valor_total REAL,
            media_consumo REAL,
            custo_por_km REAL
        )
    """)

    conexao.commit()
    conexao.close()


def criar_tabela_motoristas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS motoristas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            cnh TEXT,
            categoria_cnh TEXT,
            ativo INTEGER
        )
    """)

    conexao.commit()
    conexao.close()


def criar_tabela_diario_bordo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diario_bordo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            veiculo_id INTEGER,
            motorista_id INTEGER,
            data TEXT,
            hora_saida TEXT,
            km_saida REAL,
            hora_chegada TEXT,
            km_chegada REAL
        )
    """)

    conexao.commit()
    conexao.close()







