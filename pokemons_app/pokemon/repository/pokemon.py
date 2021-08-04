from sqlalchemy.orm import Session
from pokemon import models, schemas
from fastapi import HTTPException, status
import requests
import os

def get_all(db: Session):
    pokemons = db.query(models.Pokemon).all()
    return pokemons

def get_all_from_service(db:Session):
    host = os.environ.get('SERVER_SERVICE_HOST', 'pokeapi.co/api/v2/pokemon')     
    endpoint = f'https://{host}/'    
    response = requests.get(endpoint)    
    data=[]
    try:
        data = response.json()
        #for pokemon in range(1,data['count']):
        for pokemon in range(1,10):
            endpoint = f'https://{host}/{str(pokemon)}/'
            data = requests.get(endpoint).json()
            print(data['name'],data['sprites']['front_default'])
            description=''
            for ability in data['abilities']:
                description= description+" "+ability['ability']['name']            
            new_pokemon = models.Pokemon(name=data['name'], description=description, image=data['sprites']['front_default'])
            db.add(new_pokemon)
            db.commit()
            db.refresh(new_pokemon)
            print(description)

    except ValueError:
        return ValueError
    return data

def create(request: schemas.Pokemon, db: Session):
    new_pokemon = models.Pokemon(name=request.name, description=request.description, image=request.image)
    db.add(new_pokemon)
    db.commit()
    db.refresh(new_pokemon)
    return new_pokemon


def destroy(id: int, db: Session):
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == id)

    if not pokemon.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pokemon with id {id} not found")

    pokemon.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Pokemon, db: Session):
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == id)
    
    if not pokemon.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pokemon with id {id} not found")
    
    pokemon.update({"name":request.name, "description":request.description, "image":request.image})
    db.commit()
    return 'updated'
    
def get_pokemon_name(name: str, db: Session):
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.name.like(f"%{name}%")).all()
    
    if not pokemon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pokemon with name {name} not found")
    print(pokemon)
    
    return pokemon


def show(id: int, db: Session):
    pokemon = db.query(models.Pokemon).filter(models.Pokemon.id == id).first()
    if not pokemon:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Pokemon with the id {id} is not available")
    return pokemon
