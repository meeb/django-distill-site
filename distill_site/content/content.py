import yaml
from markdown import markdown
from django.conf import settings
from django.http import Http404
from common.utils import lowercase_ascii_only


_app = 'content'
_dir = 'static_content'
_markdown_ext = 'md'
_combined_page_ext = 'yamlmd'


def markdown_render(name):
    name = lowercase_ascii_only(name)
    path = settings.BASE_DIR / _app / _dir / f'{name}.{_markdown_ext}'
    if not path.is_file():
        raise Http404(f'Markdown content does not exist: {name} ({path})')
    with open(str(path), 'rt') as f:
        d = f.read()
    return markdown(d)


def static_page_render(name):
    """
        'yamlmd' files are static content files with a YAML header, then a
        normal --- break, then markdown content.
    """
    splitter = '\n---\n'
    name = lowercase_ascii_only(name)
    path = settings.BASE_DIR / _app / _dir / f'{name}.{_combined_page_ext}'
    if not path.is_file():
        raise Http404(f'Static page content does not exist: {name} ({path})')
    with open(str(path), 'rt') as f:
        d = f.read().replace('\r\n', '\n')
    if splitter not in d:
        raise Exception(f'Malformed page content (no ---): {name} ({path})')
    header_str, content_str = d.split(splitter, 1)
    return yaml.safe_load(header_str.strip()), markdown(content_str.strip())
