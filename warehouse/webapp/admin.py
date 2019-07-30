from django.contrib import admin
from .models import User,Customer,Consumption,Resident,Room,OTP

class UserAdmin(admin.ModelAdmin):
    search_fields = ('id','username','UserType')
    list_display = ['id','username','UserType']
    ordering = ('id',)


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'Username')
    list_display = ['id', 'Username', 'Email', 'Contact_no', 'Address' , 'Created_date']
    ordering = ('id',)


class RoomAdmin(admin.ModelAdmin):
    search_fields = ('room_name',)

    class Meta:
        models = Customer

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Consumption)
admin.site.register(Resident)
admin.site.register(OTP)

