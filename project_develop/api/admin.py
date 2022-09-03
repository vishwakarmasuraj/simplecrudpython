from django.contrib import admin

from .models import User

@admin.register(User)

class apiAdmin(admin.ModelAdmin):
    list_display = [id, 'name', 'email', 'password', 'city', 'state']