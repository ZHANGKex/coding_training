def fibonacci(n):
    a , b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Exemple d'utilisation
if __name__ == "__main__":
    n = 10
    print(fibonacci(n))  # Attendu: 55
