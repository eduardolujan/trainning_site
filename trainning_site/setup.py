#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='trainning_site',
    version='1.0',
    description="",
    author="Lincoln Loop",
    author_email='info@lincolnloop.com',
    url='',
    packages=find_packages(),
    package_data={'trainning_site': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
