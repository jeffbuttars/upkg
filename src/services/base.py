import logging
logger = logging.getLogger('upkg')

import os
import json
from pprint import pformat as pf
import tornado
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient, HTTPClient as SyncHttpClient
from tornado.httputil import url_concat

import services


class ServiceBase(object):

    api_ver = '1'
    api_base_url = 'https://example.com/api/v' + api_ver
    name = 'service_base'

    def __init__(self, api_ver=None, api_base_url=None,
                 http_client_args=[], http_client_kwargs={}
                 ):
        """todo: to be defined

        :param api_ver: arg description
        :type api_ver: type description
        :param api_base_url: arg description
        :type api_base_url: type description
        """
        logger.debug("initializing %s service", self.name)

        self._api_ver = api_ver or ''
        self._api_base_url = api_base_url or ''

        self._default_headers = {}

        self._ioloop = tornado.ioloop.IOLoop.current()

        if self._ioloop._running:
            self._hc = AsyncHTTPClient(*http_client_args, **http_client_kwargs)
        else:
            self._hc = SyncHttpClient(*http_client_args, **http_client_kwargs)
    #__init__()

    def __str__(self):
        """todo: Docstring for __str__
        :return:
        :rtype:
        """
        return self.name
    #__str__()

    def search(self, term):
        """todo: Docstring for search

        :param term: arg description
        :type term: type description
        :return:
        :rtype:
        """
        raise NotImplemented("You must override the search method.")
    #search()

    def get(self, ep, params=None, **kwargs):
        """todo: Docstring for get

        :param ep: arg description
        :type ep: type description
        :param params: arg description
        :type params: type description
        :return:
        :rtype:
        """

        url = os.path.join(self._api_base_url, ep)
        if params:
            url = url_concat(url, params)

        headers = self._default_headers.copy()
        kwargs = kwargs or {}

        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers

        logger.debug("GET ing %s %s", url, kwargs)
        return self._hc.fetch(url, method='GET', **kwargs)
    #get()

    def get_json(self, *args, **kwargs):
        """todo: Docstring for get_json

        :param *args: arg description
        :type *args: type description
        :param **kwargs: arg description
        :type **kwargs: type description
        :return:
        :rtype:
        """

        resp = self.get(*args, **kwargs)

        return json.loads(resp.body.decode("utf-8"))
    #get_json()
#ServiceBase


class ServiceResponse(object):
    def __init__(self, service, resp_dict):
        """todo: to be defined

        :param resp_dict: arg description
        :type resp_dict: type description
        """
        self._resp_dict = resp_dict
        self.name = "N/A"
        self.url = "N/A"

        for k, v in resp_dict.items():
            setattr(self, k, v)
        # end for k, v in resp_dict
    #__init__()

    def __str__(self):
        """todo: Docstring for __str__
        :return:
        :rtype:
        """
        resp = ("{} {}").format(self.name, self.url)

        return resp
    #__str__()

    def __repr__(self):
        """todo: Docstring for __repr__
        :return:
        :rtype:
        """
        return self.__str__()
    #__repr__()
#ServiceResponse
