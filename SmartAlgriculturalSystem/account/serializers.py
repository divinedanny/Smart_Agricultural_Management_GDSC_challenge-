from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id','username','email',)
        
class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password','confirm_password','profile_picture','gender','date_of_birth')
        
        
    def validate(self, attrs):
        if attrs['password']!= attrs['confirm_password']:
            raise serializers.ValidationError('Passwords do not match')
        return super().validate(attrs)
    
    def validate_password(self,attrs):
        validate_password(attrs)
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            profile_picture=validated_data['profile_picture'],
        )
        return user