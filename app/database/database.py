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







