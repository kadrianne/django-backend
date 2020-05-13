from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    delivery = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)