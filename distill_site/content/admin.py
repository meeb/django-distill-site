from django.contrib import admin
from .models import Stargazer, Release


@admin.register(Stargazer)
class StargazerAdmin(admin.ModelAdmin):

    ordering = ('name',)
    list_display = ('name', 'id', 'url')
    search_fields = ('id', 'name')


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):

    ordering = ('-published',)
    list_display = ('version', 'published', 'url')
    search_fields = ('version',)
