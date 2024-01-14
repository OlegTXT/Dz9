from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', genre_list_view, name='category'),
    re_path(r'^(?P<pk>[\w-]+)/$', genre_detail_view, name='genre_detail'),
    re_path(r'^(?P<pk>[\w-]+)/(?P<musician_slug>[\w-]+)/$', musician_detail_view, name='musician_detail')
]
