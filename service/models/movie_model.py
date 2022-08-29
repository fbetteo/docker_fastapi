from pydantic import BaseModel
from typing import List


class MovieModel(BaseModel):
    # Es un validation checker. Enforcea que todo objeto MovieModel tenga esos atributos con esos formatos. keyword obtiene por default una lista vacia
    title: str
    keywords: List[str] = []
    director: str
    year: int
