'''
src/__init__.py

@author Altair Bueno <altair.bueno@uma.es>
'''
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from .routes import BaseRouter

__name__='Segundo parcial. Ingeniería web'
__version__='0.1.0'
__docs__='Altair Bueno Calvente. Software 4ºA'

app = FastAPI()
app.include_router(BaseRouter)
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=__name__,
        version=__version__,
        description=__docs__,
        routes=app.routes,
    )

    # Include servers section
    openapi_schema["servers"] = [
        {"url": "/", "description": "Default"},
        {"url": "http://localhost:8000", "description": "Docker compose"},
        {"url": "https://cliente-iweb-uma.fly.dev", "description": "Fly.io"},
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

"""
# Mock Oauth authentication for development purposes
from .auth import Authentication, Claims
app.dependency_overrides[Authentication] = lambda: Claims(sub="auth0|6396209463e2aad93a9bcbec",exp=10^20,iat=1670881785,iss="https://dev-dmw70d0ct8r06evt.us.auth0.com/")
"""

"""
# Exception handlers
from fastapi import Request
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
async def unicorn_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
"""