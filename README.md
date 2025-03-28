Simple Django cookiecutter
==========================

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
* django-hijack to allow superusers to hijaco other users
* Werkzeug to run the dev server
* Custom User model with login/logout pages
* Bootstrap 5 templates
* Usage of thread locals to retrieve request (and user)
* An abstract model that saves created/modified datetime and user.
* Upgraded to Django 5.1 and all latest packages

I have some scripts to help me on Windows - but should work anywhere. The scripts are:

* dovenv.bat to enable the virtualenv and correctly set the settings (to the dev env ones)
* dj.bat to run python manage.py command (i.e run ``dj migrate`` for applying migrations)
* rsp.bat to run the runserver_plus command
* test.bat to run the test suite


Usage
-----

Install cookiecutter (https://github.com/audreyr/cookiecutter) to your global python packages
(or the virtualenv you are going to create -- also checkout my post @ https://spapas.github.io/2017/12/20/python-2-3-windows/ for using python 2 and 3 on windows). Then, activate your venv and run cookiecutter with this repo, i.e

```
mkdir parent_folder
cd parent_folder
py -3 -m venv venv 
pip install cookiecutter
cookiecutter https://github.com/spapas/cookiecutter-django-starter

```

Now answer the questions - the most important is the project name (i.e project name) - it will dump your project there:

```
cd project_name
dovenv.bat
pip install -r requirements\dev.txt
```

If you see ldap-related errors then install correct version of python-ldap from https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap (download it and run ``pip install python_ldap-xxx.whl``) - then run again ``pip install -r requrements\dev.txt``).

If you see rcssmin related errors then install it like this: ``pip install -U rcssmin --install-option="--without-c-extensions"``

Project is ready - from the same directory (where you run ``dovenv.bat``) run the following to also create your git repo (a proper .gitignore is alreadt provided courtesy of https://gitignore.io and some additions of mine):

```
git init
git add -A
git commit
git remote add origin http://...
git push origin master
```

Now you can run the migrations, create your superuser and run the dev server:

```
dj migrate
dj createsuperuser
rsp
```

Please notice that this project has been configured for usage in Greece. If you want to 
convert it to your language you should probably change the ``LANGUAGE_CODE`` and ``TIMEZONE`` in
settings.py and make some small changes to the templates.


### The fabric situation

Please notice that I've included a fabric 1.x script for e-z deploy. For reasons that I don't want to explain here I won't support fabric 2.x. To use that fabric script you'll need to use the life saving fab-classic project (https://ploxiln.github.io/fab-classic/) that is a fork of fabric 1.x properly supporting ypthon 3.x! This dependency is already installed with the requirements/dev.txt.

### Removing LDAP

If you don't want to use LDAP remove the ldap-related requirements from requirements/base.txt, remove the ldap_conf.py file from settings, remove the line importing ldap_conf from settings/base.py and either change your AUTHENTICATION_BACKEDS to your liking or completely remove that line from base.py and dev.py to fallback to model authentication.
