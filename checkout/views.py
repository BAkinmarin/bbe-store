from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from basket.contexts import basket_contents

import stripe

# Create your views here.


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your shopping basket")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_live_51RbJqlIx6wkpjSguSUKdGr4o4wacvKoUpVqKJvSeJLPqKcQkyhYj9XSOgoXFOT7F6M9g7YdzI612o9WiG2klCmTG003wITVEd7',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
