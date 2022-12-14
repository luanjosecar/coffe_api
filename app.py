from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi
from routes import users, readings, implementations
from fastapi.middleware.cors import CORSMiddleware

from initializer.postgres import create_databases
from initializer.mongo import create_mongo
app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Coffe PWA API",
        version="0.1.0",
        description="API para manipulação das ações dentro do sistema",
        contact={
        "name": "Luan José de Almeida Cardoso",
        "email": "140150161@aluno.unb.br",
    },
        routes=app.routes,
    )    
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def start_databases():
    create_databases()
    create_mongo()

app.include_router(users.router)
app.include_router(readings.router)
app.include_router(implementations.router)

app.openapi = custom_openapi