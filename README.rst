django-require-s3
=================

**django-require-s3** integrates `django-require <https://github.com/etianen/django-require>`_
with the S3 storage backend from `django-storages <http://django-storages.readthedocs.org/en/latest/>`_.


Features
--------

-  Optimize your static assets using `django-require <https://github.com/etianen/django-require>`_
-  Upload compiled assets to Amazon S3 using `django-storages <http://django-storages.readthedocs.org/en/latest/>`_.


Installation
------------

1. Checkout the latest django-require-s3 release and copy or symlink the
   ``require_s3`` directory into your ``PYTHONPATH``.  If using pip, run 
   ``pip install django-require-s3``.
2. Set your ``STATICFILES_STORAGE`` setting to
   ``'require_s3.storage.OptimizedStaticFilesStorage'`` or
   ``'require_s3.storage.OptimizedCachedStaticFilesStorage'``.


Support and announcements
-------------------------

Downloads and bug tracking can be found at the `main project
website <http://github.com/etianen/django-require-s3>`_.


More information
----------------

The django-require-s3 project was developed by Dave Hall. You can get the
code from the `django-require-s3 project
site <http://github.com/etianen/django-require-s3>`_.

Dave Hall is a freelance web developer, based in Cambridge, UK. You can
usually find him on the Internet in a number of different places:

-  `Website <http://www.etianen.com/>`_
-  `Twitter <http://twitter.com/etianen>`_
-  `Google Profile <http://www.google.com/profiles/david.etianen>`_

