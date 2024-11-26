# def max_subarray_sum(nums):
#     max_sum = 0
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             current_sum = sum(nums[i:j])
#             if current_sum > max_sum:
#                 max_sum = current_sum
#     return max_sum

def max_subarray_sum(nums):
    max_current = max_global = nums[0]

    for i in range(len(nums)):
        max_current = max(nums[i], nums[i] + max_current)

        if max_current > max_global:
            max_global = max_current

    return max_global
# Exemple d'utilisation
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(nums))  # Attendu: 6 (sous-tableau: [4, -1, 2, 1])
