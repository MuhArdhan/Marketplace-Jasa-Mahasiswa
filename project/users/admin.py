from django.contrib import admin
from django.contrib import admin
from .models import Customer, Vendor, Admin

admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Admin)