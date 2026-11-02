import pytest
from test_data import *
from rebalancing import *

# ============================================================
# TC10 - Zero share price
#
# Scenario:
# Verify that the application rejects a security with
# a share price of zero.
#
# Input:
# Total assets: €100,000
# IBM: 20% target, 10% current
# Share price: €0
#
# Expected result:
# ValueError identifying that the share price must
# be greater than zero.
# ============================================================

@pytest.mark.regression
@pytest.mark.negative
def test_rebalance_zero_share_price():

    with pytest.raises(ValueError, match="Share price must be greater than zero"):
        rebalance(total_assets10, portfolio10)


# ============================================================
# TC11 - Missing share price
#
# Scenario:
# Verify that the application detects a security
# with a missing share price.
#
# Input:
# Total assets: €100,000
# IBM: 20% target, 10% current
# Share price: Missing
#
# Expected result:
# ValueError identifying the missing 'price' field.
# ============================================================

@pytest.mark.regression
@pytest.mark.negative
def test_rebalancing_missing_security_data():

    with pytest.raises(ValueError, match="Missing required field 'price'"):
        rebalance(total_assets11, portfolio11)


# ============================================================
# TC12 - Missing target percentage
#
# Scenario:
# Verify that the application detects a security
# with a missing target allocation.
#
# Input:
# Total assets: €100,000
# IBM: Target allocation missing
# Current allocation: 10%
# Share price: €150
#
# Expected result:
# ValueError identifying the missing 'target' field.
# ============================================================

@pytest.mark.regression
@pytest.mark.negative
def test_rebalancing_missing_target():

    with pytest.raises(ValueError, match="Missing required field 'target'"):
        rebalance(total_assets12, portfolio12)


# ============================================================
# TC13 - Missing current percentage
#
# Scenario:
# Verify that the application detects a security
# with a missing current allocation.
#
# Input:
# Total assets: €100,000
# IBM: Target allocation: 20%
# Current allocation: Missing
# Share price: €150
#
# Expected result:
# ValueError identifying the missing 'current' field.
# ============================================================

@pytest.mark.regression
@pytest.mark.negative
def test_rebalancing_missing_current():

    with pytest.raises(ValueError, match="Missing required field 'current'"):
        rebalance(total_assets13, portfolio13)
