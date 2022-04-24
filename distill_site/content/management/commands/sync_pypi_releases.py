from dateutil.parser import parse as parse_date
from urllib.parse import urlunsplit
import feedparser
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from content.models import Release


class Command(BaseCommand):

    help = 'Syncs PyPI releases for the specified package'
    rss_scheme = 'https'
    rss_netloc = 'pypi.org'

    def get_pypi_releases(self, package):
        uri = f'/rss/project/{package}/releases.xml'
        url = urlunsplit((self.rss_scheme, self.rss_netloc, uri, '', ''))
        self.stdout.write(f'Parsing release RSS URL: {url}')
        data = feedparser.parse(url)
        return data.get('entries', [])

    def save_release(self, release):
        title = release.get('title')
        link = release.get('link')
        published = release.get('published')
        if not title or not link or not published:
            self.stderr.write(f'Skipping malformed release: {release}')
            return
        try:
            release = Release.objects.get(url=str(link))
        except Release.DoesNotExist:
            release = Release(url=str(link))
        release.version = str(title).strip()
        release.published = parse_date(published)
        release.save()
        self.stdout.write(f'Saved release: {release.url}')

    def handle(self, *args, **options):
        pypi_package = getattr(settings, 'PYPI_PACKAGE')
        if not pypi_package:
            raise CommandError(f'settings.PYPI_PACKAGE must be set')
        self.stdout.write(f'Syncing PyPI releases...')
        releases = self.get_pypi_releases(pypi_package)
        for release in releases:
            self.save_release(release)
        self.stdout.write(f'Done')
