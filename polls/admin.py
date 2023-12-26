from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Customer, Vehicle


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "short_name", "user", "mobile"]

class VehicleAdmin(admin.ModelAdmin):
    list_display = ["customer", "reg_num", "reg_date", "rc"]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vehicle, VehicleAdmin)