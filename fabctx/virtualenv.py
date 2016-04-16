# encoding: utf-8
"""
  fabctx.virtualenv
  ~~~~~~~~~~~~~~~~~

  fabric context helpers for virtualenv, virtualenvwrapper.


  :copyright: (c) gregorynicholas.
"""
from __future__ import unicode_literals
from fabctx import ctx


__all__ = [
  'workon_home', 'get_virtualenv_path',
  'prefix_workon', 'prefix_activate_virtualenv',
]


def workon_home(virtualenv_id, *args, **kwargs):
  with ctx.warn_only():
    with ctx.hide('running'):
      return ctx.getenv('WORKON_HOME', '$HOME/.virtualenvs')


def get_virtualenv_path(virtualenv_id, *args, **kwargs):
  with ctx.warn_only():
    with ctx.hide('running'):
      return '{}/{}'.format(workon_home, virtualenv_id)


@ctx.contextmanager
def prefix_workon(virtualenv_id, *args, **kwargs):
  with ctx.shell_env(WORKON_HOME=workon_home(virtualenv_id)):
    with ctx.source('/usr/local/bin/virtualenvwrapper.sh'):
      with ctx.prefix("workon {}".format(virtualenv_id)):
        yield


@ctx.contextmanager
def prefix_activate_virtualenv(*args, **kwargs):
  with ctx.prefix("source {}/bin/activate".format(workon_home(''))):
    yield
