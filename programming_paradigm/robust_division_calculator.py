def safe_divide(numerator, denominator):
    """Performs division with error handling and checks for correct output."""
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Handle division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."

        # Perform division and check the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."

