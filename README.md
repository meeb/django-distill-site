# django-distill-site

Django powered website for [django-distill.com](https://django-distill.com/)
using
[django-distill](https://github.com/meeb/django-distill) to output the sites
static HTML. The site is automatically built by Cloudflare Pages and deployed
to the Cloudflare CDN.

Various helper commands are available via the
[Makefile](https://github.com/meeb/django-distill-site/blob/main/Makefile).

Requirements are modern Python3 and pipenv.

Clone the repo and install the dependancies with:

    $ pipenv shell && pipenv install

To run the Django development server use

    $ make dev

Note that `make sync` requires a valid GitHib API key to be set in
`settings.py`.

The
[runtime.txt](https://github.com/meeb/django-distill-site/blob/main/runtime.txt)
file specifies the Python runtime to be used by the Cloudflare Pages runner
when the site is built.

This site is quite over-engineered for a small static website. This is by
design to showcase how you can use Django with static content, databases and
the CMS with static site generation.
