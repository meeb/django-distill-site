from markdown import markdown
from django.conf import settings
from django.http import Http404
from common.utils import lowercase_ascii_only



def render(name):
    name = lowercase_ascii_only(name)
    path = settings.BASE_DIR / 'content' / 'markdown' / f'{name}.md'
    if not path.is_file():
        raise Http404(f'Markdown content does not exist: {name} ({path})')
    with open(str(path), 'rt') as f:
        d = f.read()
    return markdown(d)
