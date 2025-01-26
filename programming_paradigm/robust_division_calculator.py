def safe_divide(numerator, denominator):
    """
    Safely perform division, handling common errors such as division by zero 
    and non-numeric input.

    Parameters:
    numerator: The numerator for the division.
    denominator: The denominator for the division.

    Returns:
    str: A message indicating the result of the division or the error encountered.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt the division
        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."

