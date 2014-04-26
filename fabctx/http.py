"""
  fabctx.http
  ~~~~~~~~~~~

  context magic for http.

"""
import requests
import simplejson as json

__all__ = ['post']


def post(url, payload):
  """
  make an http post
  """
  return requests.post(
    url=url,
    headers={'content-type': 'application/json'},
    data=json.dumps(payload),
  )
