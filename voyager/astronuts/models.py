from django.db import models

# Create your models here.

class Astronut(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    age = models.IntegerField()
    joindate = models.DateTimeField('date joined')
    
    def __str__(self):
        return self.name
