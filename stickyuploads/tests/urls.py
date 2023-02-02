from django.urls import include, re_path


urlpatterns = [
    re_path(r'^sticky-uploads/', include('stickyuploads.urls')),
]
