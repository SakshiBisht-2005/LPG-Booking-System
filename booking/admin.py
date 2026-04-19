from django.contrib import admin
from .models import EmailOTP, Booking, DeliveryOTP

# Register your models here.

admin.site.register(EmailOTP)
admin.site.register(Booking)
admin.site.register(DeliveryOTP)