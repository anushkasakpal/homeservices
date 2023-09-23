from django.contrib import admin

from .models import usermodel


# Register your models here.

# Register your models here.
class usermodelAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'phone','email','services','serviceTime', 'serviceDate', 'state', 'pincode']
admin.site.register(usermodel,usermodelAdmin)

