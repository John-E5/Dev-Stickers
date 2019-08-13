from django.shortcuts import render
from stickers.models import Sticker


def do_search(request):
    stickers = Sticker.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'stickers.html', {'stickers': stickers})
