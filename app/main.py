from app.routers.home import router as home_router
from app.routers.login import router as login_router
from app.routers.manutencoes import router as manutencoes_router
from app.routers.abastecimentos import router as abastecimentos_router
from app.routers.veiculos import router as veiculos_router
from app.routers.motoristas import router as motoristas_router
from fastapi import FastAPI
from app.services.veiculo_service import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

"""app.include_router(home_router)
app.include_router(login_router)
app.include_router(manutencoes_router)
app.include_router(abastecimentos_router)"""
app.include_router(veiculos_router)
"""app.include_router(motoristas_router)"""

