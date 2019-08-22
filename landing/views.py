from django.shortcuts import render
from posts.models import Post


def index(request):
    """
        A view that displays the landing page and retrieves Data from the DB
        to Display in sections.
        newest stickers
        latest posts
    """
    posts = Post.objects.all().order_by('created_date')[:2]
    return render(request, 'index.html', {'posts': posts})
