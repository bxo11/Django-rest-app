from django.contrib import admin
from .models import Meals
from .models import Ingredients

admin.site.register(Meals)
admin.site.register(Ingredients)
