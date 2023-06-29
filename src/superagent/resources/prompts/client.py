# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError


class PromptsClient:
    def __init__(self, *, environment: str, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def list_prompts(self) -> typing.Any:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "api/v1/prompts"),
            headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_a_prompt(self, *, name: str, input_variables: typing.List[typing.Any], template: str) -> typing.Any:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "api/v1/prompts"),
            json=jsonable_encoder({"name": name, "input_variables": input_variables, "template": template}),
            headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_prompt(self, prompt_id: str) -> typing.Any:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/prompts/{prompt_id}"),
            headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch_prompt(self, prompt_id: str, *, request: typing.Dict[str, typing.Any]) -> typing.Any:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/prompts/{prompt_id}"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_prompt(self, prompt_id: str) -> typing.Any:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/prompts/{prompt_id}"),
            headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPromptsClient:
    def __init__(self, *, environment: str, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def list_prompts(self) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", "api/v1/prompts"),
                headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_a_prompt(
        self, *, name: str, input_variables: typing.List[typing.Any], template: str
    ) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "api/v1/prompts"),
                json=jsonable_encoder({"name": name, "input_variables": input_variables, "template": template}),
                headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_prompt(self, prompt_id: str) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/prompts/{prompt_id}"),
                headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch_prompt(self, prompt_id: str, *, request: typing.Dict[str, typing.Any]) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/prompts/{prompt_id}"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_prompt(self, prompt_id: str) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/prompts/{prompt_id}"),
                headers=remove_none_from_headers({"X_SUPERAGENT_API_KEY": self.api_key}),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
