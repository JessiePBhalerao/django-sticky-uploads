from django.urls import re_path

from .views import UploadView

urlpatterns = [
    re_path(r'^default/$', UploadView.as_view(), name='sticky-upload-default'),
]
