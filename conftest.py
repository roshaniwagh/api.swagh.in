import pytest

from core.api_client import req
from endpoints.user_endpoints import UserEP


@pytest.fixture(scope="session")
def headers_with_authkey(get_auth_key):

    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Authorization":f"Bearer {get_auth_key}"
    }

    return headers


@pytest.fixture(scope="session")
def get_auth_key(headers):
    data={
        "username":"Shudip",
        "password":"Vampire85"
    }
    return req(method="POST",url=UserEP.LOGIN,params=None,headers=headers,data=data).json()["access_token"]

@pytest.fixture(scope="session")
def headers():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/x-www-form-urlencoded"
        }
