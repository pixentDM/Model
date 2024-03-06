from django.contrib import admin

from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'user_id','username','password','email','phone','position','department']
