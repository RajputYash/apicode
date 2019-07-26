import random
import string

from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework.views import APIView,View
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate,logout
from rest_framework.response import Response
from rest_framework import status, viewsets

from warehouse import settings
from .serializers import LoginSerializer, UserSerializer, TokenSerializer, CustomerSerializer
from django.http import HttpResponse
from warehouse.webapp.models import User,Customer,OTP
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from rest_framework.decorators import api_view


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





class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer




class ForgetPassword(APIView):
    print("forget password!!!!!!!!!!!!!!!!!!!!!!!!")
    def post(self,request):
        data = request.data
        print(data)
        Username = data.get("Username",)
        print(Username)
        Email = data.get("Email",)
        print(Email)
        Contact_no = data.get("Contact_no",)
        print(Contact_no)
        try:
            print("try block started")
            if (Username and Email and Contact_no):
                customer = Customer.objects.filter(Username=Username, Email=Email, Contact_no=Contact_no)
                if customer:
                    print("hellllloo")
                    cust = Customer.objects.get(Username = Username)
                    print(cust.id)
                    cust_id=cust.id
                    cust_username=cust.Username
                    cust_email=cust.Email
                    print(cust_email)
                    print("##########")
                    print(cust.Email)
                    print("@@@@@@@@@@@@@@@")
                    if cust.Username != Username and cust.Email != Email and cust.Contact_no != Contact_no:
                        print("Credentials mismatch")
                        return Response({"error": "credentials mismatch"})
                    else:
                        print("success")
                        #self.emailcheck(cust_id, cust_username,cust_email)
                        print("email check completed")
                        return Response({"success": "Success!! Data is valid"})
                else:
                    print("username is not in the database")
                    return Response({"error":"username is not in database"})
            else:
                print("please enter all the credentials")
                # cust = Customer.objects.get(Username=Username)
                # emailcheck(id=cust.id, Username=cust.Username)
                return Response({"error":"please enter all the credentials"})
        except Exception as err:
            print("exception error", err)
    #
    # def emailcheck(self,id,username,email,):
    #     from_mail=settings.EMAIL_HOST_USER
    #     print("hiiiiiiiiiiiiiiiiiiiii")
    #     print(id)
    #     print(username)
    #     print(email)
    #     print("%%%%%%%%%%%%%%%")
    #     print(from_mail)
    #     print("@@@@@@@@@2")
    #     email_to_send=email
    #     # email_to_send=Customer.objects.get(id=id).Email
    #     print("##############")
    #     print(email_to_send)
    #     otp=line(5)
    #     print(otp)
    #     OTP.objects.create(otp=otp , user_id=id)
    #     date = timezone.now().strftime("%b %d,%Y")
    #     print(date)
    #     email={
    #         "date": date,
    #         "otp" : otp
    #     }
    #     print("last step remaining")
    #     subject_mail = "Password Change Request for Your Smart Meter Account"
    #     print(subject_mail)
    #     msg = EmailMessage(subject_mail, email, from_mail, [email_to_send])
    #     msg.send()


def line(size, char=string.ascii_lowercase + string.digits):
    return ''.join((random.choice(char) for _ in range(size)))



class ResetPasswordApi(APIView):
    def post(self,request):
        data=request.data
        otp=data.get("otp","")
        new_password=data.get("new_password","")
        try:
            if OTP.objects.filter(otp=otp):
                ide = OTP.objects.get(otp=otp).user_id
                c=Customer.objects.get(id=ide)
                c.set_Password(new_password)
                c.save()
                return Response({"success_reset": "password reset successfully"})



        except Exception as err:
            print(err)








class CustomerViewSet(viewsets.ModelViewSet):
    u=User.objects.filter(username="Hani")
    queryset = Customer.objects.filter(Created_by=u)
    # for i in queryset:
    #     print(i.Name)
    serializer_class = CustomerSerializer















