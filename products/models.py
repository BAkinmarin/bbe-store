from django.db import models
from django.db.models import Avg


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # Dynamically update the aggregate rating whenever a new review is added
    aggregate_rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    @property
    def reviews_count(self):
        return self.reviews.count()

    @property
    def update_aggregate_rating(self):
        avg_rating = self.reviews.aggregate(models.Avg('rating'))['rating__avg']
        self.aggregate_rating = avg_rating if avg_rating else 0.0
        self.save()


# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     order_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    customer_name = models.CharField(max_length=254)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review_text = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    # Link customer review to a customer order for verification
    # order = models.ForeignKey("orders.Order", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.customer_name} - {self.product.name} ({self.rating}/5)"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_aggregate_rating()
