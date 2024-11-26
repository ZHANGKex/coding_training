def animal_sound(s):
    texts = s.split(" ")
    res = []
    for text in texts:
        for i in range(len(text) - 2):
            if text[i] == text[i + 1] == text[i + 2]:
                res.append(text)
                break
    return res