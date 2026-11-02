# Portfolio Rebalancing – Technical Assessment

## 1. Project Description

This project implements a portfolio rebalancing calculation that determines the number of shares to buy or sell 
for each security based on its target allocation, current allocation and unit share price.
The solution is implemented in Python, with automated tests using pytest.

## 2. Assessment Requirements

The assessment requires a rebalancing application to be tested through manual and automated test cases.
The tests must verify that the total number of shares to buy or sell for each security is correctly calculated.
The implementation and tests are documented and maintained in GitHub.

## 3. Rebalancing Logic
For each security, the application:
1. Calculates the target monetary value using the total portfolio assets and target allocation.
2. Calculates the current monetary value using the total portfolio assets and current allocation.
3. Calculates the difference between the target and current values.
4. Divides the difference by the unit share price to determine the number of shares to buy or sell.

**Calculation:**

- Target value = Total assets × Target allocation / 100
- Current value = Total assets × Current allocation / 100
- Difference = Target value − Current value
- Shares = Difference / Unit share price

A positive result represents shares to buy, a negative result represents shares to sell, and zero represents no trade.

## 4. Assumptions
- Portfolio allocations are supplied as percentages.
- Each security has a target allocation, current allocation and unit share price.
- The total portfolio asset value is supplied as an input.
- Fractional share quantities are supported by the current implementation.
- Results are calculated independently for each security.


## 5. Manual Test Cases
The following test cases validate the portfolio rebalancing calculations, including buying, selling, unchanged allocations and input validation.
Positive share quantities represent purchases; negative quantities represent sales.

| Test ID| Scenario                                                                                                    | Input | Expected result | Actual result | Pass/Fail |
|---     |---     |---|---|---|---|
| TC01   | Standard portfolio              | Assets: €100,000. IBM: 20% target, 10% current, €150 price. MSFT: 20%, 20%, €90. ORCL: 20%, 30%, €220. AAPL: 20%, 20%, €450. HD: 20%, 20%, €70. | IBM: +66.6667; MSFT: 0; ORCL: -45.4545; AAPL: 0; HD: 0 shares. | Pending | Pending |
| TC02   | Security already at target      | Assets: €100,000. IBM: 20% target, 20% current, €150 price.                                                                                     | IBM: 0 shares. | Pending | Pending |
| TC03   | Security below target           | Assets: €100,000. IBM: 30% target, 10% current, €150 price. | IBM: +133.3333 shares. | Pending | Pending |
| TC04   | Security above target           | Assets: €100,000. IBM: 10% target, 30% current, €150 price. | IBM: -133.3333 shares. | Pending | Pending |
| TC05   | Different portfolio allocations | Assets: €100,000. IBM: 30% target, 10% current, €100 price. MSFT: 5% target, 10% current, €50 price. | IBM: +200; MSFT: -100 shares. | Pending | Pending |
| TC06   | Different total asset value     | Assets: €200,000. IBM: 20% target, 10% current, €100 price. | IBM: +200 shares. | Pending | Pending |
| TC07   | Single-security portfolio       | Assets: €100,000. IBM: 50% target, 20% current, €100 price. | IBM: +300 shares. | Pending | Pending |
| TC08   | Empty portfolio                 | Assets: €100,000. No securities supplied. | Empty results dictionary. | Pending | Pending |
| TC09   | Zero total assets               | Assets: €0. IBM: 20% target, 10% current, €100 price. | IBM: 0 shares. | Pending | Pending |
| TC10   | Zero unit share price           | Assets: €100,000. IBM: 20% target, 10% current, €0 price. | Validation error: zero share price rejected. | Pending | Pending |
| TC11   | Missing security data           | Assets: €100,000. IBM: target 20%, current 10%, price missing. | Validation error: missing price rejected. | Pending | Pending |
| TC12 | Missing target percentage | IBM security has no `target` field | ValueError identifying missing `target` | ValueError: IBM: Missing required field 'target' | PASS |
| TC13 | Missing current percentage | IBM security has no `current` field | ValueError identifying missing `current` | ValueError: IBM: Missing required field 'current' | PASS |

### Test Execution Notes

- Actual results will be recorded after executing each test.
- Pass/Fail status will be assigned by comparing actual results against expected results.
- TC10 and TC11 require input validation to be implemented before they can pass.
- Fractional share quantities are retained by the current implementation; no rounding is applied.


## 6. Automated Testing

Automated tests are implemented using Python and pytest.
The automated test suite validates the calculated share quantities against expected results for the supported test scenarios.
Run the tests from the project directory:

```bash
python -m pytest test_rebalancing_positive.py -v - s
```

## 7. Pytest Markers and Test Execution

### Test Organisation

The automated test suite is separated into two files to distinguish between valid and invalid input scenarios:

| Test file | Purpose | Test cases |
|---|---|---|
| `test_rebalancing_positive.py` | Tests calculations using valid portfolio data. | TC01–TC09 |
| `test_rebalancing_negative.py` | Tests application validation and error handling. | TC10–TC13 |

### Pytest Markers

Pytest markers are used to categorise tests, allowing specific groups of tests to be executed independently.

The following markers are configured in `pytest.ini`:

| Marker | Purpose | Test cases |
|---|---|---|
| `smoke` | Essential checks confirming that core application functionality works. | TC01, TC02 |
| `regression` | Checks that existing application functionality continues to work correctly. | TC01–TC13 |
| `positive` | Tests valid input and expected calculation results. | TC01–TC09 |
| `negative` | Tests invalid input and expected validation errors. | TC10–TC13 |

A test can have multiple markers. For example, TC01 is classified as a smoke, regression and positive test.

### Pytest Command Options

The following command-line options are used when executing tests:

| Option | Description |
|---|---|
| `-s` | Displays `print()` statements from the application during test execution instead of capturing them. |
| `-v` | Verbose output. Displays each individual test name and its result. |
| `-m` | Selects tests using a registered pytest marker, such as `smoke`, `regression`, `positive` or `negative`. |

### Running the Test Suite

The complete test suite can be executed using:

```powershell
python -m pytest -v -s
```

This runs all discovered tests, regardless of their markers, displaying individual test results and application output.

Individual test groups can also be executed using marker selection:

| Command | Description |
|---|---|
| `python -m pytest -m smoke -v -s` | Runs smoke tests. |
| `python -m pytest -m regression -v -s` | Runs regression tests. |
| `python -m pytest -m positive -v -s` | Runs positive tests. |
| `python -m pytest -m negative -v -s` | Runs negative tests. |

Individual test files can also be executed independently:

```powershell
python -m pytest tests/test_rebalancing_positive.py -v -s
```

```powershell
python -m pytest tests/test_rebalancing_negative.py -v -s
```

### Test Execution Strategy

The markers provide flexibility in how the test suite

## 7. Project Structure

```text
Technical_Assessment_Aidan_Davis/
│
├── .venv/                  # Python virtual environment
├── .gitignore              # Files excluded from Git
├── rebalancing.py          # Rebalancing application logic
├── test_data.py            # Input data for all test scenarios
├── conftest.py              # Shared pytest fixtures and setup
├── test_rebalancing.py     # Automated test cases
├── pytest.ini               # Pytest configuration
├── requirements.txt        # Python package dependencies
└── README.md                # Assessment documentation and manual test cases
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `rebalancing.py` | Contains the rebalancing calculation being tested. |
| `test_data.py` | Stores the input data for each test scenario. |
| `conftest.py` | Provides reusable pytest fixtures and shared test setup. |
| `test_rebalancing_positive.py` | Contains automated test cases and expected results. |
| `pytest.ini` | Configures pytest test discovery and execution. |
| `requirements.txt` | Lists the Python packages required to run the tests. |
| `.gitignore` | Specifies files and folders Git should ignore. |
| `README.md` | Documents the assessment, assumptions, manual test cases and project structure. |