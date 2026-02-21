import json
from openapi_core import OpenAPI
from openapi_core.contrib.requests import (
    RequestsOpenAPIRequest,
    RequestsOpenAPIResponse,
)


class OpenAPIValidator:

    def __init__(self, spec_path="config/openapi.json"):
        with open(spec_path) as f:
            self.spec = OpenAPI.from_dict(json.load(f))

    def validate(self, request, response):
        openapi_request = RequestsOpenAPIRequest(request)
        openapi_response = RequestsOpenAPIResponse(response)

        result = self.spec.validate_response(
            openapi_request,
            openapi_response,
        )

        if result.errors:
            raise AssertionError(
                f"OpenAPI validation failed: {result.errors}"
            )

        return True