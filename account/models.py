from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import *

# Create your models here.

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class Type(models.Model):
    typ = models.CharField(max_length=10)

    def __str__(self) -> str:
        return (self.typ)


class Store(models.Model):
    usr_store_name = models.TextField(blank=True, validators=[RegexValidator(regex='[A-Za-z]', message='Please Enter Correct Name')])

    def __str__(self) -> str:
        return self.usr_store_name


class Usr(AbstractUser):
    usr_img = models.ImageField(blank=True)
    usr_phone = models.TextField(blank=True)
    usr_store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, related_name='store')
    usr_type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='type', null=True)

    def __str__(self) -> str:
        return (self.username)


class Profile(models.Model):
    user = models.OneToOneField(Usr, on_delete=models.CASCADE, related_name="profile")

    def __str__(self) -> str:
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)