from core.api_client import req
from endpoints.user_endpoints import UserEP


def test_login(self, get_auth_key):
    response = get_auth_key


def test_get_all_user(headers_with_authkey):
    response = req("GET", UserEP.GET_ALL_USERS, None, headers_with_authkey, None, None)
    return response.json()


