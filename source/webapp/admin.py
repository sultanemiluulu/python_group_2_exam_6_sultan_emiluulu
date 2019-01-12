from django.contrib import admin
from django.contrib.auth.models import User
from webapp.models import UserInfo, Post
from django.contrib.auth.admin import UserAdmin

class ClientInline(admin.StackedInline):
    model = UserInfo
    filter_horizontal = ('friend',)

class UserInfoAdmin(UserAdmin):
    inlines = [ClientInline]


admin.site.unregister(User)
admin.site.register(User, UserInfoAdmin)
admin.site.register(Post)
