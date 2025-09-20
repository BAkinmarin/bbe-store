from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.db.models import Q
from .forms import ReviewForm
from .models import Product, Category, Review
from django.db.models.functions import Lower
from django.db.models import Avg
from datetime import datetime


def all_products(request):
    """ A view to display all products with search and sort functionality """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Search and sort functionality - inspired by Code Institute's Boutique Ado walkthrough
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria!")
                return redirect (reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'year': datetime.now().year,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to display selected product details including reviews """

    product = get_object_or_404(Product, pk=product_id)

    # Fetch reviews if any
    # reviews = product.reviews.all()
    # has_reviews = reviews.exists()

    # Fetch all reviews, including those where only a rating was left
    reviews = Review.objects.filter(product=product)
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
    #     messages.error(request, "Purchase this product to leave a review.")
    #     return redirect("product_detail", product_id=product.id)

    form = ReviewForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.customer_name = request.user.username
        # review.order = user_orders.first()
        review.save()
        return redirect("product_detail", product_id=product.id)

    return render(request, "submit_product_review.html", {"product": product, "form": form})
