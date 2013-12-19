from setuptools import setup

from require_s3 import __version__


version_str = ".".join(str(n) for n in __version__)


setup(
    name = "django-require-s3",
    version = version_str,
    license = "BSD",
    description = "An integration between django-require and the S3 storage backend from django-storages.",
    author = "Dave Hall",
    author_email = "dave@etianen.com",
    url = "https://github.com/etianen/django-require-s3",
    packages = [
        "require_s3",
    ],
    zip_safe = False,
    install_requires = [
        "django-require",
        "django-storages",
        "boto",
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
