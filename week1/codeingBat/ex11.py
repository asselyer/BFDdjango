def front_back(str):
    if len(str) <= 1:
        return str

    for i in range(len(str)):
        str1 = str[1:-1]
        return str[-1] + str1 + str[0]
