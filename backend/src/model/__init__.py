'''
src/model/__init__.py

@author Altair Bueno <altair.bueno@uma.es>
'''

from bson.objectid import ObjectId
from pydantic import BaseModel
from .locationIQ import *
from .paypal import *
from .order import *
from .parada import *

class PyObjectId(ObjectId):
    """Wrapper around `pymongo`'s `ObjectId` class for Pydantic"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Sample(BaseModel):
    """Sample model for PyObjectId and Pydantic"""
    id: PyObjectId
    sample: str

    class Config:
        json_encoders = {ObjectId: str}


