from fastapi import APIRouter

from app.services.dashboard_service import resumo_dashboard


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def resumo():
    return resumo_dashboard()











