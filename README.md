# Portfolio Rebalancing – Technical Assessment

## 1. Project Description

This project implements a portfolio rebalancing calculation that determines the number of shares to buy or sell for each security based on its target allocation, current allocation and unit share price.

The solution is implemented in Python, with automated tests using pytest.

## 2. Assessment Requirements

The assessment requires a rebalancing application to be tested through manual and automated test cases.

The tests must verify that the number of shares to buy or sell for each security is correctly calculated.

The implementation, test cases and supporting documentation are maintained in GitHub.

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

- Fractional share quantities are supported. Results are not rounded to whole shares, preserving calculation accuracy.

## 5. Manual Test Cases

The following test cases define the expected behaviour of the portfolio rebalancing application. They cover buying, selling, unchanged allocations, different portfolio values, empty portfolios and input validation.

Positive share quantities represent purchases; negative quantities represent sales.

All test cases are documented for manual execution. Actual results and execution statuses remain pending until the manual tests have been performed. Automated execution is documented separately through pytest.

### TC01 – Standard Portfolio

**Test data:** Portfolio value USD 100,000. Portfolio contains IBM, MSFT, ORCL, AAPL and HD, using the target allocations, current allocations and share prices specified in the assessment.

**Expected result:** Buy 66.6667 IBM shares, sell 45.4545 ORCL shares. No trades for MSFT, AAPL or HD.

**Actual result:** Pending  
**Status:** Pending

### TC02 – Security at Target Allocation

**Test data:** IBM: target 20%, current 20%, price USD 150. Portfolio value USD 100,000.

**Expected result:** Zero shares to buy or sell.

**Actual result:** Pending  
**Status:** Pending

### TC03 – Security Below Target Allocation

**Test data:** IBM: target 30%, current 10%, price USD 150. Portfolio value USD 100,000.

**Expected result:** Buy 133.3333 IBM shares.

**Actual result:** Pending  
**Status:** Pending

### TC04 – Security Above Target Allocation

**Test data:** IBM: target 10%, current 30%, price USD 150. Portfolio value USD 100,000.

**Expected result:** Sell 133.3333 IBM shares.

**Actual result:** Pending  
**Status:** Pending

### TC05 – Different Security Allocations

**Test data:** IBM: target 30%, current 10%, price USD 100. MSFT: target 5%, current 10%, price USD 50. Portfolio value USD 100,000.

**Expected result:** Buy 200 IBM shares and sell 100 MSFT shares.

**Actual result:** Pending  
**Status:** Pending

### TC06 – Different Portfolio Value

**Test data:** IBM: target 20%, current 10%, price USD 100. Portfolio value USD 200,000.

**Expected result:** Buy 200 IBM shares.

**Actual result:** Pending  
**Status:** Pending

### TC07 – Single-Security Portfolio

**Test data:** IBM: target 50%, current 20%, price USD 100. Portfolio value USD 100,000.

**Expected result:** Buy 300 IBM shares.

**Actual result:** Pending  
**Status:** Pending

### TC08 – Empty Portfolio

**Test data:** Portfolio value USD 100,000. No securities supplied.

**Expected result:** Return an empty results dictionary.

**Actual result:** Pending  
**Status:** Pending

### TC09 – Zero Portfolio Value

**Test data:** IBM: target 20%, current 10%, price USD 100. Portfolio value USD 0.

**Expected result:** Zero shares to buy or sell.

**Actual result:** Pending  
**Status:** Pending

### TC10 – Zero Share Price

**Test data:** IBM: target 20%, current 10%, price USD 0. Portfolio value USD 100,000.

**Expected result:** Raise a ValueError stating that the share price must be greater than zero.

**Actual result:** Pending  
**Status:** Pending

### TC11 – Missing Share Price

**Test data:** Portfolio value USD 100,000. IBM: target 20%, current 10%. The `price` field is omitted.

**Expected result:** Raise a ValueError identifying the missing `price` field.

**Actual result:** Pending  
**Status:** Pending

### TC12 – Missing Target Allocation

**Test data:** Portfolio value USD 100,000. IBM: current 10%, price USD 150. The `target` field is omitted.

**Expected result:** Raise a ValueError identifying the missing `target` field.

**Actual result:** Pending  
**Status:** Pending

### TC13 – Missing Current Allocation

**Test data:** Portfolio value USD 100,000. IBM: target 20%, price USD 150. The `current` field is omitted.

**Expected result:** Raise a ValueError identifying the missing `current` field.

**Actual result:** Pending  
**Status:** Pending

## 6. Automated Testing

Automated tests are implemented using Python and pytest. The test suite verifies the calculated share quantities for valid inputs and checks input validation and error handling for invalid inputs.

### Test Organisation

The automated test suite is separated into two files:

| Test file | Purpose | Test cases |
|---|---|---|
| `test_rebalancing_positive.py` | Tests calculations using valid portfolio data. | TC01–TC09 |
| `test_rebalancing_negative.py` | Tests input validation and error handling. | TC10–TC13 |

### Pytest Markers

Pytest markers categorise tests so that specific groups can be executed independently. The following markers are configured in `pytest.ini`:

| Marker | Purpose | Test cases |
|---|---|---|
| `smoke` | Essential checks confirming core application functionality. | TC01, TC02 |
| `regression` | Checks that existing application functionality continues to work correctly. | TC01–TC13 |
| `positive` | Tests valid input and expected calculation results. | TC01–TC09 |
| `negative` | Tests invalid input and expected validation errors. | TC10–TC13 |

A test can have multiple markers. For example, TC01 is classified as a smoke, regression and positive test.

### Pytest Command Options

| Option | Description |
|---|---|
| `-s` | Displays `print()` statements from the application during test execution instead of capturing them. |
| `-v` | Displays individual test names and their results. |
| `-m` | Selects tests using a registered pytest marker, such as `smoke`, `regression`, `positive` or `negative`. |

### Running the Tests

Run the complete test suite from the project directory:

```bash
python -m pytest -v -s
```

Run individual test groups using marker selection:

| Command | Description |
|---|---|
| `python -m pytest -m smoke -v -s` | Runs smoke tests. |
| `python -m pytest -m regression -v -s` | Runs regression tests. |
| `python -m pytest -m positive -v -s` | Runs positive tests. |
| `python -m pytest -m negative -v -s` | Runs negative tests. |

Individual test files can also be executed independently:

```bash
python -m pytest test_rebalancing_positive.py -v -s
python -m pytest test_rebalancing_negative.py -v -s
```

## 7. Project Structure

The project is organised as follows:

```text
Technical_Assessment_Aidan_Davis/
│
├── .gitignore
├── rebalancing.py
├── test_data.py
├── conftest.py
├── test_rebalancing_positive.py
├── test_rebalancing_negative.py
├── pytest.ini
├── requirements.txt
├── README.md
│
└── assessment_doc/
    └── Technical Assessment QA - Aidan Davis.docx
```

The Python virtual environment (`.venv/`) and generated cache files are excluded from Git through `.gitignore`.

### File Responsibilities

| File | Responsibility |
|---|---|
| `rebalancing.py` | Contains the portfolio rebalancing calculation and input validation. |
| `test_data.py` | Stores input data for all test scenarios. |
| `conftest.py` | Reserved for shared pytest fixtures if required across multiple test files. No active fixtures are currently defined. |
| `test_rebalancing_positive.py` | Contains automated tests for valid inputs and expected calculations (TC01–TC09). |
| `test_rebalancing_negative.py` | Contains automated tests for invalid inputs and validation errors (TC10–TC13). |
| `pytest.ini` | Configures pytest test discovery and markers. |
| `requirements.txt` | Lists the Python packages required to run the tests. |
| `.gitignore` | Specifies files and folders Git should ignore. |
| `README.md` | Documents the assessment, assumptions, manual test cases and automated testing. |
| `assessment_doc/Technical Assessment QA - Aidan Davis.docx` | Contains the technical assessment submission. |


## 8. Potential CI/CD and Enterprise QA Integration

The current implementation demonstrates the core portfolio rebalancing functionality and its automated verification using pytest.

In a larger enterprise development environment, the solution could be extended through integration with established QA and DevOps tooling:

- **Jenkins CI/CD:** Configure automated test execution following code commits or pull requests, with JUnit XML reports published as part of each build.
- **Jira and Xray:** Integrate test management to provide requirements traceability, test execution tracking and centralised reporting of automated test results.
- **Automated Quality Reporting:** Generate execution summaries and maintain historical test results to monitor regression trends and build stability.
- **Code Quality Analysis:** Introduce static analysis, linting and type checking to improve code quality and maintainability.
- **Release Quality Gates:** Incorporate automated test results into the delivery pipeline to support release readiness decisions.

These integrations would extend the existing automated test suite into a broader continuous integration and quality engineering workflow.