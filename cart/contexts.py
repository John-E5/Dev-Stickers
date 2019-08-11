from django.shortcuts import get_object_or_404
from stickers.models import Sticker


def cart_contents(request):
    """
    ensures that the cart contents are available when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    sticker_count = 0
    for id, quantity in cart.items():
        sticker = get_object_or_404(Sticker, pk=id)
        total += quantity * sticker.price
        sticker_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'sticker': sticker})

    return {'cart_items': cart_items, 'total': total, 'sticker_count': sticker_count}
