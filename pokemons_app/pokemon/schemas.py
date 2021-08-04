from typing import List, Optional
from pydantic import BaseModel


class PokemonBase(BaseModel):

    name : str
    description : str
    image : str
    
class PokemonSearch(BaseModel):

    name : str

    class Config():
        orm_mode = True

class Pokemon(PokemonBase):
    class Config():
        orm_mode = True


class ShowPokemon(BaseModel):
    name: str
    description:str
    image: str

    class Config():
        orm_mode = True
        
class Scrapy(BaseModel):
    name: str



