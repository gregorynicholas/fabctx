"""
  fabctx.ctx
  ~~~~~~~~~~

  short + sweet fabric context magic.

"""
import os
from contextlib import contextmanager
from fabric.api import env, run
from fabric.context_managers import prefix, quiet, shell_env, settings

__all__ = [
  'contextmanager', 'prefix', 'quiet', 'shell_env', 'home', 'source',
  'warn_only',
]


def home():
  """
  returns string path to home directory.
  """
  with quiet():
    if env.env_id is 'local':
      return os.getenv('HOME', '')
    else:
      return run('echo $HOME', warn_only=True)


@contextmanager
def source(path):
  """
  prefix a command with sourcing a file path.
  """
  with prefix('source {}'.format(path)):
    yield


@contextmanager
def warn_only():
  with settings(warn_only=True):
    yield
