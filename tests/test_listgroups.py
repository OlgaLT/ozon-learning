from hamcrest import assert_that, equal_to, not_

from tests.clients.api_client import ApiClient
from tests.helpers.base_helper import string_generator


def test_list_groups(add_data_to_db):

    response = ApiClient().get_groups_list()

    assert_that(len(response.json().get('items')), not_(equal_to(1)), "groups list is null")


def test_removed_group_not_in_list():

    response = ApiClient().create_group(string_generator('low', 10))
    group_id = response.json().get('group_id')
    ApiClient().remove_group(group_id)

    response_2 = ApiClient().get_groups_list()
    ids_lst = []
    for item in response_2.json().get('items'):
        ids_lst.append(item.get('id'))

    assert_that(group_id not in ids_lst, "removed group in list")


def test_in_list_only_real_groups(add_data_to_db):

    response = ApiClient().get_groups_list()
    ids_lst = []
    for item in response.json().get('items'):
        ids_lst.append(item.get('id'))

    # print(ids_lst)
    assert_that('0' not in ids_lst, "groups with 0 in id in list")
