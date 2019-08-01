from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.db.models.signals import post_save,pre_save,post_delete
from django.conf import settings
from django.utils import timezone


class User(AbstractUser):
    user_type = ((1, 'Admin_user'),(2,'Customer_Admin'),(3,'Site_Manager'))
    UserType = models.PositiveIntegerField(default=1,choices=user_type)

def Create_Group(sender,instance,*args,**kwargs):
    if instance._state.adding is True and len(Group.objects.filter(name=instance.get_UserType_display())):
        print("Group has been created successfully ")
        Group.objects.create(name=instance.get_UserType_display())


def Add_group_to_user(sender,instance,*args,**kwargs):
    try:
        if(instance.UserType==1):
            User.objects.filter(username=instance.username).update(is_staff=True)
        g=Group.objects.filter(name=instance.get_UserType_display())
        print(g)
        print("Instance has been added inside the group")
        instance.groups.set(g)
    except:
        pass

post_save.connect(Add_group_to_user,sender=User)
pre_save.connect(Create_Group,sender=User)


class Customer(models.Model):
    Name = models.CharField(max_length=20)
    Username = models.CharField(max_length=20, unique=True, verbose_name=u"Please Enter your Unique Username",
                                help_text=u"Please do not select white spaces", default='test123')
    Password = models.CharField(max_length=15, default="password123")
    Created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                   limit_choices_to={'UserType': 1, 'is_active': True})
    Total_Property = models.PositiveIntegerField(default=0)
    Email = models.EmailField(max_length=40, unique=True)
    Contact_no = models.BigIntegerField(default=True,blank=True,null=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Created_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.Name


def Remove_Customer_To_User(sender, instance, *args, **kwargs):
    User.objects.filter(username=instance.Username).update(is_active=False)



def Add_Customer_To_User(sender, instance, *args, **kwargs):
    if instance._state.adding is True:
        User.objects.create_user(username=instance.Username,email=instance.Email,UserType=2,password=instance.Password)
    else:
        pass


pre_save.connect(Add_Customer_To_User,sender=Customer)
post_delete.connect(Remove_Customer_To_User,sender=Customer)


class DailyMeterReading(models.Model):
    unit_consumption = models.FloatField()
    current_date_time = models.DateTimeField(default=timezone.now)
    total_property_cumulative = models.FloatField()
    block_id = models.IntegerField()

    def __str__(self):
        return self.user_consumption

    def __unicode__(self):
        return self.user_consumption


class Consumption(models.Model):
    user_consumption = models.FloatField()
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user_consumption

    def __unicode__(self):
        return self.user_consumption


class Room(models.Model):
    room_name = models.CharField(max_length=50)
    current_balance = models.FloatField(default=0)
    Associated_floor = models.CharField(max_length=60)
    which_location = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.current_balance
    # def __str__(self):
    #     return self.current_balance

    def __unicode__(self):
        return "{} RoomID in {} floor {}".format(self.room_name, self.which_location, self.Associated_floor)

    def __str__(self):
        return "{} RoomID in {} floor {}".format(self.room_name, self.which_location, self.Associated_floor)


class Resident(models.Model):
    Name = models.CharField(max_length=50)
    which_location = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.Name

    def __str__(self):
        return self.Name

class OTP(models.Model):
    otp = models.CharField(blank=True, null=True, max_length=5)
    user_id = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return "OTP  {} on {}".format(self.otp, self.created)

    def __str__(self):
        return "OTP  {} on {}".format(self.otp, self.created)