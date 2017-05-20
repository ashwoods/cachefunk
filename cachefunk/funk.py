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
    _results = attr.ib(default=attr.Factory(list))

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
    def has_netloc(url):
        return bool(urlparse(url).netloc)

    @cached_property
    def urls(self):
        return self._parse_sitemap(self._get_sitemap())

    @cached_property
    def base_url(self):
        return os.path.dirname(self.sitemap_url)

    def list_urls(self):
        raise NotImplemented

    def dry_run(self):
        raise NotImplemented

    def run(self, concurrent=False, verify_ssl=True, force_https=False):
        if concurrent:
            rs = (grequests.get(u) for u in self.urls)
            self._results = list(grequests.imap(rs))
        else:
            s = r.Session()
            for u in tqdm(self.urls):
                if force_https:
                    u = u.replace('http', 'https')
                resp = s.get(u, allow_redirects=False, verify=verify_ssl)
                if resp.status_code in (301, 302):
                    redirect = resp.headers.get('Location')
                    if not self.has_netloc(redirect):
                        s.get(urljoin(self.base_url, redirect))
                self._results.append(s.get(u, allow_redirects=False))
