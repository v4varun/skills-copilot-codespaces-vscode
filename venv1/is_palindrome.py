def is_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome.

    Args:
    s (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
if __name__ == "__main__":
    print("Script is running")
    test_string = "A man, a plan, a canal, Panama"
    print(f"Is the string '{test_string}' a palindrome? {is_palindrome(test_string)}")