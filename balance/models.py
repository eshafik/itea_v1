from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.

class IndividualBalance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=4)
    due_month = models.PositiveIntegerField(null=True,blank=True)
    payment_details = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username



class OrganizationBalance(models.Model):
    capital = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=4)
    total_profit = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=4)
    total_loss = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=4)
    investment_details = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
