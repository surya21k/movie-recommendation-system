from src.hybrid import (
    hybrid_recommend
)

result = hybrid_recommend(
    "Toy Story (1995)"
)

for movie in result:
    print(movie)