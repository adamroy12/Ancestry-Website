from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    is_full_name_displayed = models.BooleanField(default=True)

    #Ancestry Information
    info = models.CharField(max_length=1000, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)

    #contact details
    emailaddress = models.EmailField(max_length=250, default="default_email")
    phone_number = PhoneNumberField(blank=True)


