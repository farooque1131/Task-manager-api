from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','password','email', 'password2')
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}},
            'email': {'required': True},    
        }

    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})

        validate_password(data['password'], user=User)
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2') 

        user = User.objects.create_user(username=validated_data["username"], email= validated_data["email"],password=validated_data["password"])

        return user
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_superuser"]

class UserRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["is_staff"]