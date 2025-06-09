from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .forms import ReviewForm
from .models import Product


# Create your views here.


def all_products(request):
    """ A view to display all products with search and sort functionality """

    products = Product.objects.all()
    query = None

    # Search functionality - inspired by Code Institute's Boutique Ado walkthrough
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria!")
                return redirect (reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display selected product details including reviews """

    product = get_object_or_404(Product, pk=product_id)

    # Fetch reviews if any
    reviews = product.reviews.all()  # type: ignore
    has_reviews = reviews.exists()

    context = {
        'product': product,
        'reviews': reviews,
        'has_reviews': has_reviews,
    }

    return render(request, 'products/product_detail.html', context)


def submit_product_review(request, product_id):
    """ A view to invite customers to leave feedback on verified purchases """
    product = get_object_or_404(Product, pk=product_id)
    # user_orders = Order.objects.filter(user=request.user, products=product)

    # if not user_orders.exists():
    #     messages.error(request, "Please purchase this product to leave a review.")
    #     return redirect("product_detail", product_id=product.id)

    form = ReviewForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.customer_name = request.user.username
        # review.order = user_orders.first()
        review.save()
        return redirect("product_detail", product_id=product.id)  # type: ignore

    return render(request, "submit_product_review.html", {"product": product, "form": form})
