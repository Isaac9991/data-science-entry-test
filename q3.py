def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    # Ensure dct is a dictionary
    dct = dict(dct)
    # Check if the key exists and print original value if it does
    if key in dct:
        # Print the original value
        print("Original value for key '{}': {}".format(key, dct[key]))
    # Update the value for the existing key
    dct[key] = value
    # Print the updated dictionary
    print("Updated dictionary:", dct)
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)
