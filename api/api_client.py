from urllib.parse import urlencode

from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict


class APIClient:
    def __init__(self):
        self.base_url = None
        self.end_point = None
        self.content_type = None
        self.headers = {}
        self.auth = None
        self.params = None

    def addHeader(self, key, value):
        self.headers = CaseInsensitiveDict()
        self.headers[key] = value


    def addContentType(self, value):
        self.headers = CaseInsensitiveDict()
        self.headers['Content-Type'] = value

    def addBasicAuth(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def addBearerTokenAuth(self, accessToken):
        self.headers = CaseInsensitiveDict()
        self.headers['authorization'] = "Bearer {{ {0} }}".format(accessToken)

    def addParams(self, params):
        self.params = urlencode(params)



