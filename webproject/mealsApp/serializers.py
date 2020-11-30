from rest_framework import serializers
from .models import Meals
from .models import Ingredients


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'
