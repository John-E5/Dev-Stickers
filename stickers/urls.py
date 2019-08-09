from django.conf.urls import url
from .views import all_stickers

urlpatterns = [
    url(r'^stickers/', all_stickers, name='stickers'),
]

