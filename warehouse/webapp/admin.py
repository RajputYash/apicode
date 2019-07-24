from django.contrib import admin
from .models import User,Customer,Consumption,Resident,Room

# # Register your models here.
# class ConsumptionAdmin(admin.ModelAdmin):
#     list_display= ['user_consumption','date']
#     #search_fields=(' ' , ' ')
#     class Meta:
#         models=Consumption


class UserAdmin(admin.ModelAdmin):
    search_fields = ('id','username','UserType')
    list_display = ['id','username','UserType']
    ordering = ('id',)


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('id','Username')
    list_display = ['id','Username','Email','Contact_no','Address','Contract_date']
    ordering = ('id',)


class RoomAdmin(admin.ModelAdmin):
    search_fields = ('room_name',)

    # autocomplete_fields=('Created_by',)
    # list_filter=('Created_by',)
    # list_select_related=('Created_by',)

    class Meta:
        models=Customer
admin.site.register(Room,RoomAdmin)
admin.site.register(Resident)
admin.site.register(User,UserAdmin)
admin.site.register(Customer,CustomerAdmin)
#admin.site.register(Consumption,ConsumptionAdmin)