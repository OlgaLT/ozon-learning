import requests
import random
from hamcrest import assert_that, equal_to, not_, contains_string

from tests.clients.api_client import ApiClient
from tests.helpers.base_helper import get_group_ids_list, get_max_id, get_removed_id


def test_describe_group(add_data_to_db, engine):

    group_id = random.choice(get_group_ids_list(engine))
    response = ApiClient().get_group_describe(group_id)
    response = response.json().get('group')

    # print('foo', response)
    assert_that(response.get('foo'), not_(equal_to('')), "foo is empty")
    assert_that(response.get('id'), not_(equal_to('')), "id is empty")


def test_error_describe_id_not_in_db(engine):

    group_id = get_max_id(engine)
    group_id += group_id
    response = ApiClient().get_group_describe(group_id)

    assert response.status_code == requests.codes.not_found
    assert_that(response.json().get('code'), equal_to(5), 'code is not correct')
    assert_that(response.json().get('message'), contains_string("not found"), 'message not correct')


def test_error_describe_removed_id(engine):

    group_id = random.choice(get_removed_id(engine))
    response = ApiClient().get_group_describe(group_id)

    assert response.status_code == requests.codes.not_found, 'return description for removed id'
    assert_that(response.json().get('code'), equal_to(5), 'code is not correct')
    assert_that(response.json().get('message'), contains_string("not found"), 'message not correct')


def test_error_scribe_zero_id():

    response = ApiClient().get_group_describe(0)

    assert response.status_code == requests.codes.bad
    assert_that(response.json().get('code'), equal_to(3), 'code is not correct')
    assert_that(response.json().get('message'),
                contains_string("DescribeGroupV1Request.GroupId"), 'message not correct')
