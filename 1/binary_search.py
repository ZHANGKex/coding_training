def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return None

# Exemple d'utilisation
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 4
    print(binary_search(arr, target))  # Attendu: 3 (index de 4)