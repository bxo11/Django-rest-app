from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.admin import ModelAdmin
from django.core.validators import MinLengthValidator, MaxLengthValidator

try:
    from allauth.utils import email_address_exists
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")







class UsersSerializer(serializers.Serializer):
    validators = [MinLengthValidator(2, "2 or more characters"), MaxLengthValidator(100, "Less than 100 characters")]
    
    username = serializers.CharField(required=True, max_length=100, validators=validators)
    email = serializers.EmailField(required=True, max_length=100, validators=validators)
    password1 = serializers.CharField(write_only=True, max_length=100, style={"input_type": "password"}, validators=validators)
    password2 = serializers.CharField(write_only=True, max_length=100, style={"input_type": "password"}, validators=validators)
    
    
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError( "A user is already registered with this e-mail address.")
            
        return email
    
    
    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    
    
    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Both password fields didn't match.")
        return data
    
    
    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
        }
    
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        
        return user






class AdminsSerializer(serializers.Serializer):
    validators = [MinLengthValidator(2, "2 or more characters"), MaxLengthValidator(100, "Less than 100 characters")]
    
    username  = serializers.CharField(required=True, max_length=100, validators=validators)
    email     = serializers.EmailField(required=True, max_length=100, validators=validators)
    password1 = serializers.CharField(write_only=True, max_length=100, style={"input_type": "password"}, validators=validators)
    password2 = serializers.CharField(write_only=True, max_length=100, style={"input_type": "password"}, validators=validators)
    is_superuser = serializers.BooleanField(default=True)
    
    
    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if email and email_address_exists(email):
            raise serializers.ValidationError( "A user is already registered with this e-mail address.")
            
        return email
    
    
    def validate_password1(self, password):
        return get_adapter().clean_password(password)
    
    
    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Both password fields didn't match.")
        return data
    
    
    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "is_superuser": self.validated_data.get("is_superuser", ""),
        }
    
    
    def save(self, request):
        adapter = get_adapter()
        admin = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        admin.is_staff = True
        admin.is_admin = True
        admin.is_superuser = True
        adapter.save_user(request, admin, self)
        setup_user_email(request, admin, [])
        
        return admin