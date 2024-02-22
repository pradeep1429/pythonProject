import pytest

from api.api_client import APIClient
from api.utility.property_reader import PropertyReader


@pytest.fixture(scope='session')
def api_client():
    PropertyReader.load_all_props()
    api_config = APIClient()
    api_config.base_url = PropertyReader.config_prop['base_url'].data
    api_config.content_type = PropertyReader.config_prop['content_type'].data
    return api_config