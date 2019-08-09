from django.shortcuts import render
from .models import Sticker


def all_stickers(request):
    stickers = Sticker.objects.all()
    return render(request, 'stickers.html', {'stickers': stickers})
