def pos_neg(a, b, negative):
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        if not negative:
            return True
        else:
            return False
    if a < 0 and b < 0:
        if negative:
            return True
        else:
            return False
    if a > 0 and b > 0:
        if negative:
            return False
        else:
            return False

    return True
