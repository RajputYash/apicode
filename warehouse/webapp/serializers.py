from django.core import exceptions
from rest_framework import serializers
from .models import User, Customer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self, data):
        username = data.get("username","")
        password = data.get("password","")

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                data["user"] = user
            else:
                print('user authentication fails')
                msg='invalid credentials. try again'
                return exceptions.ValidationError(msg)
        else:
            print('username & password doesnt exist')
            msg="invalid data"
            return exceptions.ValidationError(msg)

        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password","email","UserType"]





class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["key","user"]


