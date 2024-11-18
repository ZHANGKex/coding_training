def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemple d'utilisation
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(selection_sort(arr))  # Attendu: [11, 12, 22, 25, 34, 64, 90]
