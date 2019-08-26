from django.shortcuts import render
from posts.models import Post
from stickers.models import Sticker


def index(request):
    """
        A view that displays the landing page and retrieves Data from the DB
        to Display in sections.
        newest stickers
        latest posts
    """
    stickers = Sticker.objects.all()[:4]
    posts = Post.objects.all().order_by('created_date')[:2]

    args = {'posts': posts, 'stickers': stickers}
    return render(request, 'index.html', args)
