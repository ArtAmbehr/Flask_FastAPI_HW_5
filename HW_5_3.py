import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from random import choice

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []
genres = ['comedy', 'adventure', 'melodrama']

for i in range(10):
    movie = Movie(id=i,
                  title=f'title{i}',
                  description=f'description',
                  genre=f'{choice(genres)}')
    movies.append(movie)


# @app.get("/movies/", response_model=List[Movie])
# def get_movies():
#     return movies
#
#
# @app.get("/movies/{name_genre", response_model=List[Movie])
# def selection_by_genre(name_genre: str):
#     new_list = []
#     for obj in movies:
#         if obj.genre == name_genre:
#             new_list.append(obj)
#
#     if new_list:
#         return new_list
#     else:
#         raise HTTPException(status_code=404,
#                             detail=f'Task_not_found')


if __name__ == "__main__":
    uvicorn.run("task_03:app", host="127.0.0.1", port=8000, reload=True)