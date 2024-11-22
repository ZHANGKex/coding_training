import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return True
    return False

def main():
    # 用户输入
    num = int(input("请输入一个整数："))
    if is_prime(num):
        print(f"{num} 是一个素数。")
    else:
        print(f"{num} 不是一个素数。")

if __name__ == "__main__":
    main()
