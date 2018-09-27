def parrot_trouble(talking, hour):
    trouble = True
    if hour < 7 or hour > 20:
        if talking:
            return trouble
        else:
            trouble = False
    if hour >= 7 or hour <= 20:
        if talking:
            trouble = False
        else:
            trouble = False
    return trouble

