from test_data import *
from rebalancing import *


def test_rebalance_portfolio1():
    # Call the rebalancing function using Portfolio 1.
    result = rebalance(total_assets1, portfolio1)

    # Check the expected share quantities for each security.
    assert result["IBM"] == 10000 / 150
    assert result["MSFT"] == 0
    assert result["ORCL"] == -10000 / 220
    assert result["AAPL"] == 0
    assert result["HD"] == 0
