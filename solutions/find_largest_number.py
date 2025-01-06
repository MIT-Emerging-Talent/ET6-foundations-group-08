from typing import List


def find_largest_number(numbers: List[int]) -> int:
    """
    Finds the largest number in a list of integers.

    Parameters:
    numbers (list): A non-empty list of integers.

    Returns:
    int: The largest number in the list.

    Raises:
    ValueError: If the input list is empty.
    """
    # Validate input
    if not numbers:
        raise ValueError("The list cannot be empty.")

    # Initialize the largest number with the first element of the list
    largest = numbers[0]

    # Loop through each number in the list
    for num in numbers:
        # Update the largest number if a bigger number is found
        if num > largest:
            largest = num

    # Return the largest number
    return largest
