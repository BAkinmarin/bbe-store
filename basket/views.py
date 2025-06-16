from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_basket(request):
    """ A view that renders the shopping basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add quantity of selected product to shopping basket """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    
    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Update quantity of selected products in shopping basket to selected amount """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove selected item from shopping basket """
    basket = request.session.get('basket', {})

    if item_id in basket:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
