# encoding: utf-8
"""
  fabctx.ctx
  ~~~~~~~~~~

  short + sweet fabric context magic.


  :copyright: (c) gregorynicholas.
"""
from __future__ import unicode_literals
from pprint import pprint
from pprint import pformat
from os import environ
from os import path
from os import getcwd as os_getcwd
from fabric.api import env as fab_env
from fabric.api import run as run_remote
from fabric.api import local as run_local
from fabric.api import parallel
from fabric.api import hide
from fabric.api import sudo
from fabric.api import task
from fabric.context_managers import (
  prefix,
  quiet,
  shell_env,
  settings,
  hide)
from contextlib import contextmanager
from contextlib import nested

__all__ = [
  #: alias exporting common fabric task decorators, contextmanagers for a
  #: simple, one-stop-shop for writing tasks quickly, and moving on with our
  #: distateful code..

  #: contextmanagers..
  'contextmanager', 'nested',
  'prefix', 'quiet', 'shell_env', 'home', 'source', 'warn_only', 'hide',
  'settings',

  #: task method-decorators..
  'parallel', 'task', 'sudo',

  #: helper mehoods..
  'getenv', 'getenv_local', 'getenv_remote',
  'getenv_home_local', 'getenv_home_remote',
  'is_local_scope', 'is_remote_scope', 'get_scope',
]


def get_scope(scope=None, *args, **kwargs):
  #: TODO: look at the fab_env.host_string..
  if scope != None:
    return scope

  elif 'env_id' in fab_env:
    return fab_env.env_id

  else:
    return 'local'

def is_local_scope(scope=None, *args, **kwargs):
  #: TODO: look at the fab_env.host_string..
  scope = get_scope(scope=scope)
  if scope != None:
    return scope in ('local')
  return True

def is_remote_scope(scope=None, *args, **kwargs):
  #: TODO: look at the fab_env.host_string..
  scope = get_scope(scope=scope)
  if scope != None:
    return scope in ('remote')
  return True


def getenv(environment_var, default=None, scope=None, *args, **kwargs):
  if is_local_scope(scope=scope):
    return getenv_local(environment_var, default=default)
  else:
    return getenv_remote(environment_var, default=default)


def getenv_local(environment_var, default=None, *args, **kwargs):
  return environ.get(environment_var, default)

def getenv_remote(environment_var, default=None, *args, **kwargs):
  res = run_remote('echo -n ${}'.format(environment_var), warn_only=True)
  if res.return_code == 0:
    return res.stdout
  else:
    return default


def getenv_home_local():
  return getenv_local('HOME', default=path.expanduser('~'))

def getenv_home_remote(default=''):
  return getenv_remote('HOME', default=default)


def home(scope=None, *args, **kwargs):
  """
  method, returns string path to $HOME directory.

  :param scope: specify 'local', or 'remote'
  """
  with warn_only():
    with hide('running'):
      scope = get_scope(scope=scope)
      fn = getenv_home_local

      if scope != None:
        if scope = 'remote':
          fn = getenv_home_remote
      elif 'env_id' in fab_env and fab_env.env_id == 'remote':
        fn = getenv_home_remote

      return fn()


@contextmanager
def source(path, *args, **kwargs):
  """
  contextmanager, prefixes sub-commands to source the specified shell script.
  """
  # TODO: test if destination exists..
  with prefix('. {}'.format(path), *args, **kwargs):
    yield


@contextmanager
def warn_only(*args, **kwargs):
  """
  contextmanager, prefixes sub-commands with `settings(warn_only=True)`
  """
  with settings(warn_only=True, *args, **kwargs):
    yield
