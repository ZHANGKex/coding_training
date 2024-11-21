def sum_of_digits(n):
    text = [i for i in str(n)]
    res = 0
    for num in text:
        res += int(num)
    return res

# Exemple d'utilisation
if __name__ == "__main__":
    n = 12345
    print(sum_of_digits(n))  # Attendu: 15
