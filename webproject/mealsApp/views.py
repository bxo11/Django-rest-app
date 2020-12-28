from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meals
from .models import Ingredients
from .serializers import MealsSerializer, MealsDetailSerializer
from .serializers import IngredientsSerializer, IngredientsDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.




class MealsListView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

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


class MealsDetailView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Meals.objects.get(id=id)
        except Meals.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = MealsDetailSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = MealsDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IngredientsListView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    
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


class IngredientsDetailView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Ingredients.objects.get(id=id)
        except Meals.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = IngredientsDetailSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = IngredientsDetailSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)