from django.db import models
from django.utils.timezone import now


class Meals(models.Model):
    name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=100, default="lunch")
    instruction = models.CharField(max_length=500, default="nothing")
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=100, default="")
    amount = models.FloatField(default=0.)
    amountUnit = models.CharField(max_length=100, default="")
    meal = models.ManyToManyField(Meals, related_name="ingredients_list")

    def __str__(self):
        return self.name
