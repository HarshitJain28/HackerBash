from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from service.models import Consumer

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Consumer.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()