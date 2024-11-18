def remove_duplicates(nums):
    nums = set(nums)
    return list(nums)

# Exemple d'utilisation
if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4]
    print(remove_duplicates(nums))  # Attendu: [1, 2, 3, 4]
