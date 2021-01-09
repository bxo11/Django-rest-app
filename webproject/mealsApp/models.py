from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Meals(models.Model):
    validators = [MinLengthValidator(2, "2 or more characters"), MaxLengthValidator(100, "Less than 100 characters")]
    
    name = models.CharField(max_length=100, default="", validators=validators)
    category = models.CharField(max_length=100, default="lunch", validators=validators)
    instruction = models.CharField(max_length=500, default="nothing", 
                    validators=[MinLengthValidator(2, "2 or more characters"), MaxLengthValidator(500, "Less than 100 characters")])
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    validators = [MinLengthValidator(2, "2 or more characters"), MaxLengthValidator(100, "Less than 100 characters")]
    
    name = models.CharField(max_length=100, default="", validators=validators)
    amount = models.FloatField(default=0.)
    amountUnit = models.CharField(max_length=100, default="", validators=validators)
    meal = models.ManyToManyField(Meals, related_name="ingredients_list")

    def __str__(self):
        return self.name
