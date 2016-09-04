from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def add_cart(request, product_id):
    product_ordered = get_object_or_404(Product,
                                        id=product_id)
    cart = Cart(request)
    add_cart_form = CartAddProductForm(request.POST or None)
    if add_cart_form.is_valid():
        form_data = add_cart_form.cleaned_data
        cart.add(product=product_ordered,
                 quantity=form_data['quantity'],
                 update_quantity=form_data['update'])
    return redirect()
            
