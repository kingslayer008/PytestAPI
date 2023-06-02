import json

import pytest
from base import request_manager as cyrequest
from testcases.conftest import *


class TestLogin:

    @pytest.fixture(autouse=True)
    def _initial_params(self, generate_authentication_token, getURI, get_jenkins_user_password):
        self.uri = getURI
        self.token = generate_authentication_token
        self.email, self.password = get_jenkins_user_password

    @pytest.mark.regression
    def test_01_Login(self):

        login_url = self.uri + "/api/login"
        payload = {
            "email": self.email,
            "password": self.password
        }
        response = cyrequest.post_query(url=login_url, json= payload)
        pretty_print_request_body(response.request)
        json_response = json.loads(response.text)
        print(response.json()['token'])
        assert response.status_code == 200
