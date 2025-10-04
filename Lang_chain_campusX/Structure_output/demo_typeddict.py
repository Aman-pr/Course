from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

new_movie: Movie = {'Title': "Inception",'year':2020}
print(new_movie)