from sqlalchemy import Column, Integer, String, ForeignKey
from pokemon.database import Base



class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    image = Column(String)
    



