import json

import pytest
from base import request_manager as cyrequest
from testcases.conftest import *
import hashlib
import hmac
import requests
from base.endpoints import ReadEndpoint as re
from testcases.constants import EndPointModuleConstants


class TestLogin:

    @pytest.fixture(autouse=True)
    def _initial_params(self, generate_authentication_token, getURI, get_jenkins_user_password):
        self.uri = getURI
        self.token = generate_authentication_token
        self.email, self.password = get_jenkins_user_password

    @pytest.mark.regression
    def test_01_Login(self):

        login_url = self.uri + str(re.fetch_endpoint("Login", "login_endpoint"))
        payload = {
            "email": self.email,
            "password": self.password
        }
        # payload = json.loads(payload)
        # payload = json.dumps(payload)
        response = cyrequest.post_query(url=login_url, data= payload)
        pretty_print_request_body(response.request)
        json_response = json.loads(response.text)
        print(response.json()['token'])
        assert response.status_code == 200
