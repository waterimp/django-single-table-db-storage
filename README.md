This Python package provides a Django storage implementation that uses a single database table.

Django developers may find this package may be most helpful for use in their test and prototype environments.
This package may also be useful in launching small-scale projects/environments quickly without needing additional infrastructure setup.

**WARNING:** For production applications, please consider using a CDN instead of this package, as it is not a good practice to serve files from a database. Website performance will suffer! Please see the section "Alternatives" below for performant and scalable storage options.

# Features / Benefits

* Easy to install and configure.
* Serve files properly when there are multiple django servers under a load balancer.
* Files persist in database when application server is rebuilt (as long as database is not hosted on the application server).
* In unit testing scenarios, created files can be automatically "rolled back" out of existence if the unit test uses a transaction, which is how `django.test.TestCase` works.


# Installation


```shell
pip install django-single-table-db-storage
```

# Setup

In your django settings file, add `'django_single_table_db_storage'` to `INSTALLED_APPS`.

```python3
INSTALLED_APPS = [
    ...
    'django_single_table_db_storage',
    ...
]
```

Also in your django settings file, set up the default storage. It is recommended that you add a TODO to remind yourself to use a better storage in the future.

```python
# TODO: As this project scales, a CDN or S3-compatible storage for production
#       might be a better solution.
DEFAULT_FILE_STORAGE = 'django_single_table_db_storage.storage.SingleTableDbFileStorage'
```

In your django settings file, you should determine the default accesibility of the files that are uploaded.


```python
DJANGO_SINGLE_TABLE_DEFAULT_PUBLIC = True  # or set it to False. The default is False.

```

Mount the URLs where you want in your `urls.py` file.

```python
urlpatterns = [
    ... 
    path('files/', include('django_single_table_db_storage.urls')),
    ....
]
```

Run the database migrations to create the table.

```shell
./manage.py migrate
```

...And now your environment is set to use the file storage.


# Alternatives

You can find other file storage alternatives for Django here:

https://djangopackages.org/grids/g/storage-backends/


This package contains a similar and possibly better implementation to this library, depending on your use case and license that you prefer:

https://github.com/kimetrica/django-binary-database-files/

