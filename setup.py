#!/usr/bin/env python
"""
  fabctx
  ``````

  short + sweet context magic and helpers for fabric projects.



  links:
  ``````
  * `docs: <http://gregorynicholas.github.io/fabctx>`_
  * `source (github): <http://github.com/gregorynicholas/fabctx>`_
  * `package (pypi): <http://packages.python.org/fabctx>`_
  * `build (travis-ci): <http://travis-ci.org/gregorynicholas/fabctx>`_
  * `issues: <http://github.com/gregorynicholas/fabctx/issues>`_
  * `development version: <http://github.com/gregorynicholas/fabctx/zipball/master#egg=fabctx-dev>`_

"""
try:
  import multiprocessing
except ImportError:
  pass

try:
  from setuptools import setup
except ImportError:
  from ez_setup import use_setuptools
  use_setuptools()
  from setuptools import setup
import setup_utils as sutils


root = 'fabctx'
name = sutils.parse_project_name(root, __doc__)
version = sutils.parse_version(root)


setup(
  name=name,
  version=version,
  url=sutils.parse_homepage(root),
  author=sutils.parse_author(root),
  author_email=sutils.parse_author_email(root),
  description='short + sweet context magic and helpers for fabric ' +
  'projects.',
  long_description=__doc__,

  install_requires=sutils.parse_requirements(),
  scripts=[],
  packages=sutils.find_packages(),
  namespace_packages=[],

  py_modules=[],

  test_suite='nose.collector',
  tests_require=[
    'nose>=1.3.7',
    'nose-cov>=1.6',
    'cov-core==1.15.0',
    'mock>=2.0.0',
    'coverage==4.0.3',
    'coveralls==1.1',
    'pbr>=1.9.1',
    'funcsigs>=1.0.0',
    'ordereddict>=1.1',
    'docopt>=0.6.2',
  ],

  include_package_data=True,
  package_data={'': ['*.txt', '*.cfg', '*.md', '*.yml', '*.yaml']},

  cmdclass = {
    "publish" : sutils.PypiPublish,
    "runtests" : sutils.RunTests,
    "build_sphinx" : sutils.BuildSphinx,
  },

  #: these are optional and override docs.conf.py settings..
  command_options={
    'build_sphinx': {
      'project': ('setup.py', name),
      'version': ('setup.py', version),
      'release': ('setup.py', sutils.parse_release(root)),
      'config-dir': ('setup.py', './docs/'),
    },
  },

  dependency_links=[],
  zip_safe=False,
  license='MIT',
  platforms=['any'],
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
