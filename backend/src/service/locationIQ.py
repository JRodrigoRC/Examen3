from typing import List
from ..settings import LocationIQConfig
from ..model import SearchLocationIQ

from httpx import AsyncClient

class LocationIQService:
    config: LocationIQConfig
    def __init__(self, config) -> None:
        self.config = config

    async def search(self, query)->List[SearchLocationIQ]:
        '''https://locationiq.com/docs#search-forward-geocoding'''
        params = {
            "key" : self.config.apikey,
            "format": "json",
            "q": query
        }
        
        async with AsyncClient(base_url=self.config.baseurl) as client:
            response = await client.get("/v1/search" , params=params)
            payload = response.json()
        
        return [SearchLocationIQ(**x) for x in payload]
        
