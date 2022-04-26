from django_distill import distill_path
from .views import (index_view, install_view, integration_view,
                    deployment_view, yamlmd_page_view)


app_name = 'content'


urlpatterns = [

    distill_path('',
                 index_view,
                 name='index',
                 distill_file='index.html'),

    distill_path('install.html',
                 install_view,
                 name='install'),

    distill_path('integration.html',
                 integration_view,
                 name='integration'),

    distill_path('deployment.html',
                 deployment_view,
                 name='deployment'),

    distill_path('<slug:page_name>.html',
                 yamlmd_page_view,
                 name='yamlmd_page'),

]
