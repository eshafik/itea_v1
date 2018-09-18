from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.core.validators import RegexValidator



class Profile(models.Model):
    STATUS_CHOICES = ( 
        ('student', 'Student'), 
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
    )
    ITEA_STATUS = (
        ('member','General Member'),
        ('executive','Executive Member'),
        ('public', 'Public'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    current_status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='student') 

    status_details = models.TextField(blank=True,null=True)
    mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+8801'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[mobile_regex], max_length=17,null=True, blank=True) 
    date_of_birth = models.DateField(blank=True,null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True,null=True)
    current_address = models.TextField(blank=True,null=True)
    permanent_address = models.TextField(blank=True,null=True)
    itea_status = models.CharField(max_length=20,choices=ITEA_STATUS,default='public')
    finance = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('profile_details',args=[self.user.username])

    def is_executive(self):
        if str(self.itea_status) == 'executive':
            return True
        else:
            return False

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
