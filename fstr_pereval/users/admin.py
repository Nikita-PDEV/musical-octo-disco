from django.contrib import admin
from .models import PassUser

@admin.register(PassUser)
class PassUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'status')