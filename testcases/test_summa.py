import pytest
from base import request_manager as cyrequest
from testcases.conftest import *


#@pytest.mark.usefixtures("generate_authentication_token")
class TestChumma:

    # @pytest.fixture(autouse=True)
    # def _initial_params(self, generate_authentication_token, getURI, get_jenkins_user_password):
    #     self.uri = getURI
    #     self.token = generate_authentication_token
    #     self.email, self.password = get_jenkins_user_password



    def test_01_checking(self, generate_authentication_token, getURI):
        print(generate_authentication_token)
        print(getURI)

    def test_02_checking(self, generate_authentication_token, getURI):
        print(generate_authentication_token)
        print(getURI)
