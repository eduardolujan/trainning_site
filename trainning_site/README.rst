.. 

Trainning Site
======================


Sitio de Administracion de Bujutsu.tv
----------

Quickstart
----------

To bootstrap the project::

    virtualenv trainning_site
    source trainning_site/bin/activate
    cd path/to/trainning_site/repository
    pip install -r requirements.pip
    pip install -e .
    cp trainning_site/settings/local.py.example trainning_site/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
