import random
from warehouse import settings
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.utils import timezone
from warehouse.webapp.models import OTP, User


def line(size, li=range(10)):
    return ''.join(map(str, ([random.choice(li) for _ in range(size)])))


passwrd_reset = """

"""


def emailcheck(id,username,email):
    from_mail = settings.EMAIL_HOST_USER
    email_to_send = email
    userId = User.objects.get(username=username).id
    otp = line(5)
    print(otp)
    OTP.objects.create(otp=otp , user_id=userId)
    date = timezone.now().strftime("%b %d,%Y")
    email = passwrd_reset

    html_message = """
    <html>
    <head>
    
    Dear Customer  &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;  {}
    <br><br>
    Thank you for using Aviconn Smart Energy Management (SEM).<br><br>
    One Time Password (OTP) for the process to Reset Password is <b>{}</b>.     
    Click the given link to set New Password :  <a href="https://sem.aviconn.in/" target="_blank">Click Here to Reset Password</a>
    <br><br>
    Do not share your password with anyone.
    <br><br>
    Looking forward to more opportunities to be of service to you.
    <br>
    <br>
    Sincerely,
    <br><br>
    Aviconn Solution Pvt Ltd
    </head>
    </html>

    """.format(date, otp)

    print("last step remaining")
    subject_mail = "Password Change Request for Your Smart Meter Account"
    print(subject_mail)
    msg = EmailMultiAlternatives(subject_mail, email, from_mail, [email_to_send])
    msg.attach_alternative(html_message, "text/html")
    msg.send()
    print("send mail successfull")
    return otp


# msg_mail = get_template('low_balance.html').render({'date': date, 'balance': current_balance, 'res': res})
