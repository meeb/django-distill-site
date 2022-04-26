Once you have 
[<i class="fa-solid fa-fw fa-file-import"></i> installed](/install.html)
**django-distill** into your Django project you just
wrap the URLs you want to generate static pages for by replacing Django's
`django.urls.path()` with `django_distill.distill_path()`:

    from django_distill import distill_path
    from app.views import page_view

    urlpatterns = [
        # Wrap your URL with distill_path() instead of path()
        distill_path('page.html',
                     page_view,
                     name='page'),
    ]

And you're done! You can now generate `page.html` as a static page with the
`distill-local` Django command:

    $ python manage.py distill-local /path/to/output/directory

There's support for pages with parameters using a URL generator, generating
a subset of files from models, renaming files, publishing to CDNs and much
more is detailed in the
[<i class="fa-solid fa-fw fa-book-open-reader"></i> integration](/integration.html)
and
[<i class="fa-solid fa-fw fa-cloud-arrow-up"></i> deployment](/deployment.html)
documentation.
