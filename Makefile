python=/usr/bin/env python


all: clean build


dev:
	$(python) distill_site/manage.py runserver


build:
	touch distill_site/distill_site/local_settings.py
	mkdir -p docs
	mkdir -p distill_site/media
	mkdir -p distill_site/static
	$(python) distill_site/manage.py collectstatic --noinput
	$(python) distill_site/manage.py distill-local --force docs
	cp -av distill_site/media docs/media


clean:
	rm -rf docs
	rm -rf distill_site/static


test:
	cd distill_site && $(python) manage.py test --verbosity=2 && cd ..


sync:
	$(python) distill_site/manage.py sync_pypi_releases
	$(python) distill_site/manage.py sync_github_stargazers
