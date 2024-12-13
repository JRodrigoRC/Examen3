from typing import Optional
from pydantic import BaseModel

class FilterParada(BaseModel):
    codLinea: Optional[int]
    sentido: Optional[int]
    nombreParada: Optional[str]
    precision: float = 0.003
    lon: Optional[float]
    lat: Optional[float]

"""
    nombreLinea: Optional[str]
    orden: Optional[int]
    codParada: Optional[int]
    direccion: Optional[str]
"""

class Parada(BaseModel):
    codLinea: int
    nombreLinea: str
    sentido: int
    orden: int
    codParada: int
    nombreParada: str
    direccion: str
    lon: float
    lat: float
