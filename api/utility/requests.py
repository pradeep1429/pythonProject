import json
from urllib.parse import urljoin

import requests

from api.api_client import APIClient


class Requests:

    @staticmethod
    def get(config: APIClient):
        url = urljoin(config.base_url, config.end_point)
        try:
            response = requests.get(url=url,
                                    headers=config.headers,
                                    params=config.params,
                                    auth=config.auth)
            return response
        except requests.exceptions.RequestException as e:
            raise e

    @staticmethod
    def post(config: APIClient,data=None):
        json_string = json.dumps(data)
        url = urljoin(config.base_url, config.end_point)
        try:

            response = requests.post(url=url,
                                     headers=config.headers,
                                     params=config.params,
                                     auth=config.auth,
                                     data=json_string
                                     )
            return response
        except requests.exceptions.RequestException as e:
            return e

    # Add more methods as per the requirement: PUT, DELETE etc.