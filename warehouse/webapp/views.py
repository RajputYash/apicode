from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets
from warehouse.webapp.send_email import emailcheck
from .serializers import LoginSerializer, UserSerializer, TokenSerializer, CustomerSerializer
from warehouse.webapp.models import User,Customer,OTP


class LoginApi(APIView):
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            userinfo = User.objects.get(id=token.user_id)
            serializer_class = UserSerializer(userinfo, many=False)
            return Response({"token": token.key, "user": serializer_class.data})
        except KeyError as er:
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
                if ( str(cust.Email) == str(Email) and str(cust.Contact_no) == str(Contact_no) ):
                    otp = emailcheck(cust.id, cust.Username, cust.Email)
                    return Response({"result": 1, "Success": "Otp sent successfull . Kindly check your email ","otp": otp})
                else:
                    return Response({"result": 0, "Error": "Data is not valid"})
            else:
                return Response({"result": 0, "Error": "Username doesn't match in database"})

        except Exception as err:
            print("exception error", err)




class ResetPasswordApi(APIView):
    def post(self,request):
        data = request.data
        otp = str(data.get("otp",""))
        new_password = data.get("newpassword","")
        try:
            if OTP.objects.filter(otp=otp):
                ide = OTP.objects.get(otp=otp).user_id
                user = User.objects.get(id=ide)
                user.set_password(new_password)
                user.save()
                return Response({"result": 1, "success": "password reset successfully"})
            else:
                return Response({"result": 0, "error": "OTP doesn't match"})

        except Exception as err:
            print("Exception is :", err)



class CustomerViewSet(viewsets.ModelViewSet):
    u=User.objects.filter(username="Hani")
    queryset = Customer.objects.filter(Created_by=u)
    serializer_class = CustomerSerializer















