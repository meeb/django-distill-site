from django.shortcuts import render
from content.markdown import render as markdown_render
from content.models import Release


def index_view(request):
    return render(request, 'content/index.html', context={
        'intro': markdown_render('index-intro'),
        'how_it_works': markdown_render('index-how-it-works'),
        'latest_release': Release.get_latest(),
    })


def install_view(request):
    return render(request, 'content/install.html', context={})


def integration_view(request):
    return render(request, 'content/integration.html', context={})


def deployment_view(request):
    return render(request, 'content/deployment.html', context={})


def development_view(request):
    return render(request, 'content/development.html', context={})
