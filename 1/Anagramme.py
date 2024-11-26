# def are_anagrams(str1: str, str2: str) -> bool:
#     return sorted(str1) == sorted(str2)

def are_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    
    count_char = {}
    for char in str1:
        count_char[char] = count_char.get(char, 0) + 1
        
    for char in str2:
        if char not in count_char:
            return False
        count_char[char] -= 1
        if count_char[char] < 0:
            return False
        
    return True

def main():
    """
    主函数：测试 are_anagrams 函数
    """
    # 测试用例 1
    str1 = "listen"
    str2 = "silent"
    print(f"测试 1: {are_anagrams(str1, str2)}")  # 期望输出 True

    # 测试用例 2
    str1 = "hello"
    str2 = "world"
    print(f"测试 2: {are_anagrams(str1, str2)}")  # 期望输出 False

    # 测试用例 3
    str1 = "aabbcc"
    str2 = "abcabc"
    print(f"测试 3: {are_anagrams(str1, str2)}")  # 期望输出 True

    # 测试用例 4
    str1 = "python"
    str2 = "typhon"
    print(f"测试 4: {are_anagrams(str1, str2)}")  # 期望输出 True

    # 测试用例 5
    str1 = "test"
    str2 = "sett"
    print(f"测试 5: {are_anagrams(str1, str2)}")  # 期望输出 True


if __name__ == "__main__":
    main()
