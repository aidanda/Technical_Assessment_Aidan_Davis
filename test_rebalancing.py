
import pytest
from test_data import *
from rebalancing import *

# TC01
# Verify that the standard portfolio produces the correct number of shares
# to buy, sell or leave unchanged for all five securities.
def test_rebalance_portfolio1():
    # Call the rebalancing function using Portfolio 1.
    result = rebalance(total_assets1, portfolio1)

    # Check the expected share quantities for each security.
    assert result["IBM"] == pytest.approx(10000 / 150)
    assert result["MSFT"] == 0
    assert result["ORCL"] == pytest.approx(-10000 / 220)
    assert result["AAPL"] == 0
    assert result["HD"] == 0


# TC02
# Verify that a security already at its target allocation requires no trade.
def test_rebalance_security_already_at_target():
    # Call the rebalancing function using Portfolio 2.
    result = rebalance(total_assets2, portfolio2)

    # Check that no shares need to be bought or sold.
    assert result["IBM"] == 0


# TC03
# Verify that a security below its target allocation produces the
# correct positive share quantity to buy.
def test_rebalance_security_below_target():
    # Call the rebalancing function using Portfolio 3.
    result = rebalance(total_assets3, portfolio3)

    # Check the expected number of shares to buy.
    assert result["IBM"] == pytest.approx(133.3333333333)


# TC04
# Verify that a security above its target allocation produces the
# correct negative share quantity to sell.
def test_rebalance_security_above_target():
    # Call the rebalancing function using Portfolio 4.
    result = rebalance(total_assets4, portfolio4)

    # Check the expected number of shares to sell.
    assert result["IBM"] == pytest.approx(-133.3333333333)


# TC05
# Verify that different allocation percentages across multiple securities
# produce the correct share quantities to buy and sell.
def test_rebalance_different_portfolio_allocations():
    # Call the rebalancing function using Portfolio 5.
    result = rebalance(total_assets5, portfolio5)

    # Check the expected share quantities for each security.
    assert result["IBM"] == pytest.approx(200)
    assert result["MSFT"] == pytest.approx(-100)


# TC06
# Verify that changing the total account value to €200,000 produces
# the correct share quantity based on the new account value.
def test_rebalance_different_total_asset_value():
    # Call the rebalancing function using Portfolio 6.
    result = rebalance(total_assets6, portfolio6)

    # Check the expected number of shares to buy.
    assert result["IBM"] == pytest.approx(200)


# TCO7
def test_rebalance_single_security_portfolio():
    result = rebalance(total_assets7, portfolio7)

    # Check the expected number of shares to buy.
    assert result["IBM"] == pytest.approx(300)

# TC08
def test_rebalance_empty_portfolio():
    result = rebalance(total_assets8, portfolio8)

    assert result == {}

# TC09
def test_rebalance_zero_total_account_balance():
    result = rebalance(total_assets9, portfolio9)

    assert result["IBM"] == pytest.approx(0)

# TC10
# Verify that the application rejects a security with a zero share price
# and raises a ValueError instead of attempting division by zero.
def test_rebalance_zero_share_price():

    # Check that the application raises the expected exception.
    with pytest.raises(ValueError, match="Share price must be greater than zero"):
        rebalance(total_assets10, portfolio10)