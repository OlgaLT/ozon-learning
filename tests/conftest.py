import pytest
from sqlalchemy import create_engine

from tests.clients.api_client import ApiClient


@pytest.fixture
def add_data_to_db():
    response = ApiClient().create_group('test group')
    yield
    ApiClient().remove_group(response.json().get('group_id'))


@pytest.fixture()
def engine():
    db_string = "postgresql://postgres:postgres@localhost:5432/usr_group_api"
    engine = create_engine(db_string)
    return engine
