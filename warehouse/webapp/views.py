from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate,logout
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import LoginSerializer, UserSerializer, TokenSerializer, CustomerSerializer
from django.http import HttpResponse

from warehouse.webapp.models import User,Customer


class LoginApi(APIView):
    print("loginapi")
    def post(self,request):
        print("post method")
        serializer=LoginSerializer(data=request.data)
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

        # print("user variables get key")
        # token,created=Token.objects.get_or_create(user=user)
        # userinfo=User.objects.get(id=token.user_id)
        # serializer_class=UserSerializer(userinfo,many=False)
        # return Response({"token" : token.key, "user": serializer_class.data})
        # else:
        #     print('login cannot be possible')
        #     return Response({'error': "errom while login"})


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer




class CustomerViewSet(viewsets.ModelViewSet):
    u=User.objects.filter(username="Hani")
    queryset = Customer.objects.filter(Created_by=u)
    # for i in queryset:
    #     print(i.Name)
    serializer_class = CustomerSerializer









    # def post(self,request):
    #     logout(request)
    #     if logout:
    #         request.user.token.delete()
    #         return Response({"detail": "Successfully logged out."},
    #                     status=status.HTTP_200_OK)
    # def post(self, request):
    #     try:
    #         request.user.token.delete()
    #     except (AttributeError):
    #
        #         pass
    #
    #     logout(request)
    #
    #     return Response({"detail": "Successfully logged out."},
    #                     status=status.HTTP_200_OK)















