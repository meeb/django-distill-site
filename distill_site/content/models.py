from django.db import models


class Stargazer(models.Model):
    """
        GitHub stargazers for the specified project.
    """

    id = models.PositiveIntegerField(
        primary_key=True,
        help_text='GitHub user ID'
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        db_index=True,
        help_text='GitHub username'
    )
    url = models.URLField(
        help_text='GitHub user profile URL'
    )
    avatar = models.URLField(
        help_text='GitHub user avatar URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Stargazer'
        verbose_name_plural = 'Stargazers'
        ordering = ('name',)


class Release(models.Model):
    """
        PyPI releases for the specified project.
    """

    version = models.CharField(
        max_length=16,
        db_index=True,
        help_text='Version of the release'
    )
    url = models.URLField(
        help_text='URL of the release'
    )
    published = models.DateTimeField(
        db_index=True,
        help_text='Date and time of the release'
    )

    def __str__(self):
        return self.version

    class Meta:
        verbose_name = 'Release'
        verbose_name_plural = 'Releases'
        ordering = ('-published',)

    @classmethod
    def get_latest(obj):
        try:
            return obj.objects.order_by('-published')[0]
        except IndexError:
            return None
