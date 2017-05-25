# -*- coding: utf-8 -*-

import logging
import re
from xml.etree import ElementTree
import time
from tqdm import tqdm
from urllib.parse import urlparse, urljoin
import os

import attr
import grequests
import requests as r

from cached_property import cached_property
from structlog import configure, get_logger
from structlog.stdlib import LoggerFactory


logging.basicConfig()
configure(logger_factory=LoggerFactory())
logger = get_logger(__name__)


@attr.s
class Funk:

    sitemap_url = attr.ib()

    _concurrent = attr.ib(default=None)
    _verify_ssl = attr.ib(default=True)
    _verify_response = attr.ib(default=False)
    _force_https = attr.ib(default=None)
    _replace = attr.ib(default=None)
    _session = attr.ib(init=False, repr=None)
    _results = attr.ib(default=attr.Factory(list), repr=None)
    _timeout = attr.ib(default=0)
    _progress = attr.ib(default=False)

    def __attrs_post_init__(self):
        self._session = r.Session()

    def _get_sitemap(self):
        sitemap = r.get(self.sitemap_url)
        if sitemap.status_code != 200:
            self.log.error("could not get sitemap")
            sitemap.sitemap.raise_for_status()
        return sitemap

    @staticmethod
    def _parse_sitemap(sitemap):
        regex = re.compile(r'\{(.+)\}')
        fstr = './/sitemap:url/sitemap:loc'

        tree = ElementTree.fromstring(sitemap.content)
        # retrieve xmlns
        ns = regex.search(tree.tag).group(1)
        namespaces = dict(sitemap=ns)
        locations = [str(l.text) for l in tree.findall(fstr, namespaces)]
        return locations

    @staticmethod
    def _has_netloc(url):
        return bool(urlparse(url).netloc)

    @cached_property
    def _urls(self):
        return self._parse_sitemap(self._get_sitemap())

    @cached_property
    def _base_url(self):
        return os.path.dirname(self.sitemap_url)

    def _get(self, url):
        if self._force_https:
            url = url.replace('http', 'https')
        resp = self._session.get(url, allow_redirects=False, verify=self._verify_ssl)
        if resp.status_code in (301, 302):
            redirect = resp.headers.get('Location')
            if not self._has_netloc(redirect):
                self._session.get(urljoin(self._base_url, redirect))

    def run(self):
        if self._concurrent:
            rs = (grequests.get(u) for u in self._urls)
            self._results = list(grequests.imap(rs))
        else:
            for u in tqdm(self._urls):
                self._results.append(self._get(u))

    def dry_run(self):
        raise NotImplemented
