import pytest
from test_data import total_assets1, portfolio1


@pytest.fixture
def standard_portfolio():
    return total_assets1, portfolio1