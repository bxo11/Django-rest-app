from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator


class Meals(models.Model):
    name = models.CharField(max_length=100, default="", validators=[MinLengthValidator(2, "2 or more characters")])
    category = models.CharField(max_length=100, default="lunch", validators=[MinLengthValidator(2, "2 or more characters")])
    instruction = models.CharField(max_length=500, default="nothing", validators=[MinLengthValidator(2, "2 or more characters")])
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=100, default="", validators=[MinLengthValidator(2, "2 or more characters")])
    amount = models.FloatField(default=0.)
    amountUnit = models.CharField(max_length=100, default="", validators=[MinLengthValidator(2, "2 or more characters")])
    meal = models.ManyToManyField(Meals, related_name="ingredients_list")

    def __str__(self):
        return self.name
