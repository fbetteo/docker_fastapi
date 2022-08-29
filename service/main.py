import fastapi
import uvicorn
import movie_data
from models.movie_model import MovieModel
# https://www.youtube.com/watch?v=qQNGw_m8t0Y
app = fastapi.FastAPI()


@app.get('/')
def index():
    return {
        'messaage': 'Hello World',
        'usage': 'Call /api/movie/{title}'
    }


@app.get('/api/movie/{title}', response_model=MovieModel)
# como get_movie() es una coroutine (async) necesitas awaitearla para que devuelva el resultado
async def movie_search(title: str):
    movie = await movie_data.get_movie(title)
    if not movie:
        raise fastapi.HTTPException(status_code=404)

    # lo deovlves como dict, no se bien como afecta no hacerlo
    return movie.dict()

if __name__ == '__main__':
    uvicorn.run(app)
