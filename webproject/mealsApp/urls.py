from django.urls import path, include
from .views import MealsListView, IngredientsListView, MealsDetailView, IngredientsDetailView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('meals/', MealsListView.as_view()),
    path('meals/<int:id>', MealsDetailView.as_view()),
    path('ingredients/', IngredientsListView.as_view()),
    path('ingredients/<int:id>', IngredientsDetailView.as_view()),
    path('accounts/', include('accounts.urls')),
]
