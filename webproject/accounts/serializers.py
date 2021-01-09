from rest_framework import serializers
from django.contrib.auth.models import User

try:
    from allauth.utils import email_address_exists
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")





class CustomUserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email')



class UsersSerializer(serializers.Serializer):
    
    username = serializers.CharField(required=True, max_length=100)
    email = serializers.EmailField(required=True, max_length=100)
    password1 = serializers.CharField(write_only=True, max_length=100, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, max_length=100, style={"input_type": "password"})
    
    
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

