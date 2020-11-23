from rest_framework import serializers
from .models import Meals

class mealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields='__all__'