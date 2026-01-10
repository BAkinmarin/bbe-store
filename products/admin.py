from django.contrib import admin
from .models import Product, Category, Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'reviews_count',
        'image',
    )

    # Order by highest-rated products
    ordering = ["-rating"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rating',
        'review_date',
        'user',
        'order',
        'is_approved',
        'admin_response_short',
    )
    list_filter = (
        'is_approved',
        'rating',
        'review_date',
        'product'
    )
    search_fields = (
        'user__username',
        'product__name',
        'review_text',
        'admin_response',
    )
    readonly_fields = (
        'review_date',
        'admin_response_date',
        'product',
        'user',
        'order',
    )

    fieldsets = (
        ("Review Details", {
            "fields":
            ('product', 'user', 'order',
             'rating', 'review_text', 'review_date')
        }),
        ("Moderation", {
            "fields": ("is_approved",)
        }),
        ("Admin Response", {
            "fields": ("admin_response", "admin_response_date")
        }),
    )

    # Add functionality for bulk approvals
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)

    def admin_response_short(self, obj):
        if obj.admin_response:
            return obj.admin_response[:40] + "..."
        return "—"
    admin_response_short.short_description = "Admin Response"


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
