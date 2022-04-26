from django_distill import distill_path
from .views import index_view, yamlmd_page_view


app_name = 'content'


urlpatterns = [

    distill_path('',
                 index_view,
                 name='index',
                 distill_file='index.html'),

    distill_path('<slug:page_name>.html',
                 yamlmd_page_view,
                 name='yamlmd_page'),

]
