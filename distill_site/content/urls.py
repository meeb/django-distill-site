from django_distill import distill_path
from .views import index_view, yamlmd_page_view


app_name = 'content'


def iter_yamlmd_pages():
    """
        A static list of the page names to be generated in
        content/static_content. You could make this dynamic from a query
        or from a glob() style file matching.
    """
    return (
        'deployment',
        'development',
        'guide-aws-s3',
        'guide-cloudflare-pages',
        'install',
        'integration'
    )


urlpatterns = [

    distill_path('',
                 index_view,
                 name='index',
                 distill_file='index.html'),

    distill_path('<slug:page_name>.html',
                 yamlmd_page_view,
                 name='yamlmd_page',
                 distill_func=iter_yamlmd_pages),

]
