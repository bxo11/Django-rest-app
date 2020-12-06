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


class IngredientsDetailSerializer(serializers.ModelSerializer):
    # meal = serializers.PrimaryKeyRelatedField(queryset=Meals.objects.all(), many=True)

    meal = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ingredients
        fields = '__all__'


class SimpleIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        exclude = ['meal']


class MealsDetailSerializer(serializers.ModelSerializer):
    ingredients_list = SimpleIngredientsSerializer(many=True, read_only=True)

    class Meta:
        model = Meals
        fields = ['name', 'category', 'instruction', 'dateAdded', 'ingredients_list']
