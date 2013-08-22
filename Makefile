MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=app.settings $(MANAGE) test app

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=app.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=app.settings $(MANAGE) syncdb --noinput
