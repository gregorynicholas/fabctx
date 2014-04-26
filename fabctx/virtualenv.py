"""
  fabctx.virtualenv
  ~~~~~~~~~~~~~~~~~

  context magic for virtualenv + virtualenvwrapper.

"""
import os
from fabric.api import env
from fabctx import ctx

__all__ = [
  'venv_path', 'workon', 'activate_venv',
]


def venv_path(workon_id):
  with ctx.quiet():
    if env.env_id in ('local', 'test'):
      return os.getenv('VIRTUAL_ENV', '')
    else:
      return "{}/.virtualenvs/{}".format(ctx.home(), workon_id)


@ctx.contextmanager
def workon(workon_id):
  with ctx.shell_env(WORKON_HOME=venv_path(workon_id)):
    with ctx.source('/usr/local/bin/virtualenvwrapper.sh'):
      with ctx.prefix("workon {}".format(workon_id)):
        yield


@ctx.contextmanager
def activate_venv():
  with ctx.prefix("source {}/bin/activate".format(venv_path(''))):
    yield
