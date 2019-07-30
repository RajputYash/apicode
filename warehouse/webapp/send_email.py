import random

from django.core.mail import EmailMessage,send_mail
from django.utils import timezone
from rest_framework.response import Response

from warehouse import settings
from warehouse.webapp.models import OTP


def line(size):
    li = range(10)
    a=[]
    for i in range(size):
        a.append(random.choice(li))
    #z = str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]) + str(a[4])
    z=''.join(map(str,a))
    return z


passwrd_reset = """Dear Customer                                                {}
Use {} as One Time Password (OTP) to change password 
of your Smart Meter Dashboard.
Please reach us at sem@aviconn.in for any query."""

def emailcheck(id,username,email):
    from_mail = settings.EMAIL_HOST_USER
    email_to_send = email
    print("##############")
    print(email_to_send)
    otp = line(5)
    print(otp)
    OTP.objects.create(otp=otp , user_id=id)
    date = timezone.now().strftime("%b %d,%Y")
    print(date)
    # msg_mail = get_template('low_balance.html').render({'date': date, 'balance': current_balance, 'res': res})
    email=passwrd_reset.format(date,otp)
    print("last step remaining")
    subject_mail = "Password Change Request for Your Smart Meter Account"
    print(subject_mail)
    msg = EmailMessage(subject_mail, email, from_mail, [email_to_send])
    msg.send()
    return Response({"msg": " otp send to your email"})