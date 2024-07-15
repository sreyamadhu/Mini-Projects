from django.db import models

class CensorInfo(models.Model):
    rating=models.CharField(max_length=300,null=True)
    certified_by=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.certified_by

class Director(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name

# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=25)
    year=models.IntegerField(null=True)
    description=models.TextField()
    poster=models.ImageField(upload_to='images/', null=True, blank=True)
    censor_details=models.OneToOneField(CensorInfo, on_delete=models.SET_NULL, related_name='movie', null=True)
    directed_by=models.ForeignKey(Director,null=True,on_delete=models.CASCADE,related_name='directed_movies')
    acters=models.ManyToManyField(Actor,related_name='acted_movies')


    def __str__(self):
        return self.title



