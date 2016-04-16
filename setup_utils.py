# encoding: utf-8
"""
  setup_helpers
  ~~~~~~~~~~~~~

  util methods for python package setup.


  :copyright: (c) gregorynicholas.
"""
from __future__ import unicode_literals
import re
import codecs
import fnmatch as fm
from os import path
from os import listdir
try:
  from setuptools import setup
  from setuptools import find_packages
  from setuptools import Command
except ImportError:
  from ez_setup import use_setuptools
  use_setuptools()
  from setuptools import setup, find_packages, Command
from sphinx.setup_command import BuildDoc as BuildSphinx


__all__ = [
  'parse_project_name',
  'parse_version',
  'parse_release',
  'parse_author',
  'parse_author_email',

  'PypiPublish',
  'RunTests',
  'BuildSphinx',

  'find_packages',
]


def parse_project_name(root, doc):
  o = doc.strip().split('\n')[0]
  return o

def parse_version(root):
  with open(root + '/__init__.py', 'r') as f:
    o = re.findall(r'__version__\s*=\s*\'(.*)\'', f.read())
    return o[0]

def parse_release(root):
  with open(root + '/__init__.py', 'r') as f:
    o = re.findall(r'__release__\s*=\s*\'(.*)\'', f.read())
    return o[0]

def parse_author(root):
  with open(root + '/__init__.py', 'r') as f:
    o = re.findall(r'__author__\s*=\s*\'(.*)\'', f.read())
    return o[0]

def parse_author_email(root):
  with open(root + '/__init__.py', 'r') as f:
    o = re.findall(r'__author_email__\s*=\s*\'(.*)\'', f.read())
    return o[0]

def parse_homepage(root):
  with open(root + '/__init__.py', 'r') as f:
    o = re.findall(r'__homepage__\s*=\s*\'(.*)\'', f.read())
    return o[0]

def parse_requirements():
  with open('requirements.txt', 'r') as f:
    requires = f.read().strip()
    requires = requires.split('\n')


class PypiPublish(Command):
  description = "publishes a package to the pypi."
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    """
    publishes package to the pypi
    """
    from os import system
    system("python setup.py --verbose runtests")
    system("python setup.py --verbose sdist")
    system("python setup.py --verbose register --show-response")
    system("python setup.py --verbose upload --show-response")
    system("python setup.py --verbose upload_docs --show-response")


class RunTests(Command):
  description = "runs the nosetests runner."
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    """
    runs the nosetests runner
    """
    from os import system
    system("python setup.py --verbose clean --all")
    system("python setup.py --verbose check --metadata --strict")
    system("python setup.py --verbose check --restructuredtext")
    system("python setup.py --verbose build  --force")
    system("python setup.py --verbose build_scripts --force")
    system("python setup.py nosetests --config nose-local.cfg")
