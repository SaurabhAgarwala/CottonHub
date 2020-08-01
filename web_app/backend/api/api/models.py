from django.db import models
from django.contrib.auth.models import AbstractUser,Group


PERIOD = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )

class User(AbstractUser):

    CUSTOMER = 1
    FARMER = 2
    MINISTRY =3
    
    GROUP_CHOICES = (
        (CUSTOMER, 'Customer'),
        (FARMER, 'Farmer'),
        (MINISTRY, 'Ministry'),
    )

    email               = models.CharField(max_length=50,null = True, blank = True)
    pan                 = models.CharField(verbose_name="PAN Number",max_length=15,null=False,blank =False)
    aadhar              = models.CharField(verbose_name="Aadhar Number",max_length=20,null=False,blank = False)
    gst                 = models.CharField(max_length=20,default = "")
    REQUIRED_FIELDS     = ['email','pan','aadhar','first_name','last_name']

    def __str__(self):

        return self.username + "  " + self.first_name

class PhoneOtp(models.Model):

    phone_relation      = models.ForeignKey(User,on_delete = models.CASCADE)
    otp                 = models.CharField(verbose_name="otp",max_length=8,null = False)
    count               = models.IntegerField(verbose_name="otp_count",default = 0)
