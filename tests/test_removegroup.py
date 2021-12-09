import requests
import random
from hamcrest import assert_that, equal_to, not_, contains_string

from tests.clients.api_client import ApiClient
from tests.helpers.base_helper import get_group_ids_list, get_max_id, get_removed_id


def test_remove_group(add_data_to_db, engine):

    group_id = random.choice(get_group_ids_list(engine))
    response = ApiClient().remove_group(group_id)

    assert_that(response.json().get('found'))


def test_error_remove_id_not_in_db(engine):

    group_id = get_max_id(engine)
    group_id += group_id
    response = ApiClient().remove_group(group_id)

    assert_that(not_(response.json().get('found')))


def test_error_remove_removed_id(engine):

    group_id = random.choice(get_removed_id(engine))
    response = ApiClient().remove_group(group_id)

    assert_that(not_(response.json().get('found')))


def test_error_remove_zero_id():

    response = ApiClient().remove_group(0)

    assert response.status_code == requests.codes.bad
    assert_that(response.json().get('code'), equal_to(3), 'code is not correct')
    assert_that(response.json().get('message'), contains_string("RemoveGroupV1Request.GroupId"), 'message not correct')
