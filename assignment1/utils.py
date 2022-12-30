from assignment1.models import Actor, Cast, Rating, Movie, Director
from django.db.models import *

DIRECTOR_LIST = [
    "Sam", "Stan Lee", "James", "Robert", "Sammual"
]
ACTOR_LIST = [
    {
        "actor_id": "actor_1",
        "name": "Robert Downy Junior"
    },
    {
        "actor_id": "actor_2",
        "name": "Tom Holland"
    },
    {
        "actor_id": "actor_3",
        "name": "Mark"

    },
    {
        "actor_id": "actor_4",
        "name": "Jhonny Deph"
    }
]
MOVIE_LIST = [
    {
        "movie_id": "movie_1",
        "name": "Iron Man",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "500",
        "release_date": "2009-3-3",
        "director_name": "Sam"
    },
    {
        "movie_id": "movie_2",
        "name": "Spider-man",
        "actors": [
            {
                "actor_id": "actor_2",
                "role": "hero",
                "is_debut_movie": True
            }
        ],
        "box_office_collection_in_crores": "300",
        "release_date": "2019-5-3",
        "director_name": "Stan Lee"
    },
    {
        "movie_id": "movie_3",
        "name": "Hulk",
        "actors": [
            {
                "actor_id": "actor_3",
                "role": "hero",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "500",
        "release_date": "2003-3-3",
        "director_name": "James"
    },
    {
        "movie_id": "movie_4",
        "name": "Pirates of the Carraibean",
        "actors": [
            {
                "actor_id": "actor_4",
                "role": "Pirate",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "800",
        "release_date": "2009-3-3",
        "director_name": "Robert"
    },
    {
        "movie_id": "movie_5",
        "name": "Iron Man2",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            },
            {
                "actor_id": "actor_2",
                "role": "Villan",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "500",
        "release_date": "2009-3-3",
        "director_name": "Sammual"
    },
    {
        "movie_id": "movie_6",
        "name": "Iron Man4",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            },
            {
                "actor_id": "actor_3",
                "role": "Villan",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "500",
        "release_date": "2009-3-3",
        "director_name": "Sam"
    }
]

MOVIE_RATING_LIST = [
    {
        "movie_id": "movie_1",
        "rating_one_count": 10,
        "rating_two_count": 12,
        "rating_three_count": 4,
        "rating_four_count": 4,
        "rating_five_count": 4
    },

    {
        "movie_id": "movie_2",
        "rating_one_count": 15,
        "rating_two_count": 4,
        "rating_three_count": 10,
        "rating_four_count": 8,
        "rating_five_count": 4
    },

    {
        "movie_id": "movie_3",
        "rating_one_count": 100,
        "rating_two_count": 120,
        "rating_three_count": 40,
        "rating_four_count": 40,
        "rating_five_count": 40
    },

    {
        "movie_id": "movie_4",
        "rating_one_count": 104,
        "rating_two_count": 124,
        "rating_three_count": 44,
        "rating_four_count": 44,
        "rating_five_count": 44
    }

]


def create_actors(actor_list):
    """
    :param actor_list: [
        {
            "actor_id": "string",
            "role": "string",
            "is_debut_movie": "boolean"
        }
    ]
    :return:
    """
    actors = [
        Actor(name=actor['name'], actor_id=actor['actor_id'])
        for actor in actor_list
    ]
    Actor.objects.bulk_create(actors)


def create_directors(director_list):
    """
    :param director_list: [string]
    :return:
    """
    directors = [
        Director(name=director)
        for director in director_list
    ]
    Director.objects.bulk_create(directors)


def create_movies(movie_list):
    """
    :param movie_list: [
        {
            "movie_id": "string",
            "name": "string",
            "actors": [
                {
                    "actor_id": "string",
                    "role": "string",
                    "is_debut_movie": "boolean"
                }
            ],
            "box_office_collection_in_crores": int,
            "release_date": "string",
            "director_name": "string"
        }
    ]
    :return:
    """

    director_list = list(Director.objects.values_list('name', 'pk'))
    director_name_wise_id = {name: pk for name, pk in director_list}
    movies = [
        Movie(
            name=movie['name'],
            movie_id=movie['movie_id'],
            release_date=movie['release_date'],
            box_office_collection_in_crores=movie[
                'box_office_collection_in_crores'],
            director_id=director_name_wise_id[movie["director_name"]]
        )
        for movie in movie_list
    ]
    Movie.objects.bulk_create(movies)


def create_cast(movies, actor_id_wise_pk, movie_id_wise_pk):
    # change this as discussed
    """
    :param movies:
    :param actor_id_wise_pk: {}
    :param movie_id_wise_pk: {}
    :return:
    """
    cast = []
    for movie in movies:
        movie_id = movie['movie_id']
        for actor in movie['actors']:
            actor_id = actor_id_wise_pk[actor['actor_id']]
            movie_id = movie_id_wise_pk[movie_id]
            cast_object = Cast(actor_id=actor_id, movie_id=movie_id,
                               role=actor['role'],
                               is_debute_movie=actor['is_debut_movie'])
            cast.append(cast_object)
    Cast.objects.bulk_create(cast)


def create_ratings(rating_list, movie_id_pk_dict):
    """

    :param rating_list: []
    :param movie_id_pk_dict: {}
    :return:
    """
    ratings = [
        Rating(movie_id=movie_id_pk_dict[rating['movie_id']],
               rating_one_count=rating['rating_one_count'],
               rating_two_count=rating['rating_two_count'],
               rating_three_count=rating['rating_three_count'],
               rating_four_count=rating['rating_four_count'],
               rating_five_count=rating['rating_five_count'])
        for rating in rating_list
    ]
    Rating.objects.bulk_create(ratings)


def get_actor_id_wise_id():
    """
    :return: {actor_id_wise_id}
    """
    actors_dict = list(Actor.objects.values_list('actor_id', 'pk'))
    actor_id_wise_id = {
        actor: pk
        for actor, pk in actors_dict
    }
    return actor_id_wise_id


def get_movie_id_wise_id():
    """
    :return: {movie_id_wise_id}
    """
    movie_dict = list(Movie.objects.values_list('movie_id', 'pk'))
    movie_id_wise_id = {
        movie: pk
        for movie, pk in movie_dict
    }
    return movie_id_wise_id


def import_data_to_db(actor_list, movie_rating_list, director_list,
                      movie_list):
    """

    :param actor_list: [
         {
            "actor_id": "string" ,
            "name": "string"
         }
    ]
    :param movie_rating_list: [
        {
        "movie_id": "string",
        "rating_one_count": int,
        "rating_two_count": int,
        "rating_three_count": int,
        "rating_four_count": int,
        "rating_five_count": int
       }
    ]
    :param director_list: [
        name : "string"
    ]
    :param movie_list: [
        {
            "movie_id": "string",
            "name": "string",
            "actors": [
                {
                    "actor_id": "string",
                    "role": "string",
                    "is_debut_movie": "boolean"
                }
            ],
            "box_office_collection_in_crores": int,
            "release_date": "string",
            "director_name": "string"
        }
    ]
    :return:
    """
    create_actors(actor_list)
    create_directors(director_list)
    actor_id_wise_id = get_actor_id_wise_id()
    movie_id_wise_id = get_movie_id_wise_id()
    create_movies(movie_list)
    create_cast(movie_list, actor_id_wise_id, movie_id_wise_id)
    create_ratings(movie_rating_list, movie_id_wise_id)


def get_no_of_distinct_movies_actor_acted(actor_id):
    # this has to be changed
    """
    :param actor_id: int
    :return: int
    """
    no_of_movies = Cast.objects.filter(
        actor__actor_id=actor_id).aggregate(
        count=Count('movie', distinct=True))
    return no_of_movies['count']


def get_movies_directed_by_director(director_obj):
    """
    :param director_obj: <Director: Director 1>
    :return: int
    """
    no_of_movies = Movie.objects.filter(director=director_obj).aggregate(
        count=Count('movie_id'))
    return no_of_movies['count']


def get_average_rating_of_movie(movie_obj):
    # this has to be changed
    """
    :param movie_obj: <Movie: movie_1>
    :return: int
    """
    y = Rating.objects.filter(movie=movie_obj).aggregate(stl=Sum(
        F('rating_one_count') + F('rating_two_count') + F(
            'rating_three_count') + F('rating_four_count') + F(
            'rating_five_count')))


def delete_movie_rating(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return: none
    """
    Rating.objects.filter(movie=movie_obj).delete()


def get_all_actor_objects_acted_in_given_movies(movie_objs):
    """
    :param movie_objs: <Movie: movie_1>
    :return: [list of actors]
    """
    actors = []
    for movie in movie_objs:
        actors += list(movie.actors.all())

    actor_set = {actor for actor in actors}
    return list(actor_set)


def update_director_for_given_movie(movie_obj, director_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :param director_obj: <Director: Director 1>
    :return: none
    """
    movie_obj.director = director_obj
    movie_obj.save()


def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    """
    :return: [list of movie object]
    """
    movies = list(Movie.objects.filter(actors__name__contains=
                                       'john').distinct())
    return movies


def remove_all_actors_from_given_movie(movie_obj):
    """
    :param movie_obj: <Movie: movie_1>
    :return: none
    """
    Cast.objects.filter(movie=movie_obj).delete()


def get_all_rating_objects_for_given_movies(movie_objs):
    """
    :param movie_objs: <Movie: movie_1>
    :return:[<Rating: rating_1>]
    """
    ratings = list(Rating.objects.filter(movie__in=movie_objs))
    return ratings
