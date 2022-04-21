from django_distill import distill_path
from .views import index_view


urlpatterns = [

    distill_path('',
                 index_view,
                 name='index',
                 distill_file='index.html'),

]
