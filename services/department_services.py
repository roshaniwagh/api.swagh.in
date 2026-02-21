from core.api_client import req
from endpoints.department_endpoints import Department
from utils.excel_utils import read_data


def add_department(headers_with_authkey,json):
       response = req("POST", url=Department.CREATE_DEPARTMENT, params=None,headers= headers_with_authkey,json= json,data= None)
       return  response


def get_all_department(headers_with_authkey)   :
       response = req("GET", url=Department.GET_ALL_DEPARTMENT, params=None, headers=headers_with_authkey, json=None,
                      data=None)
       return response
