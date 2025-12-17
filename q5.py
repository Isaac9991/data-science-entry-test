def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    # Check if both num and divisor are numeric
    if isinstance(num, (int, float)) and isinstance(divisor, (int, float)):
        # Check divisibility
        result = (num % divisor == 0)
        # Print the result
        print("Is {} divisible by {}: {}".format(num, divisor, result))
        return result
    # If either num or divisor is not numeric, print an error message
    else:
        print("Both num and divisor must be numeric.")
    return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
check_divisibility(10, 2)
check_divisibility(7, 3)