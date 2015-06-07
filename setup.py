#!/usr/bin/env python
"""
  fabctx
  ~~~~~~

  short + sweet context magic + helpers for fabric scripts.


    links
    `````

    * `docs <http://gregorynicholas.github.io/fabctx>`_
    * `source <http://github.com/gregorynicholas/fabctx>`_
    * `package <http://packages.python.org/fabctx>`_

"""
try:
  import multiprocessing
except ImportError:
  pass
from setuptools import setup


# parse version number
with open('fabctx/__init__.py') as f:
  m = re.findall(r'__version__\s*=\s*\'(.*)\'', f.read())
  version = m[0]


setup(
  name='fabctx',
  version=version,
  url='http://github.com/gregorynicholas/fabctx',
  license='MIT',
  author='gregorynicholas',
  author_email='gn@gregorynicholas.com',
  description=__doc__,
  zip_safe=False,
  platforms='any',
  install_requires=[
    'fabric==1.6.1',
    'requests==2.0.1',
    'simplejson==2.6.2',
  ],
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
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ]
)
