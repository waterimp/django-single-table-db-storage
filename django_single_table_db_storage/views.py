from io import BytesIO

from django.http import FileResponse

from .models import SingleTableDbFile


def view_storage_file(request, name):
    database_file = SingleTableDbFile.objects.get(name=name, is_public=True)
    # reported_filename = name.split('/')[-1]

    # may need to customize more if not intelligent enough.
    # reference: https://docs.djangoproject.com/en/2.2/ref/request-response/#fileresponse-objects
    # it would be cool to examine the filename to get the mime type.
    response = FileResponse(BytesIO(database_file.content))
    return response
