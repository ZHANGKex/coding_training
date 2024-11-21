def two_sum(nums, target):
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            if nums[left] + nums[right] == target:
                return [left, right]
            
    return [0, 0]

# Exemple d'utilisation
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Attendu: [0, 1] (ou les indices des deux nombres)
