def translate(text):
    """
    Translate a given text to Javanais.

    Args:
        text (str): The input text (lowercase, < 255 characters).

    Returns:
        str: The translated text in Javanais.
    """
    vowel = {"a","e", "i", "o", "u"}
    res = []
    for index, char in enumerate(text):
        if char in vowel and(index == 0 or text[index - 1] not in vowel):
            char = "av" + char
        res.append(char)
    return "".join(res)


if __name__ == "__main__":
    # Exemples de tests
    sentences = [
        "bonjour",     # Résultat attendu : "bavonjavour"
        "oiseau",      # Résultat attendu : "avoiseau"
        "python",      # Résultat attendu : "pythavon"
        "hello",       # Résultat attendu : "havellavo"
        "aeiou",       # Résultat attendu : "avaeaviavioavu"
    ]

    for sentence in sentences:
        print(f"Original: {sentence} -> Javanais: {translate(sentence)}")
