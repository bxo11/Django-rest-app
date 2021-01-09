from django.urls import path, include
from .views import UserRegisterView, AdminRegisterView
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path("", include("rest_auth.urls")),
    path("register/", UserRegisterView.as_view()),
    #path('register/<int:pk>/', UserRegisterView.as_view()),
    path("admin/", AdminRegisterView.as_view()),
]
