'''
src/settings.py

@author Altair Bueno <altair.bueno@uma.es>
'''
from pydantic import BaseModel, BaseSettings, HttpUrl


class MongoConfig(BaseModel):
    url: str
    collection: str
    database: str

    class Config:
        frozen = True

class PaypalConfig(BaseModel):
    url: HttpUrl
    clientid: str
    secret: str
    class Config:
        frozen = True

class LocationIQConfig(BaseModel):
    apikey: str
    baseurl: HttpUrl

    class Config:
        frozen = True

class AuthSettings(BaseModel):
    baseurl: HttpUrl
    audience: str
    class Config:
        frozen = True
      
class Settings(BaseSettings):
    mongo: MongoConfig
    locationiq: LocationIQConfig
    paypal: PaypalConfig
    auth: AuthSettings

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "_"
        frozen = True

