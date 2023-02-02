from .views import get_tag
from django.urls import re_path, path
from .views import *


urlpatterns = [
    # path('', home.as_view(), name='home'),
    re_path(r'api/get_tag', get_tag.as_view(), name='get_tag'),
]