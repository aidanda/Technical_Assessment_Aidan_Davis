
def rebalance(total_assets, portfolio):
    # Dictionary to store the calculated shares to buy or sell for each security.
    results = {}

    # Process each security and its allocation details in the portfolio.
    for security, data in portfolio.items():

        # Calculate the value the security should have based on its target allocation.
        target_value = total_assets * data["target"] / 100

        # Calculate the value the security currently has based on its current allocation.
        current_value = total_assets * data["current"] / 100

        # Calculate the difference between the target and current values.
        # Positive = buy, negative = sell, zero = no trade.
        difference = target_value - current_value

        # Convert the monetary difference into a number of shares using the unit price.
        shares = difference / data["price"]

        # Store the share quantity against the security name.
        results[security] = shares

        # Display the calculated result for this security.
        print(f"{security}: {shares} shares")

    # Return the completed dictionary containing results for all securities.
    return results
