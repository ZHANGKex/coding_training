import string

# def is_anagram(word1, word2):
#     word1 = "".join(char.lower() for char in word1 if char.isalnum())
#     word2 = "".join(char.lower() for char in word2 if char.isalnum())

#     return sorted(word1) == sorted(word2)

def is_anagram(word1, word2):
    word1 = "".join(char.lower() for char in word1 if char.isalnum())
    word2 = "".join(char.lower() for char in word2 if char.isalnum())

    char_dict = {}

    for char in word1:
        char_dict[char] = char_dict.get(char, 0) + 1

    for char in word2:
        if char not in char_dict:
            return False
        char_dict[char] -= 1
        if char_dict[char] < 0:
            return False
    return True
    
    print(char_dict)
# Tests
print(is_anagram("listen", "silent"))  # True
print(is_anagram("Astronomer", "Moon starer"))  # True
print(is_anagram("Hello", "World"))  # False
