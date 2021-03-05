from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from gopublish.exceptions import GopublishConnectionError
from gopublish.file import FileClient

from future import standard_library

import requests

standard_library.install_aliases()


class GopublishInstance(object):

    def __init__(self, host="localhost", port="9100", **kwargs):
        self.host = host
        self.port = str(port)

        self.endpoints = self._get_endpoints()

        # Initialize Clients
        args = (self.host, self.port, self.login, self.password, self.endpoints)
        self.file = FileClient(*args)

    def __str__(self):
        return '<GopublishInstance at {}:{}>'.format(self.host, self.port)

    def _get_endpoints(self):

        try:
            r = requests.get("http://{}:{}/api/endpoints".format(self.host, self.port))
            if not r.status_code == 200:
                raise requests.exceptions.RequestException
            return r.json()
        except requests.exceptions.RequestException:
            raise GopublishConnectionError("Cannot connect to {}:{}. Please check the connection.".format(self.host, self.port))

