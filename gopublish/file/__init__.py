from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from future import standard_library

from gopublish.client import Client
from gopublish.exceptions import GopublishTokenMissingError

standard_library.install_aliases()


class FileClient(Client):
    """
    Manipulate files managed by Gopublish
    """

    def list(self):
        """
        List files published in Gopublish

        :rtype: list
        :return: List of files
        """

        body = {}
        return self._api_call("get", "list_files", body)['files']

    def search(self, file_name):
        """
        Launch a pull task

        :type file_name: str
        :param file_name: Either a file name, or a file UID

        :rtype: list
        :return: List of files matching the search
        """
        body = {"file": file_name}

        return self._api_call("get", "search", body, inline=True)['files']

    def publish(self, path, version=1, contact="", email="", token=""):
        """
        Launch a publish task

        :type path: str
        :param path: Path to the file to be published

        :type version: int
        :param version: Version of the file to publish

        :type contact: str
        :param contact: Contact email for this file

        :type email: str
        :param email: Contact email for notification when publication is done

        :type token: str
        :param token: You Gopublish token.

        :rtype: dict
        :return: Dictionnary containing the response
        """
        body = {"path": path, "version": version, "contact": contact, "email": email}
        auth = None
        if email:
            body['email'] = email

        if contact:
            body['contact'] = contact

        if token:
            body['token'] = token
        else:
            if os.getenv("GOPUBLISH_TOKEN"):
                body['token'] = os.getenv("GOPUBLISH_TOKEN")
            else:
                raise GopublishTokenMissingError("Missing token: either specify it with --token, or set it as GOPUBLISH_TOKEN in your environnment")

        return self._api_call("post", "publish_file", body, auth=auth)
