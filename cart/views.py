from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
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
    return redirect('cart:detail')


def cart_remove(request, product_id):
    product_removed = get_object_or_404(Product,
                                        id=product_id)
    cart = Cart(request)
    cart.remove(product_removed)
    return redirect('cart:detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
