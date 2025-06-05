from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from django.contrib import messages
from .forms import ReviewForm

# Create your views here.


def all_products(request):
    """ A view to display all products with search and sort functionality """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display selected product details including reviews """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/products.html', context)


def submit_product_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_orders = Order.objects.filter(user=request.user, products=product)

    if not user_orders.exists():
        messages.error(request, "Please purchase this product to leave a review.")
        return redirect("product_detail", product_id=product.id)


    form = ReviewForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.customer_name= request.user.username
        review.order= user_orders.first()
        review.save()
        return redirect("product_detail", product_id=product.id)

    return render(request, "submit_product_review.html", {"product": product, "form": form})
