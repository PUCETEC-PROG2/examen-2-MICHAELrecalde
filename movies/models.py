from django.db import models


# Create your models here.
class Movie(models.Model):

    id=models.IntegerField(primary_key=True)    
    name=models.CharField(max_length=30,null=False)
    gender=models.CharField(max_length=30,null=False)
    director=models.CharField(max_length=30,null=False)
    year=models.CharField(max_length=30,null=False)
    synopsis=models.TextField(max_length=30,null=False)
    

def __str__(self):
    return self.name

