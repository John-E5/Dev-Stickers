from django.conf.urls import url
from .views import all_stickers

urlpatterns = [
    url(r'^', all_stickers, name='stickers'),
]

