from django.conf.urls import url
from .views import get_posts

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
]
