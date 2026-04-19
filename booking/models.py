from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
# Create your models here.

class EmailOTP(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.otp}"
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()

    booking_date = models.DateTimeField(auto_now_add=True)

    delivery_date = models.DateTimeField(null=True, blank=True)

    price = models.IntegerField(default=1100)  # ₹ price

    status = models.CharField(
        max_length=20,
        default='Pending',
        choices=[
            ('Pending', 'Pending'),
            ('Dispatched', 'Dispatched'),
            ('Delivered', 'Delivered'),
        ]
    )

    def save(self, *args, **kwargs):
        if not self.delivery_date:
            self.delivery_date = timezone.now() + timedelta(days=2)
        super().save(*args, **kwargs)

class DeliveryOTP(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)