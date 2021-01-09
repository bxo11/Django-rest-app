from .serializers import UsersSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated





class UserRegisterView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]
    
    def get(self, request, format=None):
        snippet = User.objects.all()
        serializer = UsersSerializer(snippet, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
