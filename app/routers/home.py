from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_root():
    return {
        "system": "FleetFlow",
        "version": "0.1.0",
        "status": "online"
    }