from src.content_based import (
    get_recommendations
)

from src.item_cf import (
    get_similar_movies
)

def hybrid_recommend(
    movie_title,
    n=10
):
    
    content_recs = list(
        get_recommendations(
            movie_title,
            n=5
        )
    )

    item_recs = list(
        get_similar_movies(
            movie_title,
            n=5
        )["title"]
    )

    combined = list(
        dict.fromkeys(
            content_recs +
            item_recs
        )
    )

    return combined[:n]

from src.hybrid import (
    hybrid_recommend
)

result = hybrid_recommend(
    "Toy Story (1995)"
)

for movie in result:
    print(movie)