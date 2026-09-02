from fastapi import FastAPI

from app.database.database import inicializar_banco

from app.routers.veiculos import router as veiculos_router
from app.routers.motoristas import router as motoristas_router
from app.routers.abastecimentos import router as abastecimentos_router
from app.routers.diario_bordo import router as diario_bordo_router
from app.routers.manutencoes import router as manutencoes_router


app = FastAPI()

inicializar_banco()


app.include_router(veiculos_router)
app.include_router(motoristas_router)
app.include_router(abastecimentos_router)
app.include_router(diario_bordo_router)
app.include_router(manutencoes_router)