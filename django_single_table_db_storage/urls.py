from django.urls import re_path

from .views import view_storage_file

urlpatterns = [
    re_path(r'^(?P<name>.+)$', view_storage_file, name='view_storage_file')
]
