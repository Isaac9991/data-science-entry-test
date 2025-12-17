def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        # Swapping the values
        x, y = y, x
        print("Swapped values: x =", x, ", y =", y)
    # If either x or y is not numeric, return -1
    else:
        return -1
    return (x, y)


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap("Apple", 10)
swap(9, 17)