import requests

from core.config_loader import config_load
from utils.openapi_validator import OpenAPIValidator

config=config_load()
ENV=config["env"].lower()

BASE_URL=config["base_url"][ENV]

validator=OpenAPIValidator()

def req(method=None,url=None,params=None,headers=None,json=None,data=None):
    response= requests.request(method=method,
                            url=BASE_URL+url,
                            params=params,
                            headers=headers,
                            json=json,
                            data=data,
                            timeout=10
                            )
    validator.validate(response.request,response)
    return response