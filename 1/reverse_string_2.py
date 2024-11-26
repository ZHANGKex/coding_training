def reverse_string(s):
    if len(s) <= 1:  # 基本情况
        return s
    return reverse_string(s[1:]) + s[0]  # 递归关系

# 测试
print(reverse_string("hello"))  # 输出："olleh"

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:] + s[0])