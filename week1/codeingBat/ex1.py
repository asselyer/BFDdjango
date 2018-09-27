def sleep_in(weekday, vacation):
    sleep = True
    if not weekday or vacation:
        return sleep
    else:
        sleep = False

    return sleep
