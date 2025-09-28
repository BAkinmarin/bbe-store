from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """
    Inspired by Code Institute's Boutique Ado Walkthrough Project.
    For maintaining default delivery information and order history.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=False, blank=False)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=False, blank=False)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=False, blank=False)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update UserProfile.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Save existing user profile
    instance.userprofile.save()
