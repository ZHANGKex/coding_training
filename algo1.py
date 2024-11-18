import re

def calibration_value(file_path):
    total_value = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                digits = re.findall(r'\d', line)
                if digits:
                    first = digits[0]
                    last = digits[-1]
                    number = int(first + last)
                    total_value = total_value + number
    
    return total_value

file_path = r'C:\work\training\input.txt'
result = calibration_value(file_path)
print("result:", result)