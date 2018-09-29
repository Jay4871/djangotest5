from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField(default=0)


class City(models.Model):
    name=models.CharField(max_length=16,null=True)

    def __str__(self):
        return self.name