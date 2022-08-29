# Creating an API in docker with FastAPI.
Based on this [TUTORIAL](https://www.youtube.com/watch?v=qQNGw_m8t0Y)

I don't remember why but the dockerfile used is not the same as in the video. However it does pretty much the same thing and works.

### How to run

1) open docker for windows
2) `docker build -t fastapi-tutorial .`
3) `docker images` to check.
4) `docker run -p 8000:8000  fastapi-tutorial`
5) localhost:8000 in the browser