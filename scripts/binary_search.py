def binary_search(values, target):
    """
    Finds the position of a target value
    inside a sorted array.
    """

    # Initialize pointers
    left = 0
    right = len(values) - 1

    # Search while range exists
    while left <= right:

        # Get middle position
        middle = (left + right) // 2

        # Target found
        if values[middle] == target:
            return middle

        # Search left half
        elif target < values[middle]:
            right = middle - 1

        # Search right half
        else:
            left = middle + 1

    # Target does not exist
    return -1


# ---------------------------------------------------
# Example usage
# ---------------------------------------------------

numbers = [2, 4, 6, 8, 10, 12, 14]

position = binary_search(
    values=numbers,
    target=10
)

print("Target Index:", position)