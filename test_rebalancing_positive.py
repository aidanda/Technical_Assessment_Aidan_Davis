
import pytest
from test_data import *
from rebalancing import *


# ============================================================
# TC01 - Standard portfolio rebalancing
#
# Scenario:
# Verify that the application correctly calculates the shares
# to buy, sell or leave unchanged across five securities.
#
# Input:
# Total assets: €100,000
# IBM: 20% target, 10% current, €150 share price
# MSFT: 20% target, 20% current, €90 share price
# ORCL: 20% target, 30% current, €220 share price
# AAPL: 20% target, 20% current, €450 share price
# HD: 20% target, 20% current, €70 share price
#
# Expected result:
# IBM: Buy approximately 66.67 shares
# MSFT: No trade
# ORCL: Sell approximately 45.45 shares
# AAPL: No trade
# HD: No trade
# ============================================================

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio1():

    result = rebalance(total_assets1, portfolio1)

    assert result["IBM"] == pytest.approx(10000 / 150)
    assert result["MSFT"] == 0
    assert result["ORCL"] == pytest.approx(-10000 / 220)
    assert result["AAPL"] == 0
    assert result["HD"] == 0


# ============================================================
# TC02 - Security already at target allocation
#
# Scenario:
# Verify that no shares are bought or sold when a security
# is already at its target allocation.
#
# Input:
# Total assets: €100,000
# IBM: 20% target, 20% current, €150 share price
#
# Expected result:
# Zero shares to buy or sell.
# ============================================================

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio2():

    result = rebalance(total_assets2, portfolio2)

    assert result["IBM"] == 0


# ============================================================
# TC03 - Security below target allocation
#
# Scenario:
# Verify that the application calculates a positive share
# quantity when a security is below its target allocation.
#
# Input:
# Total assets: €100,000
# IBM: 30% target, 10% current, €150 share price
#
# Expected result:
# Buy approximately 133.33 shares.
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio3():

    result = rebalance(total_assets3, portfolio3)

    assert result["IBM"] == pytest.approx(133.3333333333)


# ============================================================
# TC04 - Security above target allocation
#
# Scenario:
# Verify that the application calculates a negative share
# quantity when a security is above its target allocation.
#
# Input:
# Total assets: €100,000
# IBM: 10% target, 30% current, €150 share price
#
# Expected result:
# Sell approximately 133.33 shares.
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio4():

    result = rebalance(total_assets4, portfolio4)

    assert result["IBM"] == pytest.approx(-133.3333333333)


# ============================================================
# TC05 - Multiple securities requiring different trades
#
# Scenario:
# Verify that the application correctly calculates buying
# and selling quantities across multiple securities.
#
# Input:
# Total assets: €100,000
# IBM: 30% target, 10% current, €100 share price
# MSFT: 5% target, 10% current, €50 share price
#
# Expected result:
# IBM: Buy 200 shares
# MSFT: Sell 100 shares
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio5():

    result = rebalance(total_assets5, portfolio5)

    assert result["IBM"] == 200
    assert result["MSFT"] == -100


# ============================================================
# TC06 - Increased total account value
#
# Scenario:
# Verify that share quantities are recalculated correctly
# when the total account value increases.
#
# Input:
# Total assets: €200,000
# IBM: 20% target, 10% current, €100 share price
#
# Expected result:
# Buy 200 shares.
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio6():

    result = rebalance(total_assets6, portfolio6)

    assert result["IBM"] == 200


# ============================================================
# TC07 - Single-security portfolio
#
# Scenario:
# Verify that the application correctly processes a
# portfolio containing only one security.
#
# Input:
# Total assets: €100,000
# IBM: 50% target, 20% current, €100 share price
#
# Expected result:
# Buy 300 shares.
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio7():

    result = rebalance(total_assets7, portfolio7)

    assert result["IBM"] == 300


# ============================================================
# TC08 - Empty portfolio
#
# Scenario:
# Verify that the application handles an empty portfolio
# without raising an exception.
#
# Input:
# Total assets: €100,000
# Portfolio: Empty
#
# Expected result:
# Return an empty results dictionary.
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio8():

    result = rebalance(total_assets8, portfolio8)

    assert result == {}


# ============================================================
# TC09 - Zero total account assets
#
# Scenario:
# Verify that the application handles a portfolio with
# zero total assets.
#
# Input:
# Total assets: €0
# IBM: 20% target, 10% current, €100 share price
#
# Expected result:
# Zero shares to buy or sell.
# ============================================================

@pytest.mark.regression
@pytest.mark.positive
def test_rebalance_portfolio9():

    result = rebalance(total_assets9, portfolio9)

    assert result["IBM"] == 0

# ============================================================
