from .views import get_tag
from django.urls import re_path, path
from .views import *


urlpatterns = [
    re_path(r'api/get_tag', get_tag.as_view(), name='get_tag'),
    re_path(r'api/download_video', download_video.as_view(), name='download_video'),
    re_path(r'api/video_details', video_details.as_view(), name='video_details'),
]