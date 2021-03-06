from django.shortcuts import render, get_object_or_404

from .models import Category, Product

from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context_data = {'category': category,
                    'categories': categories,
                    'products': products
                    }
    return render(request,
                  'shop/product/list.html',
                  context_data)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    related_products = Product.objects.filter(
        category=product.category
    )
    cart_add_form = CartAddProductForm()
    context_data = {'product': product,
                    'cart_add_form': cart_add_form,
                    'related_products': related_products}
    return render(request,
                  'shop/product/detail.html',
                  context_data)
