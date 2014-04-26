#!/usr/bin/env python
"""
  fabctx
  ~~~~~~~~~~

  short + sweet context magic + helpers for fabric scripts.


    links
    `````

    * `docs <http://gregorynicholas.github.io/fabctx>`_
    * `source <http://github.com/gregorynicholas/fabctx>`_
    * `package <http://packages.python.org/fabctx>`_

"""
from setuptools import setup

__version__ = "0.0.1"

with open("requirements.txt", "r") as f:
  requires = f.readlines()


setup(
  name='fabctx',
  version=__version__,
  url='http://github.com/gregorynicholas/fabctx',
  license='MIT',
  author='gregorynicholas',
  author_email='gn@gregorynicholas.com',
  description=__doc__,
  zip_safe=False,
  platforms='any',
  install_requires=requires,
  packages=[
    'fabctx',
  ],
  dependency_links=[
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
