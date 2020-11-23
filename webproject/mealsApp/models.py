from django.db import models


class Meals(models.Model):
    meals_ID = models.IntegerField()
    name = models.CharField(max_length=20)
    destription = models.CharField(max_length=200)

    def __str__(self):
        return self.name