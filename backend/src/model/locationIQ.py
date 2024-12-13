from typing import List, Optional
from pydantic import BaseModel
from pydantic import BaseModel, Field


class SearchLocationIQ(BaseModel):
    place_id: str
    licence: str
    osm_type: str
    osm_id: str
    boundingbox: List[str]
    lat: str
    lon: str
    display_name: str
    class_: str = Field(..., alias='class')
    type: str
    importance: float
    icon: Optional[str]

