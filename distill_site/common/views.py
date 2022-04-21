from pathlib import Path
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


BASE_DIR = Path(__file__).resolve().parent.parent
DOMAIN_NAME = getattr(settings, 'DOMAIN_NAME')


def favicon_view(request):
    favicon = BASE_DIR / 'common' / 'static' / 'images' / 'favicon.ico'
    with open(str(favicon), 'rb') as f:
        data = f.read()
    return HttpResponse(data, content_type='image/x-icon')


def robots_view(request):
    content = '\n'.join([
        'User-agent: *',
        'Allow: /',
    ])
    return HttpResponse(content, content_type='text/plain')


def _headers_view(request):
    content = '\n'.join([
        f'https://:project.pages.dev/*',
        f'  X-Robots-Tag: noindex',
        f'  Location: https://{DOMAIN_NAME}/',
        f'',
        f'/*',
        f'  X-Frame-Options: DENY',
        f'  X-Content-Type-Options: nosniff',
        f'  Referrer-Policy: no-referrer',
        f'  Permissions-Policy: document-domain=()',
        f'  Content-Security-Policy: script-src \'self\'; frame-ancestors \'none\';',
    ])
    return HttpResponse(content, content_type='text/plain')


def error404_view(request):
    return render(request, 'error404.html', status=404)
