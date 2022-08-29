from models.movie_model import MovieModel
from typing import Optional
from starlette.routing import request_response
import httpx  # podria usar la lib requests. en el tutorial usan esta. Beneficios de async

# definis funcion asincronica

# Optional -> o devuelve MovieModel o None, ambas son validas


async def get_movie(title_subtext: str) -> Optional[MovieModel]:
    url = f'https://movieservice.talkpython.fm/api/search/{title_subtext}'

    # To make asynchronous requests, you'll need an AsyncClient.
    async with httpx.AsyncClient() as client:
        # para avanzar necesitas primero la respuesta de client.get(url)
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()

        data = resp.json()  # de txt a dict

    results = data['hits']
    if not results:
        None

    # El json resultante se le pasa a MovieModel y chequea que cumpla todo
    movie = MovieModel(**results[0])
    return movie
