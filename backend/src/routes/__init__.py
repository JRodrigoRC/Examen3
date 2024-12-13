'''
src/routes/__init__.py

@author Altair Bueno <altair.bueno@uma.es>
'''
from fastapi import APIRouter, Depends

from ..auth import Authentication, Claims
from ..beans import get_collection, get_locationiq_service
from ..service import LocationIQService
from .orders import ordersRouter
from .parada import paradaRouter

BaseRouter = APIRouter()

"""
@BaseRouter.get("/example")
async def example(collection=Depends(get_collection)):
    return [x async for x in collection.find({}, {"_id":0})]

@BaseRouter.get("/geocoding")
async def geocoding(query: str,service:LocationIQService=Depends(get_locationiq_service)):
    return await service.search(query)

@BaseRouter.get("/requires_auth")
async def requires_auth(auth: Claims=Depends(Authentication)):
    print(auth.json())
    return "Hello world"
"""

#BaseRouter.include_router(ordersRouter)
BaseRouter.include_router(paradaRouter)
