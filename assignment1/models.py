from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Actor(models.Model):
    name = models.CharField(max_length=100, null=True)
    actor_id = models.CharField(max_length=100, unique=True)


class Movie(models.Model):
    name = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100, unique=True)
    actors = models.ManyToManyField(Actor, through='Cast', null=True)
    release_date = models.DateField()
    box_office_collection_in_crores = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class Cast(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=501, null=True)
    is_debute_movie = models.BooleanField()


class Rating(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    rating_one_count = models.IntegerField(default=0)
    rating_two_count = models.IntegerField(default=0)
    rating_three_count = models.IntegerField(default=0)
    rating_four_count = models.IntegerField(default=0)
    rating_five_count = models.IntegerField(default=0)
