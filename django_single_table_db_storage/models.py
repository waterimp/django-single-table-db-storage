# import uuid
from django.db import models
from django_extensions.db.fields import (CreationDateTimeField,
                                         ModificationDateTimeField)


class SingleTableDbFile(models.Model):
    class Meta:
        db_table = 'storage_file'
    # uuid = models.UUIDField(primary_key=False,
    #                         default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500, unique=True)
    content = models.BinaryField(null=False, blank=True)
    created_ts = CreationDateTimeField()
    updated_ts = ModificationDateTimeField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return '<SingleTableDbFile object>'
