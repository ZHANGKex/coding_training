def reshape(n, line):
    line = line.replace(" ", "")
    res = [line[i:i+n] for i in range(0, len(line), n)]
    return "\n".join(res)


if __name__ == "__main__":
    test_input1 = (3, "abc de fghij")
    expected_output1 = "abc\ndef\nghi\nj"
    print(f"Input: {test_input1}")
    print(f"Expected Output: {expected_output1}")
    print(f"Your Output: {reshape(*test_input1)}")
    print()

    # 测试用例 2
    test_input2 = (2, "1 23 456")
    expected_output2 = "12\n34\n56"
    print(f"Input: {test_input2}")
    print(f"Expected Output: {expected_output2}")
    print(f"Your Output: {reshape(*test_input2)}")
    print()

    # 额外测试用例
    test_input3 = (4, "abcdefghijk")
    expected_output3 = "abcd\nefgh\nijk"
    print(f"Input: {test_input3}")
    print(f"Expected Output: {expected_output3}")
    print(f"Your Output: {reshape(*test_input3)}")
