from .models import Cart, CartItem
from .views import get_cart_session


def cart_item_counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=get_cart_session(request))
            cart_items = CartItem.objects.filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except:
            cart_count = 0
    return dict(cart_count=cart_count)


