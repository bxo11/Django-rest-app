from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Meals
from . serializers import mealsSerializer

# Create your views here.

class mealsView(APIView):
    def get(self, request):
        meals1 = Meals.objects.all()
        serializer = mealsSerializer(meals1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

def index(request):
    return HttpResponse("App is working")
