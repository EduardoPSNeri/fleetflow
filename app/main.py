from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.database.database import inicializar_banco

from app.routers.veiculos import router as veiculos_router
from app.routers.motoristas import router as motoristas_router
from app.routers.abastecimentos import router as abastecimentos_router
from app.routers.diario_bordo import router as diario_bordo_router
from app.routers.manutencoes import router as manutencoes_router
from app.routers.dashboard import router as dashboard_router
from app.routers.trocas_oleo import router as trocas_oleo_router



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

inicializar_banco()


app.include_router(veiculos_router)
app.include_router(motoristas_router)
app.include_router(abastecimentos_router)
app.include_router(diario_bordo_router)
app.include_router(manutencoes_router)
app.include_router(dashboard_router)
app.include_router(trocas_oleo_router)