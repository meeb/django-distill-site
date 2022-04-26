from django.shortcuts import render
from content.content import markdown_render, static_page_render
from content.models import Release, Stargazer


def index_view(request):
    return render(request, 'content/index.html', context={
        'intro': markdown_render('index-intro'),
        'how_it_works': markdown_render('index-how-it-works'),
        'latest_release': Release.get_latest(),
        'num_stargazers': Stargazer.objects.all().count(),
        'stargazers': Stargazer.objects.order_by('?')[:144]
    })


def install_view(request):
    return render(request, 'content/install.html', context={})


def integration_view(request):
    return render(request, 'content/integration.html', context={})


def deployment_view(request):
    return render(request, 'content/deployment.html', context={})


def yamlmd_page_view(request, page_name):
    header, content = static_page_render(page_name)
    return render(request, 'content/page.html', context={
        'header': header,
        'content': content
    })
