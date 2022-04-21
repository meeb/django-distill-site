from django.urls import path, include
from django.contrib import admin


admin.site.site_title = 'Django Distill site admin'
admin.site.site_header = 'Django Distill site admin'


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('', include('content.urls')),

]
