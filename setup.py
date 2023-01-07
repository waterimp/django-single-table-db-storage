from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longdesc = f.read()

setup(
    name="django-single-table-db-storage",
    version="0.1.0",
    description="Provides a Django storage implementation that uses a single database table.",
    long_description=longdesc,
    long_description_content_type="text/markdown",
    url="https://github.com/waterimp/django-single-table-db-storage",
    author="Lee Bush",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Text Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
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