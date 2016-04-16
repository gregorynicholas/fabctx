# encoding: utf-8
"""
  fabctx.http
  ~~~~~~~~~~~

  fabric context helpers for http requests.


  :copyright: (c) gregorynicholas.
"""
from __future__ import unicode_literals
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
