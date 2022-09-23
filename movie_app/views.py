from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(["GET"])
def director_view(request):
    directors = Director.objects.all()
    data = DirectorListSerializer(directors, many=True).data
    return Response(data=data)


@api_view(["GET"])
def one_director_view(request, id):
    director = {
        'name': Director.objects.get(id=id).name if Director.objects.count() >= id else f"Режиссера под номером {id} не существует!"
    }
    return Response(data=director)


@api_view(["GET"])
def movie_view(request):
    movies =Movie.objects.all()
    data =MovieListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(["GET"])
def one_movie_view(request, id):
    movie = {
        "title": Movie.objects.get(id=id).title if Movie.objects.count() >= id else f"Фильм № {id} еще не добавили в кинотеатр!!",
        "duration": f"{Movie.objects.get(id=id).duration} мин" if Movie.objects.count() >= id else f"У несуществующего фильма №{id} еще нету длительности!!",
        "description": Movie.objects.get(id=id).description if Movie.objects.count() >= id else f"У несуществующего фильма №{id} еще нету описания!!",
        "director": Movie.objects.get(id=id).name if Movie.objects.count() >= id else f"Так как фильма не существует №{id} у него соответственно и режиссера нет!",
    }
    return Response(data=movie)


@api_view(["GET"])
def review_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerialiser(reviews, many=True).data
    return Response(data=data)


@api_view(["GET"])
def one_review_view(request, id):
    review = {
        "text": Review.objects.get(id=id).text if Review.objects.count() >= id else f"Так как не существует фильма №{id} ему нельзя оставить отзыв",
        "movie": Review.objects.get(id=id).movie.title if Review.objects.count() >= id else f"Фильм под номером {id} еще не добавлена в кинотеатр"
    }
    return Response(data=review)
