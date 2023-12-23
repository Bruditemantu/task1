from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    author=models.CharField(max_length=50)
    is_avilable=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name



    
