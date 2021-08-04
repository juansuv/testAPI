from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pokemon import  models
from pokemon.database import engine
from pokemon.routers import pokemon
from scrapi.routers import scrapi
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates

app = FastAPI(title='Proyecto de prueba tusdatos.co',
            description='Obtenga los pokemos directamente de la api  https://pokeapi.co/ para mostrarlos y buscarlo, tambien encontrar un breve ejemplo de scrapi',
            version='1.0.0')

models.Base.metadata.create_all(engine)


origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/pokemon/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "pokemon\\static"),
    name="static",
)

templates = Jinja2Templates(directory="pokemon\\templates")


app.include_router(pokemon.router)
app.include_router(scrapi.router)

