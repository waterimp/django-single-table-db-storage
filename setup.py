from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longdesc = f.read()

setup(
    name="django-single-table-db-storage",
    version="0.1.1",
    description="Provides a Django storage implementation that uses a single database table.",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url="https://github.com/waterimp/django-single-table-db-storage",
    author="Lee Bush",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
    ],
    keywords="django storage database",
    packages=['django_single_table_db_storage'],
    package_dir={'django_single_table_db_storage': 'django_single_table_db_storage'},
    package_data={},
    scripts=[],
    install_requires=[
          'Django>=3.2',
      ],
    python_requires=">=3.5",
)