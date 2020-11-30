from django.urls import path, include
from .views import MealsView, IngredientsView, index
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', index),
    path('api/meals/', MealsView.as_view()),
    path('api/ingredients/', IngredientsView.as_view()),
]
