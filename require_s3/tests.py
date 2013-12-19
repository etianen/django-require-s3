from django.test import TestCase
from django.test.utils import override_settings
from django.utils.functional import empty
from django.contrib.staticfiles.storage import staticfiles_storage


TEST_SETTINGS = {
    "AWS_STORAGE_BUCKET_NAME": "etianen-django-require-s3",
    "AWS_QUERYSTRING_AUTH": False,
    "CACHES": {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        },
    },
}


class ResetStaticFilesStorageMixin(object):

    def setUp(self):
        staticfiles_storage._wrapped = empty


@override_settings(
    STATICFILES_STORAGE = "require_s3.storage.OptimizedStaticFilesStorage",
    **TEST_SETTINGS
)
class TestOptimizedStaticFilesStorage(ResetStaticFilesStorageMixin, TestCase):

    def testFilePath(self):
        self.assertEqual(
            staticfiles_storage.url("test.png"),
            "https://etianen-django-require-s3.s3.amazonaws.com/test.png",
        )

    def testFolderPath(self):
        self.assertEqual(
            staticfiles_storage.url("test/"),
            "https://etianen-django-require-s3.s3.amazonaws.com/test/",
        )


@override_settings(
    STATICFILES_STORAGE = "require_s3.storage.OptimizedCachedStaticFilesStorage",
    **TEST_SETTINGS
)
class TestOptimizedCachedStaticFilesStorage(ResetStaticFilesStorageMixin, TestCase):

    def testFilePath(self):
        self.assertEqual(
            staticfiles_storage.url("test.png"),
            "https://etianen-django-require-s3.s3.amazonaws.com/test.5e3ae665fe7b.png",
        )

    def testFolderPath(self):
        self.assertEqual(
            staticfiles_storage.url("test/"),
            "https://etianen-django-require-s3.s3.amazonaws.com/test/",
        )
