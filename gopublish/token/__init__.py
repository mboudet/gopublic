from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import getpass

from future import standard_library

from gopublish.client import Client

standard_library.install_aliases()


class TokenClient(Client):
    """
    Manipulate files managed by Gopublish
    """

    def get(self, username):
        """
        Get token

        :type username: str
        :param username: Username

        :rtype: dict
        :return: Dictionary containing the token
        """

        if self.gopublish_mode == "prod":
            try:
                password = getpass.getpass(prompt='Enter your GenOuest password ')
            except Exception as error:
                print('Error', error)
        else:
            password = username

        body = {"username": username, "password": password}

        return self._api_call("post", "create_token", body)

    def revoke(self, token):
        """
        Revoke a token

        :type token: str
        :param token: The token

        :rtype: dict
        :return: The API response
        """
        body = {"token": token}

        return self._api_call("delete", "revoke_token", body)

