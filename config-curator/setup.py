#!/usr/bin/env python3

from setuptools import setup
from config_curator.contractor.client import __VERSION__

setup( name='config-curator',
       version=__VERSION__,
       description='Config Curator - pulls config values from contractor, merges with templates, writes config files',
       author='Peter Howe',
       author_email='pnhowe@gmail.com',
       url='https://github.com/t3kton/disks',
       python_requires='~=3.8',
       license='Apache2',
       classifiers=[
           'Development Status :: 5 - Production/Stable',
           'Intended Audience :: System Administrators',
           'License :: OSI Approved :: Apache Software License',
           'Programming Language :: Python :: 3',
       ],
       packages=[ 'config_curator', 'config_curator.contractor', 'libconfig', 'libconfig.jinja2', 'libconfig.markupsafe' ],
       )
