import pytest
import requests
from hamcrest import assert_that, not_none, equal_to, contains_string

from tests.clients.api_client import ApiClient
from tests.helpers.base_helper import string_generator


@pytest.mark.parametrize("group_name", [
    (string_generator('low', 10)),
    (string_generator('low', 1000)),
    (string_generator('upper', 10)),
    (string_generator('digits', 10)),
    (string_generator('cyrillic', 10))
], ids=["lowcase, 10 chars", "lowcase, 1000 runes", "uppercase, 10 runes", "digits, 10 runes", "cyrillic runes"])
def test_create_group(group_name):

    response = ApiClient().create_group(group_name)

    assert response.ok
    assert_that(response.json().get('group_id'), not_none)


@pytest.mark.parametrize("group_name", [
    (string_generator('low', 9)),
    (string_generator('low', 1001))
], ids=["name less than 10 runes", "name more than 1000 runes"])
def test_error_create_group(group_name):

    response = ApiClient().create_group(group_name)

    assert response.status_code == requests.codes.bad
    assert_that(response.json().get('code'), equal_to(3), 'code is not correct')
    assert_that(response.json().get('message'), contains_string("CreateGroupV1Request.Foo"), 'message not correct')
