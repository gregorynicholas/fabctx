#!/usr/bin/env python
"""
fabctx
``````

short + sweet context magic + helpers for fabric scripts.


links:
``````
* `docs: <http://gregorynicholas.github.io/fabctx>`_
* `source: <http://github.com/gregorynicholas/fabctx>`_
* `package: <http://packages.python.org/fabctx>`_
* `travis-ci: <http://travis-ci.org/gregorynicholas/fabctx>`_
* `issues: <http://github.com/gregorynicholas/fabctx/issues>`_
* `development version: <http://github.com/gregorynicholas/fabctx/zipball/master#egg=fabctx-dev>`_

"""
try:
  import multiprocessing
except ImportError:
  pass

try:
  from setuptools import setup
  from setuptools import find_packages
except ImportError:
  from distutils.core import setup

from os import path, listdir
import fnmatch as fm
import re


# parse version number
with open('fabctx/__init__.py', 'r') as f:
  v = re.findall(r'__version__\s*=\s*\'(.*)\'', f.read())
  __version__ = v[0]

with open("requirements.txt", "r") as f:
  requires = f.readlines()


setup(
  name='fabctx',
  version=__version__,
  url='http://github.com/gregorynicholas/fabctx',
  author='gregorynicholas',
  author_email='gn@gregorynicholas.com',

  description='short + sweet context magic + helpers for fabric scripts.',
  long_description=__doc__,

  install_requires=requires,

  scripts=[
  ],

  packages=find_packages(),

  namespace_packages=[
  ],

  py_modules=[
  ],

  test_suite='nose.collector',
  tests_require=[
    'nose==1.3.7',
    'nose-cov==1.7',
    'mock==1.0.1',
  ],

  include_package_data=True,
  package_data={'': ['*.txt', '*.cfg', '*.md', '*.yml', '*.yaml']},

  dependency_links = [
  ],
  license='MIT',
  zip_safe=False,
  platforms='any',
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
  ]
)
