from .models import CustomUser
from django.contrib import admin

class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('id','username')

    list_display_links = ('id','username')

admin.site.register(CustomUser, CustomUserAdmin)