from urllib.parse import urlunsplit
import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from content.models import Stargazer


class Command(BaseCommand):

    help = 'Syncs GitHub stargazers for the specified repo'
    api_scheme = 'https'
    api_netloc = 'api.github.com'

    def get_github_stargazers(self, repo_user, repo_name, username, token):
        page = 1
        stargazers = []
        while True:
            uri = f'/repos/{repo_user}/{repo_name}/stargazers'
            q = f'page={page}'
            url = urlunsplit((self.api_scheme, self.api_netloc, uri, q, ''))
            self.stdout.write(f'Fetching: {url}')
            response = requests.get(url, auth=(username, token))
            if response.status_code == 200:
                data = response.json()
                if data:
                    stargazers += data
                else:
                    self.stdout.write(f'Empty page, breaking...')
                    break
            page += 1
        return stargazers

    def save_stargazer(self, stargazer):
        username = stargazer.get('login')
        userid = stargazer.get('id')
        url = stargazer.get('html_url')
        avatar = stargazer.get('avatar_url')
        if not username or not userid or not url or not avatar:
            self.stderr.write(f'Skipping malformed stargazer: {stargazer}')
            return
        try:
            stargazer = Stargazer.objects.get(id=int(userid))
        except Stargazer.DoesNotExist:
            stargazer = Stargazer(id=int(userid))
        stargazer.name = str(username).strip()
        stargazer.url = str(url).strip()
        stargazer.avatar = str(avatar).strip()
        stargazer.save()
        self.stdout.write(f'Saved stargazer: {stargazer.name} '
                          f'({stargazer.id})')
        
    def cleanup_stargazers(self):
        self.stdout.write(f'Deleting existing stargazers...')
        Stargazer.objects.all().delete()

    def handle(self, *args, **options):
        gitub_repo_username = getattr(settings, 'GITHUB_REPO_USERNAME')
        if not gitub_repo_username:
            raise CommandError(f'settings.GITHUB_REPO_USERNAME must be set')
        gitub_repo_name = getattr(settings, 'GITHUB_REPO_NAME')
        if not gitub_repo_name:
            raise CommandError(f'settings.GITHUB_REPO_NAME must be set')
        gitub_username = getattr(settings, 'GITHUB_USERNAME')
        if not gitub_username:
            raise CommandError(f'settings.GITHUB_USERNAME must be set')
        gitub_token = getattr(settings, 'GITHUB_ACCESS_TOKEN')
        if not gitub_token:
            raise CommandError(f'settings.GITHUB_ACCESS_TOKEN must be set')
        self.stdout.write(f'Syncing GitHub stargazers...')
        stargazers = self.get_github_stargazers(
            gitub_repo_username, gitub_repo_name, gitub_username, gitub_token)
        if stargazers:
            self.cleanup_stargazers()
            for stargazer in stargazers:
                self.save_stargazer(stargazer)
        self.stdout.write(f'Done')
