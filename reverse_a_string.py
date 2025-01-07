def test_reverse_string():
    # function body
def is_palindrome(s):
    """
    Check if the given string is a palindrome.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: convert to lowercase and remove any spaces
    normalized_str = s.lower()
    
    # Compare the string with its reverse
    return normalized_str == normalized_str[::-1]

# Test Cases
def test_is_palindrome():
    """
    Test the is_palindrome function with multiple cases.
    """
    # Case 1: A simple palindrome
    assert is_palindrome("madam") == True, "Test Case 1 Failed"
    
    # Case 2: A non-palindrome string
    assert is_palindrome("hello") == False, "Test Case 2 Failed"
    
    # Case 3: A case-insensitive palindrome
    assert is_palindrome("RaceCar") == True, "Test Case 3 Failed"
    
    # Case 4: An empty string (edge case)
    assert is_palindrome("") == True, "Test Case 4 Failed"
    
    # Case 5: A single-character string (edge case)
    assert is_palindrome("a") == True, "Test Case 5 Failed"
    
    print("All test cases passed!")

# Run Tests
test_is_palindrome()
