from app.database.database import conectar
 
    
def adicionar_veiculo_banco(numero_frota, placa, marca, modelo, km, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO veiculos (
            numero_frota,
            placa,
            marca,
            modelo,
            km,
            ativo
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        numero_frota,
        placa,
        marca,
        modelo,
        km,
        ativo
    ))

    conexao.commit()
    conexao.close()
    

def listar_veiculos_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM veiculos
    """)

    veiculos = cursor.fetchall()

    conexao.close()

    return veiculos


def buscar_ultimo_numero_frota_banco():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT MAX(numero_frota)
        FROM veiculos
    """)

    resultado = cursor.fetchone()

    conexao.close()

    return resultado[0]


def buscar_placa_banco(placa):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM veiculos
        WHERE placa = ?
    """, (placa,))

    veiculo = cursor.fetchone()

    conexao.close()

    return veiculo


def atualizar_km_banco(placa, novo_km):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE veiculos
        SET km = ?
        WHERE placa = ?
    """, (novo_km, placa))

    conexao.commit()
    conexao.close()


def atualizar_status_veiculo_banco(placa, ativo):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE veiculos
        SET ativo = ?
        WHERE placa = ?
    """, (ativo, placa))

    conexao.commit()
    conexao.close()

