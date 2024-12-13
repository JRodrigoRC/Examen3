from typing import List, Optional
from fastapi import APIRouter, Depends

from src.model import Parada
from src.auth import Authentication

from ..model import FilterParada

from ..service import ParadaService
from ..beans import get_parada_service


paradaRouter = APIRouter(tags=["Parada"], prefix="/paradas")

@paradaRouter.get("", operation_id="get_paradas", response_model=List[Parada])
async def get_paradas(
    codLinea: Optional[int] = None,
    sentido: Optional[int] = None,
    nombreParada: Optional[str] = None,
    precision: float = 1,
    lon: Optional[float] = None,
    lat: Optional[float] = None,
    auth = Depends(Authentication),
    service: ParadaService = Depends(get_parada_service)
):
    f = FilterParada(
        codLinea=codLinea,
        sentido=sentido,
        nombreParada=nombreParada,
        lon=lon,
        lat=lat,
        precision=precision
    )
    return await service.get_paradas(f)

@paradaRouter.get("/address_search", operation_id="search_by_address", response_model=List[Parada])
async def search_by_address(
    address: str, 
    service: ParadaService = Depends(get_parada_service),
    auth = Depends(Authentication),

):
    return await service.get_paradas_by_address(address)