import yaml
from markdown import markdown
from bs4 import BeautifulSoup
from django.conf import settings
from django.http import Http404
from django.template import Template, Context
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


def static_page_render(name, context={}):
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
    header = yaml.safe_load(header_str.strip())
    plain_html = markdown(content_str.strip())
    content = add_bulma_classes(plain_html)
    django_rendered_html = Template(content)
    django_template_context = Context(context)
    return header, django_rendered_html.render(django_template_context)


_extra_css_classes = {
    'h1': [
        'title',
        'is-size-3-desktop',
        'is-size-4-tablet',
        'is-size-5-mobile'
    ],
    'h2': [
        'subtitle',
        'is-size-4-desktop',
        'is-size-5-tablet',
        'is-size-6-mobile',
        'is-side-note'
    ],
    'code': [
        'is-family-code'
    ]
}


def add_bulma_classes(html):
    """
        Adds Bulma CSS framework classes to an HTML document. Used to add
        default CSS classes to HTML rendered automatically from Markdown.
    """
    soup = BeautifulSoup(html, 'html.parser')
    for tag, classes in _extra_css_classes.items():
        for tag in soup.find_all(tag):
            tag['class'] = tag.get('class', []) + classes
    return str(soup)
