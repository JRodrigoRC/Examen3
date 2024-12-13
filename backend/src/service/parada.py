from typing import List

from src.model import Parada
from .locationIQ import LocationIQService
from ..model.parada import FilterParada


class ParadaService:
    locationiq: LocationIQService
    def __init__(self, collection, locationiq) -> None:
        self.collection = collection
        self.locationiq = locationiq

    async def get_paradas_by_address(self, address: str) -> List[Parada]:
        response = await self.locationiq.search(address)
        first = response[0] 
        f = FilterParada(
            lat=first.lat,
            lon=first.lon,
            precision=0.003
        )
        return await self.get_paradas(f)

    async def get_paradas(self, f: FilterParada) -> List[Parada]:
        pipeline = []

        if f.codLinea:
            pipeline.append({"$match": {"codLinea": f.codLinea}})
        if f.sentido:
            pipeline.append({"$match": {"sentido": f.sentido}})
        if f.nombreParada:
            pipeline.append({"$match": {"nombreParada": {"$regex": f.nombreParada, "$options": "i"}}})

        if f.lat:
            pipeline.append({
                "$match": {
                    "lat": {
                        "$gte": f.lat - f.precision, 
                        "$lt": f.lat + f.precision
                    }
                }
            })
        if f.lon:
            pipeline.append({
                "$match": {
                    "lon": {"$gte": f.lon - f.precision, "$lt": f.lon + f.precision}
                }
            })
        

        return [
            Parada(**document)
            async for document in self.collection.aggregate(pipeline)
        ]