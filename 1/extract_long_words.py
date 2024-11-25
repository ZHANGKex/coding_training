def extract_long_words(s):
    res = [word for word in s.split() if len(word) > 5]
    return res


if __name__ == "__main__":
    input_text = "This is an example of a sentence with several long words"
    result = extract_long_words(input_text)
    print(result)  # 示例输出: ['example', 'sentence', 'several']