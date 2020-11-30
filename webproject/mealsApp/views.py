from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meals
from .models import Ingredients
from .serializers import MealsSerializer
from .serializers import IngredientsSerializer
from rest_framework.decorators import api_view

# Create your views here.

class MealsView(APIView):

    def get(self, request):
        meals1 = Meals.objects.all()
        serializer = MealsSerializer(meals1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientsView(APIView):
    def get(self, request):
        ingredients1 = Ingredients.objects.all()
        serializer = IngredientsSerializer(ingredients1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("App is working")
