from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view that renders the shopping basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add quantity of selected product to shopping basket """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'{basket[item_id]} x {product.name} added to basket!')
    else:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} added to basket!')

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Update quantity of selected products in basket to selected amount """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'{product.name} updated to {basket[item_id]} in basket!')
    else:
        basket.pop(item_id)
        messages.success(request, f'{product.name} removed from basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove selected item from shopping basket """
    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})

    try:
        if item_id in basket:
            basket.pop(item_id)
            messages.success(request, f'{product.name} removed from basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:

        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
