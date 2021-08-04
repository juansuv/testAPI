from typing import List

import requests
from fastapi import APIRouter, Depends, status, HTTPException, Request
from pokemon import schemas, database, models
from sqlalchemy.orm import Session
from pokemon.repository import pokemon
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

router = APIRouter(
    prefix="/pokemon",
    tags=['Pokemons']
)

get_db = database.get_db


templates = Jinja2Templates(directory="pokemon\\templates")



@router.get('/', response_model=List[schemas.ShowPokemon])
def all(request: Request,db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        "pokemons2.html", {"request": request,"datos":pokemon.get_all(db)})
     


@router.get('/get', status_code=status.HTTP_201_CREATED)
def pokemos_from_service(db: Session = Depends(get_db)):
    pokemon.get_all_from_service(db)
    #url = router.url_path_for("pokemon")
    
    return RedirectResponse(url='/pokemon/')


@router.get('/{name}', response_model=List[schemas.ShowPokemon])
def pokemos_search_name(name: str, request:Request, db: Session = Depends(get_db) ):
    
    return templates.TemplateResponse(
        "pokemons2.html", {"request": request,"datos":pokemon.get_pokemon_name(name,db)})



@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Pokemon, db: Session = Depends(get_db)):
    return pokemon.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return pokemon.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Pokemon, db: Session = Depends(get_db)):
    
    return pokemon.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowPokemon)
def show(id: int, db: Session = Depends(get_db)):
    return pokemon.show(id, db)
