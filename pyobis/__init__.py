# -*- coding: utf-8 -*-

# pyobis

'''
pyobis library
~~~~~~~~~~~~~~~~~~~~~

pyobis is a Python client for OBIS.

Example usage:

# Import entire library
import pyobis
# or import modules as needed
## occurrence
from pyobis import occurrence
## taxa
from pyobis import taxa
## eez
from pyobis import eez

## use advanced logging
### setup first
import requests
import logging
import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
### then make request
from pyobis import occurrence
occurrence.search(geometry='POLYGON((30.1 10.1, 10 20, 20 40, 40 40, 30.1 10.1))', limit=20)
'''

__version__ = '0.0.2.9000'
__title__ = 'pyobis'
__author__ = 'Scott Chamberlain'
__license__ = 'MIT'

from .occurrences import search
from .taxon import search
