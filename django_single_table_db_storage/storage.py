"""
Custom Django file storage that saves files in a single database table.
"""


from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import Storage
from django.urls import reverse
# from django.utils.crypto import get_random_string
from django.utils.deconstruct import deconstructible

from .models import SingleTableDbFile


@deconstructible
class SingleTableDbFileStorage(Storage):
    def __init__(self, *args, **kwargs):
        # TODO: load stuff from conf.settings.
        super().__init__(*args, **kwargs)

    def __light_load(self, name):
        return SingleTableDbFile.objects.filter(name=name).only('id', 'created_ts', 'updated_ts').get()

    def _open(self, name, mode='rb'):
        database_file = SingleTableDbFile.objects.filter(name=name).only('id', 'content').get()
        return ContentFile(database_file.content)

    def _save(self, name, content):
        is_public = True  # TODO: compute using settings and looking at name prefix.
        database_file = SingleTableDbFile.objects.create(name=name, content=content.read(), is_public=is_public)
        database_file.save()
        return database_file.name

    def delete(self, name):
        SingleTableDbFile.objects.filter(name=name).delete()

    def exists(self, name):
        return SingleTableDbFile.objects.filter(name=name).exists()

    def get_accessed_time(self, name):
        raise NotImplementedError

    # def get_available_name(self, name, max_length=None):
    #     pass

    def get_created_time(self, name):
        return self.__light_load(name=name).created_ts

    def get_modified_time(self, name):
        return self.__light_load(name=name).updated_ts

    # def get_valid_name(self, name):
    #     pass

    # def generate_filename(self, filename):
    #     pass

    def listdir(self, path):
        raise NotImplementedError

    def size(self, name):
        return NotImplementedError

    def url(self, name):
        return reverse('view_storage_file', kwargs={'name': name})
