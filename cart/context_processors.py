from .models import Cart, CartItem
from .views import _cart_id


def counter(req):
    item_count = 0
    if "admin" in req.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(req))
            cart_items = CartItem.objects.all().filter(cart=cart)
            for item in cart_items:
                item_count += item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)
