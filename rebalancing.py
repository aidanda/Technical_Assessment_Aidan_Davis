
def validate_portfolio(portfolio):

    # Define the security fields required for rebalancing.
    required_fields = ["target", "current", "price"]

    # Check every security in the portfolio.
    for security, data in portfolio.items():

        # Check that all required fields are present.
        for field in required_fields:
            if field not in data:
                raise ValueError(f"{security}: Missing required field '{field}'")

        # Check that the share price is greater than zero.
        if data["price"] <= 0:
            raise ValueError(f"{security}: Share price must be greater than zero")


def rebalance(total_assets, portfolio):

    # Validate the portfolio before performing any calculations.
    validate_portfolio(portfolio)

    # Dictionary to store the calculated shares to buy or sell.
    results = {}

    # Process each security in the portfolio.
    for security, data in portfolio.items():

        # Calculate the target and current security values.
        target_value = total_assets * data["target"] / 100
        current_value = total_assets * data["current"] / 100

        # Calculate the difference between target and current values.
        # Positive = buy, negative = sell, zero = no trade.
        difference = target_value - current_value

        # Convert the monetary difference into a number of shares.
        shares = difference / data["price"]

        # Store the calculated share quantity.
        results[security] = shares

        # Display the calculated result for this security.
        print(f"{security}: {shares} shares")

    # Return the completed results dictionary.
    return results
