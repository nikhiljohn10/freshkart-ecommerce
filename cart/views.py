from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Product

from .models import Cart, CartItem


def _cart_id(req):
    cart = req.session.session_key
    if not cart:
        cart = req.session.create()
    return cart


def cart_home(req, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(req))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for item in cart_items:
            total += item.sub_total()
            counter += item.quantity
    except ObjectDoesNotExist:
        pass
    return render(
        req, "cart.html", dict(cart_items=cart_items, total=total, counter=counter)
    )


def add_cart(req, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(req))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(req))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    return redirect("cart:home")


def remove_cart(req, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(req))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("cart:home")


def delete_cart(req, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(req))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect("cart:home")
