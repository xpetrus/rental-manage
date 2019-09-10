from django.contrib import admin
from .models import Rental, Invoice, Vendor

# Register your models here.
admin.site.register(Rental)
admin.site.register(Invoice)
admin.site.register(Vendor)
