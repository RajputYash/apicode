import random
import string

from django.core import serializers
# from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from kombu.utils import json
from rest_framework.views import APIView,View
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate,logout
from rest_framework.response import Response
from rest_framework import status, viewsets

from warehouse import settings
from warehouse.webapp.send_email import emailcheck
from .serializers import LoginSerializer, UserSerializer, TokenSerializer, CustomerSerializer
from django.http import HttpResponse, request
from warehouse.webapp.models import User,Customer,OTP
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, RetrieveAPIView


class LoginApi(APIView):
    print("loginapi")
    def post(self,request):
        print("post method")
        serializer=LoginSerializer(data=request.data)
        print("serializer data type: ",type(serializer))
        print(serializer)
        print("serializer")
        serializer.is_valid(raise_exception=True)
        print('serialize is valid')
        print(serializer.is_valid(raise_exception=True))
        try:
            user=serializer.validated_data["user"]
            print(user)
            print("user variables get key")
            token, created = Token.objects.get_or_create(user=user)
            userinfo = User.objects.get(id=token.user_id)
            serializer_class = UserSerializer(userinfo, many=False)
            return Response({"token": token.key, "user": serializer_class.data})
        except KeyError as er:
            print(er)
            print('login cannot be possible')
            return Response({'error': "Please enter valid credentaials "})





class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer



class ForgetPassword(APIView):
    def post(self,request):
        data = request.data
        Username = data.get("Username",)
        Email = data.get("email",)
        Contact_no = data.get("mobile",)

        try:
            if  (Customer.objects.filter(Username = Username)):
                cust = Customer.objects.get(Username = Username)
                if ( str(cust.Email) == Email and str(cust.Contact_no) == str(Contact_no) ):
                    emailcheck(cust.id, cust.Username, cust.Email)
                    return Response({"result": 1, "Success": "Otp sent successfull . Kindly check your email "},)
                else:
                    return Response({"result": 0, "Error": "Data is not valid"})
            else:
                return Response({"result": 0, "Error": "Username doesn't match in database"})

        except Exception as err:
            print("exception error", err)




class ResetPasswordApi(APIView):
    def post(self,request):
        data = request.data
        print("data is :", data)
        otp = str(data.get("otp",""))
        print("otp is :", otp)
        new_password = data.get("new_password","")
        print("new password is :", new_password)
        try:
            if OTP.objects.filter(otp=otp):
                print("inside the if condition")
                ide = OTP.objects.get(otp=otp).user_id
                print("ide is :", ide)
                user = User.objects.get(id=ide)
                print("user id/info is", user)
                user.set_Password(new_password)
                print("password get set successfully")
                user.save()
                print("finally password updated in the User table")
                return Response({"result": 1, "success_reset": "password reset successfully"})
            else:
                print("OTP doesn't match")
                return Response({"result": 0, "error": "OTP doesn't match"})

        except Exception as err:
            print("Exception is :", err)








class CustomerViewSet(viewsets.ModelViewSet):
    u=User.objects.filter(username="Hani")
    queryset = Customer.objects.filter(Created_by=u)
    # for i in queryset:
    #     print(i.Name)
    serializer_class = CustomerSerializer















