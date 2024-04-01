import json
import os
from json import loads
from urllib.parse import urlencode

import jsonschema
import requests
from bs4 import BeautifulSoup
from deepdiff import DeepDiff
from icecream import ic
from requests.auth import HTTPBasicAuth

from api.utility.requests import Requests


class TestSample:

    __access_token = "Bearer token"

    def test_get_validate_status_code_200(self,api_client):
        api_client.end_point = "api/products/2"
        api_client.headers = {}
        response = Requests.get(api_client)
        print(response.status_code)
        print(type(loads(response.text)))
        print(type(json.dumps(response.json(), indent=2)))



    def test_get_query_params(self,api_client):
        api_client.end_point = "api/users"
        api_client.headers = {}
        api_client.params = {'page': '2'}
        response = Requests.get(api_client)
        print(response.json())

    def test_session_cookie(self,api_client):
        session = requests.Session()
        print(session.cookies.get_dict())  # {}
        print('-' * 50)
        session.get('http://google.com')
        print(session.cookies.get_dict())
        print('-' * 50)
        api_client.base_url = "https://www.google.com"
        api_client.headers = {}
        response = Requests.get(api_client)
        print(response.cookies.get_dict())
        with open('cookies.txt', 'w', encoding='utf-8') as f:
            json.dump(requests.utils.dict_from_cookiejar(response.cookies),f)

    def test_send_cookies_with_request(self):
        session = requests.Session()
        response = session.get(
            'https://httpbin.org/cookies',
            cookies={'my-cookie': 'my-value'}
        )
        print(response.json())


    def test_access_token(self,api_client):
        api_client.base_url = "https://api.github.com"
        api_client.end_point = "/users/pradeep1429/repos"
        api_client.addHeader("authorization",self.__access_token)
        response = Requests.get(api_client)
        #ic(response.json())
        repo = os.path.abspath(os.path.pardir+"\\repos.json")
        with open(repo) as r:
            json_data = r.read()
        actual_data = response.json()
        if DeepDiff(json.loads(json_data), actual_data, ignore_order=True):
            ic("json response is valid")
        else:
            ic("json response is not same")
        with open(os.path.abspath(os.path.pardir + "\\schema.json")) as schma:
            schema = schma.read()
        jsonschema.validate(instance=response.text, schema=(schema))


    def test_session_access(self,api_client):
        api_client.base_url = "https://api.github.com"
        api_client.end_point = "/user/emails"
        api_client.addHeader("authorization", self.__access_token)
        response = Requests.get(api_client)
        ic(response.headers)
        ic(f"response from requests:\n{response.json()}")
        ic(response.status_code)
        session = requests.Session()
        url = "https://api.github.com/user/emails"
        session.headers.update({'authorization': self.__access_token})
        headers = {"Authorization": self.__access_token}
        response = session.get(url,headers=session.headers)
        ic(response.status_code)
        ic(f"response from sessions: \n{response.json()}")


    def test_bearer_token(self,api_client):
        # api_client.base_url = "https://www.codechef.com"
        # api_client.end_point = "/"
        # auth = HTTPBasicAuth("pradeep555593","Willchange@1")
        # headers = {"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9,"
        #                              "eyJpc3MiOiJjb2RlY2hlZi5jb20iLCJzdWIiOiI0NDE3MTMxIiwidXNlcm5hbWUiOiJwcmFkZWVwNTU1NTkzIiwiaWF0IjoxNzA4MDg1NzM1LCJuYmYiOjE3MDgwODU3MzUsImV4cCI6MTcxMDA4MDEzNX0,"
        #                              "euiW8_pzd0DNaS4LL0UmdlEcx9OObBDcqVkG2iClz_s"}
        # response = requests.post("https://www.codechef.com/api/codechef/login",auth=auth,headers=headers)
        # ic(response.status_code)

        login_data = {
            'username': 'pradeep555593',
            'password': 'Willchange@1',
            'form_build_id' : 'new_login_form',
            'csrf_token': 'token'
        }
        headers = {'Content-Type':'application/json'}
        with requests.Session() as session:
            url = "https://www.codechef.com/login"
            response = session.get(url, headers=headers)
            ic(session.cookies)
            soup = BeautifulSoup(response.content,'html5lib')
            login_data['form_build_id'] = soup.find('input', attrs={'name':'form_build_id'})['value']
            login_data['csrf_token'] = soup.find('input', attrs={'name':'csrfToken'})['value']
            encode_data = urlencode(login_data)
            ic(encode_data)
            response = session.post("https://www.codechef.com", data=encode_data, headers=headers)
            ic(login_data)
            ic(response.status_code)
            ic(session.cookies)
            ic(response.content)

    def test_session_login(self):
        s = requests.Session()
        url = "http://localhost:8080"
        s.auth = HTTPBasicAuth("admin", "token")
        response = s.post(url)
        ic(response.text)
        crumb_response = s.get(f"{url}/crumbIssuer/api/json")
        ic(crumb_response.json())
        s.headers.update({'Jenkins-Crumb': crumb_response.json().get('crumb')})
        ic(s.headers)
        ic(response.cookies.get_dict())
        ic(response.status_code)
        if(response.text.__contains__("python_project")):
            ic("login success")
        else:
            ic("login failed")

    def test_multiple_user_agent(self):
        cookies = {'JSESSIONID.939ded21': 'node01o5tmq9pb1vz8ypo628o7fd235.node0'}
        response = requests.get("http://localhost:8080/job/python_project/", cookies=cookies)
        print(response.text)
        if (response.text.__contains__("python_project")):
            ic("login success")
        else:
            ic("login failed")

    def test_cookie_login(self):
        cookie = {'SESS93b6022d778ee317bf48f7dbffe03173':'435d9e2b639d25c9afdd775679b7eaff'}
        res = requests.get("https://www.codechef.com/dashboard",cookies=cookie)
        print(res.text)

    def test_open_weather(self, api_client):
        key = "token"
        api_client.base_url = "http://api.openweathermap.org"
        api_client.end_point = "/geo/1.0/direct"
        api_client.addParams({"q":"Hyderabad","limit":"5","appid":f"{key}"})
        resp = Requests.get(api_client)
        latitude = ic(resp.json()[0].get("lat"))
        longitude = ic(resp.json()[0].get("lon"))
        api_client.end_point = "/data/2.5/weather"
        api_client.addParams({"lat":f"{latitude}","lon":f"{longitude}","appid":f"{key}"})
        response = Requests.get(api_client)
        dict = response.json()
        ic(dict['name'])
        ic(dict['sys']['country'])
        ic(dict['main']['temp'])

    def test_graphql_request(self):
        url = "https://countries.trevorblades.com/"
        query = """
        {
          country(code: "IN") {
            name,
            native,
            capital,
            currency,
            languages {
              code,
              name
            }
          }
        }
        """

        response = requests.post(url, json={'query': query})
        print(json.dumps(response.json(), indent=2))





# encode security aspects (params/json_data)
# verifyig sec aspects (manual)
# schema validation
# graphql, grpc, websocket
# diff protocols



