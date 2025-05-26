from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to display all products with search and sort functionality """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
