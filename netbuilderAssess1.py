import string


def replaceLetterWithPosition(text):
    # create dictionary of letters: numbers
    alphabet = dict(zip(string.ascii_lowercase, range(1, 27)))
    # use dictionary comprehension to cast numbers into strings
    alphabet = {k: str(v) for k, v in alphabet.items()}

    # format string by making it lowercase and removing spaces
    text = text.lower().replace(" ", "")
    # Use list comprehension to replace letters with str(numbers)
    numbers = [alphabet[character] for character in text]
    # Join all valies a list into one giant string
    return " ".join(numbers)
