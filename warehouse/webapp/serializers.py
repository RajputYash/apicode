from django.core import exceptions
from rest_framework import serializers
from rest_framework.response import Response
from .models import User, Customer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    print("login serializer class")

    def validate(self, data):
        print('validate method')
        username = data.get("username","")
        print("username value", username)
        password = data.get("password","")
        print("password value:",password)

        if username and password:
            print("checking password & username")
            user = authenticate(username=username, password=password)
            print(user)
            print("user getting authenticated")

            if user:
                print(user)
                print("user got authenticated")
                print(data)
                data["user"] = user
                print(data)
                print(data["user"])
                print('data is going to return')
                print("something is returning")

            else:
                print('user authentication fails')
                msg='invalid credentials. try again'
                # return exceptions.ValidationError(msg)
        else:
            print('username & password doesnt exist')
            msg="invalid data"
            # return exceptions.ValidationError(msg)
        #       return Response({"login_error": "invalid credentials please check"})
        # else:
        #     return Response({"error" : "please provide username and password"})
        # print("something is returning")
        # return data
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","email","UserType"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        #fields=['Name', 'UserName', 'Password', 'Created_by', 'Total_Property', 'Email', 'Contact_No', 'Address', 'Contract_date' ]
        fields = '__all__'



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Token
        fields=["key","user"]