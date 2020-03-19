from django.db import models

# Create your models here.
class Director(models.Model):
    name=models.CharField(max_length=100,unique=True)
    #date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=6)
    #age=models.IntegerField(null=True)
    #image=models.URLField(null=True)
    no_of_facebook_likes=models.CharField(max_length=15)
    #description=models.CharField(max_length=250,null=True)

class Actor(models.Model):
    actor_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    #date_of_birth=models.DateField(null=True)
    gender=models.CharField(max_length=6)
    #age=models.IntegerField(null=True)
    #image=models.URLField(null=True)
    fb_likes=models.CharField(max_length=15)
    #description=models.CharField(max_length=250,null=True)


class Movie(models.Model):
    movie_id=models.CharField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    budget=models.CharField(max_length=15)
    box_office_collection_in_crores=models.IntegerField()
    year_of_release=models.CharField(max_length=4)
    likes_on_fb=models.IntegerField()
    average_rating=models.FloatField(default=0)
    genre=models.CharField(max_length=200)
    #image=models.URLField(null=True)
    language=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    no_of_users_voted=models.CharField(max_length=15)
    actors=models.ManyToManyField(Actor,through='Cast')
    director_name=models.ForeignKey(Director,on_delete=models.CASCADE)
    #description=models.CharField(max_length=250,null=True)

class Cast(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    actor=models.ForeignKey(Actor,on_delete=models.CASCADE)
    role=models.CharField(max_length=50)
    is_debut_movie=models.BooleanField(default=False)

# class Rating(models.Model):
#     movie=models.OneToOneField(Movie,on_delete=models.CASCADE)
#     rating_one_count=models.IntegerField(default=0)
#     rating_two_count=models.IntegerField(default=0)
#     rating_three_count=models.IntegerField(default=0)
#     rating_four_count=models.IntegerField(default=0)
#     rating_five_count=models.IntegerField(default=0)
    
    

