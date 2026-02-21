from http.client import responses

from IPython.lib.deepreload import found_now

from core.api_client import req
from endpoints.department_endpoints import Department
from endpoints.user_endpoints import UserEP
from services.department_services import add_department, get_all_department
from utils.excel_utils import read_data, randomize_record


class Tests:


    def test_add_department_and_register_user(self,headers_with_authkey):

        payload = read_data("payload/create_department.xlsx", "Sheet1")[0]
        payload["name"] = randomize_record("payload/create_department.xlsx", "Sheet1","name")


        response_json=add_department(headers_with_authkey,payload)
        assert response_json.status_code==200
        assert response_json.json()["name"] == payload["name"]
        assert response_json.json()["location"] == payload["location"]
        found=False
        for dept in get_all_department(headers_with_authkey).json():
            if payload["name"]==dept["name"]:
                found=True
                break

        assert found
        APIAssert(response_json)
