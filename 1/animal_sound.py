def animal_sound(s):
    texts = s.split(" ")
    res = []
    for text in texts:
        for i in range(len(text) - 2):
            if text[i] == text[i + 1] == text[i + 2]:
                res.append(text)
                break
    return res


def animal_sound(s):
    def is_animal_sound(mot):
        left = 0
        right = 0
        count = 0
        while right < len(mot):
            while mot[left] == mot[right]:
                count += 1
                right += 1
                if count > 2:
                    return True
            left = right
            count = 0
            right += 1

        return False