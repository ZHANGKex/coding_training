def is_palindrome(s):
    return s == s[::-1]

# Exemple d'utilisation
if __name__ == "__main__":
    s = "radar"
    print(is_palindrome(s))  # Attendu: True
