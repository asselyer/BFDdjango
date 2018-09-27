def string_splosion(str):
    leng = ""
    for i in range(len(str)):
        leng = leng + str[:i + 1]
    return leng
