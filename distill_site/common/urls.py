from django_distill import distill_path
from .views import favicon_view, robots_view, _headers_view, error404_view


app_name = 'common'


urlpatterns = [

    distill_path('favicon.ico',
                 favicon_view,
                 name='favicon'),

    distill_path('robots.txt',
                 robots_view,
                 name='robots'),

    distill_path('_headers',
                 _headers_view,
                 name='_headers'),

    distill_path('404.html',
                 error404_view,
                 name='error404',
                 distill_status_codes=(200, 404)),

]
