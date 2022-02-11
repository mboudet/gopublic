from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

from future import standard_library

from gopublic.golib.client import Client
from gopublic.golib.exceptions import GopublishTokenMissingError

standard_library.install_aliases()


class FileClient(Client):
    """
    Manipulate files managed by Gopublish
    """

    def list(self, tags="", limit=None, offset=None):
        """
        List files published in Gopublish

        :type tags: str
        :param tags: Comma-separated tags

        :type limit: int
        :param limit: Limit the results numbers

        :type offset: int
        :param offset: Offset for listing the results (used with limit)

        :rtype: dict
        :return: Dict with files and total count
        """

        body = {}

        tags = self._parse_input_values(tags, "Tags")
        if tags:
            body['tags'] = tags

        if offset and not limit:
            offset = None
        if limit:
            body['limit'] = limit
        if offset:
            body['offset'] = offset

        return self._api_call("get", "list_files", body, inline=True)

    def search(self, file_name, tags="", limit=None, offset=None):
        """
        Launch a pull task

        :type file_name: str
        :param file_name: Either a file name, or a file UID

        :type tags: str
        :param tags: Comma-separated tags

        :type limit: int
        :param limit: Limit the results numbers

        :type offset: int
        :param offset: Offset for listing the results (used with limit)

        :rtype: dict
        :return: Dict with files and total count
        """
        body = {"file": file_name}

        tags = self._parse_input_values(tags, "Tags")

        if offset and not limit:
            offset = None
        if limit:
            body['limit'] = limit
        if offset:
            body['offset'] = offset

        if tags:
            body['tags'] = tags

        return self._api_call("get", "search", body, inline=True)

    def publish(self, path, tags="", linked_to="", contact="", email="", token=""):
        """
        Launch a publish task

        :type path: str
        :param path: Path to the file to be published

        :type tags: str
        :param tags: Comma-separated tags

        :type linked_to: str
        :param linked_to: id of the original file this file is a version of

        :type contact: str
        :param contact: Contact email for this file

        :type email: str
        :param email: Contact email for notification when publication is done

        :type token: str
        :param token: Your Gopublish token.

        :rtype: dict
        :return: Dictionnary containing the response
        """

        body = {"path": path}
        if email:
            body['email'] = email

        if contact:
            body['contact'] = contact

        tags = self._parse_input_values(tags, "Tags")
        if tags:
            body['tags'] = tags

        if linked_to:
            body['linked_to'] = linked_to

        if not token:
            if os.getenv("GOPUBLISH_TOKEN"):
                token = os.getenv("GOPUBLISH_TOKEN")
            else:
                raise GopublishTokenMissingError("Missing token: either specify it with --token, or set it as GOPUBLISH_TOKEN in your environnment")
        headers = {"X-Auth-Token": "Bearer " + token}

        return self._api_call("post", "publish_file", body, headers=headers)
