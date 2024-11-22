def is_palindrome(s):
    text = " ".join(char.lower() for char in s if char.isalnum())
    return text == text[::-1]