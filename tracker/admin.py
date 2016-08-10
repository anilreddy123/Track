from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
from .models import Usertype


# Register your models here.


class UsertypeInline(admin.StackedInline):
    model = Usertype
    can_delete = False
    verbose_name_plural = 'usertype'


class UserAdmin(BaseUserAdmin):
    inlines = (UsertypeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(AddDevice)
admin.site.register(MobileReg)
admin.site.register(Notify)
admin.site.register(IP)
admin.site.register(Port)
