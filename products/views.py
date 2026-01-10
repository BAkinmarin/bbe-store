from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import ReviewForm, ProductForm
from .models import Product, Category, Review

from django.db.models.functions import Lower
from django.db.models import Avg

from datetime import datetime

from functools import wraps
from checkout.models import Order, OrderLineItem


def all_products(request):
    """ A view to display all products with search and sort functionality """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Search and sort functionality - inspired by Code Institute's Boutique Ado
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
                return redirect(reverse('products'))

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
    """ A view to display individual products and details """
    product = get_object_or_404(Product, pk=product_id)

    user_orders_with_product = []
    reviewed_order_ids = []

    if request.user.is_authenticated:
        # Find all orders where the user bought this product
        order_ids = OrderLineItem.objects.filter(
            order__user_profile=request.user.userprofile,
            product=product
        ).values_list("order_id", flat=True)

        user_orders_with_product = Order.objects.filter(id__in=order_ids)

        # Find which of those orders already have reviews
        reviewed_order_ids = list(Review.objects.filter(
            user=request.user,
            product=product,
            order_id__in=order_ids
        ).values_list("order_id", flat=True))

    context = {
        "product": product,
        "user_orders_with_product": user_orders_with_product,
        "reviewed_order_ids": reviewed_order_ids,
        'product_id': product.id,
        'has_reviews': Review.objects.filter(product=product).exists(),
        'reviews':
            Review.objects.filter(product=product).order_by('-review_date'),
    }

    return render(request, "products/product_detail.html", context)


@login_required
def review_product(request, order_id, product_id):
    """ A view to display product reviews of verified purchases """
    product = get_object_or_404(Product, pk=product_id)
    order = get_object_or_404(Order, pk=order_id,
                              user_profile=request.user.userprofile)

    # Check that this order actually contains this product
    purchased = OrderLineItem.objects.filter(
        order=order,
        product=product
    ).exists()

    if not purchased:
        messages.error(request, "This product is not part of that order.")
        return redirect("product_detail", product_id=product.id)

    # Check if review already exists for this product/order
    already_reviewed = Review.objects.filter(
        user=request.user,
        product=product,
        order=order
    ).exists()

    if already_reviewed:
        messages.error(request, "You already have a review for this order.")
        return redirect("product_detail", product_id=product.id)

    form = ReviewForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.user = request.user
        review.order = order
        review.save()

        messages.success(request, "Thanks for reviewing your purchase!")
        return redirect("product_detail", product_id=product.id)

    context = {
        "product": product,
        "order": order,
        "form": form,
    }

    return render(request, "products/review_product.html", context)


def superuser_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only the store owner can do that!')
            return redirect(reverse('home'))
        return view_func(request, *args, **kwargs)
    return wrapper


@superuser_required
def add_product(request):
    """ Functionality for Admin to add products to store """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory update successful!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Inventory update failed. Please check form and try again.')

    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        }

    return render(request, template, context)


@superuser_required
def modify_product(request, product_id):
    """ Functionality for Admin to modify an existing product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product modification successful!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product modification failed. Please check form and try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are about to modify {product.name}!')

    template = 'products/modify_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@superuser_required
def delete_product(request, product_id):
    """ Functionality for Admin to delete an existing product from store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect(reverse('products'))
