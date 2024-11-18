def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    a , b = 0, 1
    for _ in range(n):
        a = b
        b = a + b
    return a