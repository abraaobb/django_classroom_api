from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person

@admin.register(Person)
class PersonAdmin(UserAdmin):
    model = Person
    list_display = ('username', 'email', 'type', 'is_staff', 'is_active')
    list_filter = ('type', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('type',)}),
    )
