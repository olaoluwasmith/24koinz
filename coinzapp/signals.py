from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import *

User = get_user_model()


@receiver(post_save, sender=User)
def create_detail(sender, instance, created, **kwargs):
    if created:
        Detail.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_detail(sender, instance, **kwargs):
    instance.detail.save()