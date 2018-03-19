Simple Django cookiecutter
==========================

*Warning: Upgraded to Django 2.x - for python 3 only!*

This cookiecutter has LDAP authentication configured - if you don't want it you need to remove the lines

```
from .ldap_conf import *
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    '{{cookiecutter.project_name}}.core.auth.NoLoginModelBackend',
)

```

from ``settings/base.py``

Other things that are used (and configured except the LDAP auth):

* Three different environments (dev - uat - prod) with different requirements and settings for each
* django-tables2 for nice tables
* django-filters for nice qs filtering
* django-crispy-forms for nice forms
* django-debug-toolbar configured for dev env
* django-reversion to enable change auditing
* django-compressor to combine and compress your static assets
* django-extensions to enable some useful functionality
* Werkzeug to run the dev server

I have some scripts to help me on Windows - but should work anywhere. The scripts are:

* dovenv.bat to enable the virtualenv and correctly set the settings (to the dev env ones)
* dj.bat to run python manage.py command (i.e run ``dj migrate`` for applying migrations)
* rsp.bat to run the runserver_plus command
* test.bat to run the test suite


Usage:

Install cookiecutter (https://github.com/audreyr/cookiecutter) to your global python packages
(or the virtualenv you are going to create). Then,

```
mkdir parent_folder
cd parent_folder
virtualenv venv
cookiecutter https://github.com/spapas/cookiecutter-django-starter

```

Now answer the questions - the most important is the project name (i.e project name) - it will dump your project there:

```
cd project_name
dovenv.bat
pip install -r requirements\dev.txt

```

Project is ready - from the same directory (where you run ``dovenv.bat``) run the following to also create your git repo:

```
git init
git add -A
git commit
git remote add origin http://...
git push origin master
```


Please notice that this project has been configured for usage in Greece. If you want to 
convert it to your language you should probably change the ``LANGUAGE_CODE`` and ``TIMEZONE`` in
settings.py and make some small changes to the templates.


