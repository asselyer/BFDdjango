def monkey_trouble(a_smile, b_smile):
    monkey = False
    if a_smile and b_smile:
        monkey = True
    if not a_smile and not b_smile:
        monkey = True

    return monkey