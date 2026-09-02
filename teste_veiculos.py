from app.database.database import conectar


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
    999,
    999,
    "2026-09-02",
    "08:00",
    1000,
    None,
    None
))

conexao.commit()
conexao.close()