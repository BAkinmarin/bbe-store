from django.contrib import admin
from .models import Product, Category, Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'aggregate_rating',
        'reviews_count',
        'image',
    )

    # Order by highest-rated products
    ordering = ["-aggregate_rating"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'customer_name',
        'product',
        'rating',
        'review_date',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
