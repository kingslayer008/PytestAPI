from base import request_manager as rm
import pytest
from config.environment import ReadConfig


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="qa")
    parser.addoption("--uri", action="store", default=ReadConfig.getURI())
    parser.addoption("--Email", action="store", default=ReadConfig.getEmail())
    parser.addoption("--Password", action="store", default=ReadConfig.getPassword())


@pytest.fixture
def getURI(request):
    return request.config.getoption("uri")


@pytest.fixture(scope="session")
def generate_authentication_token(request):

    url = request.config.getoption("uri") + "/api/login"
    email = request.config.getoption("Email")
    password = request.config.getoption("Password")
    data_payload = {
        "email": email,
        "password": password
    }
    response = rm.post_query(url=url, data=data_payload)
    return response.json()['token']


@pytest.fixture
def get_jenkins_user_password(request):
    email = request.config.getoption("Email")
    password = request.config.getoption("Password")
    return email, password


def pretty_print_request_body(request):
    print('\n---------Request---------\n{}\n{}\n'.format(
        request.method + ' ' + request.url,
        request.body)
    )


def pretty_print_message(message):
    print("\n{}\n".format(
        message
    ))


def pretty_print_response(response):
    print('\n-------Response--------\nStatus code: {}\nResponse Time:{}\n'.format(
        str(response.status_code),
        response.elapsed.total_seconds())
    )