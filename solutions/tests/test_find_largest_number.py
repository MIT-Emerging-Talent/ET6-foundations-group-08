from find_largest_number import find_largest_number

# Test cases
print(find_largest_number([3, 1, 7, 0, 5]))  # Output: 7
print(find_largest_number([-10, -20, -3, -50]))  # Output: -3
print(find_largest_number([0, 0, 0, 0]))  # Output: 0
print(find_largest_number([100, 200, 300]))  # Output: 300
print(find_largest_number([5]))  # Output: 5
print(find_largest_number([1, -1, 3, -5, 2]))  # Output: 3

# Edge case: Empty list (should raise an error)
try:
    print(find_largest_number([]))  # Expected to raise a ValueError
except ValueError as e:
    print(e)  # Output: The list cannot be empty.
