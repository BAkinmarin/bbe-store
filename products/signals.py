from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Review


@receiver(post_delete, sender=Review)
def update_product_rating_on_delete(sender, instance, **kwargs):
    instance.product.update_aggregate_rating()
