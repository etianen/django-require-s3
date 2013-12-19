from django.contrib.staticfiles.storage import CachedFilesMixin

from storages.backends.s3boto import S3BotoStorage

from require.storage import OptimizedFilesMixin


class FolderNameHackMixin(object):

    # HACK: Fixing handling of folder names.
    def url(self, name, *args, **kwargs):
        url = super(FolderNameHackMixin, self).url(name, *args, **kwargs)
        if name.endswith("/") and not url.endswith("/"):
            url += "/"
        return url


class OptimizedStaticFilesStorage(FolderNameHackMixin, OptimizedFilesMixin, S3BotoStorage):
    
    """
    A storage backend that optimizes with RequireJS and stores the result on S3.
    """


class OptimizedCachedStaticFilesStorage(FolderNameHackMixin, OptimizedFilesMixin, CachedFilesMixin, S3BotoStorage):
    
    """
    A storage backend that optimizes with RequireJS, applies a cached MD5 suffix,
    and stores the result on S3.
    """
