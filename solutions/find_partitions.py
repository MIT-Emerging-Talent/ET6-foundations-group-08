"""
Module: Partition Finder

This module provides a function `find_partitions` that calculates all possible
partitions of a given number `n` using integers up to a specified maximum
value `max_num`. A partition of a number is a way of expressing it as a sum
of positive integers, regardless of order.

Behavior:
- The function uses recursion to explore all valid partitions of `n`.
- It ensures the partitions are unique and sorted.
- The implementation handles base cases for invalid inputs and recursively
  builds partitions by including and excluding the current `max_num`.

Implementation:
1. Base cases:
   - If `n` is negative or `max_num` is 0, return an empty list (no partitions).
   - If `n` equals `max_num`, include the partition `[max_num]`.
2. Recursive calls:
   - Find partitions including `max_num` by subtracting it from `n`.
   - Find partitions excluding `max_num` by reducing `max_num`.
3. Combine results:
   - Return all valid partitions by concatenating and sorting the partitions
     from the above steps.

Example:
    Input: n = 6, max_num = 4
    Output: [[4, 2], [4, 1, 1], [3, 3], [3, 2, 1], [3, 1, 1, 1], [2, 2, 2],
             [2, 2, 1, 1], [2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
"""


def find_partitions(n, max_num):
    """
    Find all possible partitions of a number `n` using integers from 1 to `max_num`.

    A partition of `n` is a way of writing it as a sum of positive integers, where
    the order of terms doesn't matter. This function returns all unique partitions
    of `n` using numbers from 1 to `max_num`.

    Parameters:
    - n (int): The number to be partitioned.
    - max_num (int): The largest integer that can be used in the partition.

    Returns:
    - list of lists: A list containing all partitions, where each partition is a
      list of integers that sum to `n`. All numbers used are <= `max_num`.
    """
    if n < 0 or max_num == 0:
        return []

    exact_match = []
    if n == max_num:
        exact_match = [[max_num]]

    with_max_num = [
        partition + [max_num] for partition in find_partitions(n - max_num, max_num)
    ]
    without_max_num = find_partitions(n, max_num - 1)

    return sorted(exact_match) + sorted(with_max_num) + sorted(without_max_num)


# Add test cases for the function
if __name__ == "__main__":
    expected_result_case_1 = [
        [1, 1, 4],
        [2, 4],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2],
        [1, 1, 1, 3],
        [1, 1, 2, 2],
        [1, 2, 3],
        [2, 2, 2],
        [3, 3],
    ]
    expected_result_case_2 = [
        [1, 1, 3],
        [2, 3],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 2, 2],
    ]
    expected_result_case_3 = [[1, 1, 2], [2, 2], [1, 1, 1, 1]]
    expected_result_case_4 = [[1, 1, 1]]
    expected_result_case_5 = []
    expected_result_case_6 = []

    # Test cases for correctness
    assert find_partitions(6, 4) == expected_result_case_1, "Test case 1 failed"
    assert find_partitions(5, 3) == expected_result_case_2, "Test case 2 failed"
    assert find_partitions(4, 2) == expected_result_case_3, "Test case 3 failed"
    assert find_partitions(3, 1) == expected_result_case_4, "Test case 4 failed"
    assert find_partitions(0, 5) == expected_result_case_5, "Test case 5 failed"
    assert find_partitions(-1, 3) == expected_result_case_6, "Test case 6 failed"

    print("All test cases passed!")
