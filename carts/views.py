from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def get_cart_session(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=get_cart_session(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.stock * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    context = {
        "total": total,
        "quantity": quantity,
        "cart_items": cart_items,
    }
    return render(request, 'store/cart.html', context)


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=get_cart_session(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=get_cart_session(request)
        )
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()

    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_session(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def delete_cart(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_session(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

