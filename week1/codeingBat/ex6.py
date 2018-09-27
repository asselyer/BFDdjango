def makes10(a, b):
  if a == 10 or b==10:
    return True
  if a != 10 and b!=10:
    if a+b==10:
      return True
    else:
      return False
  return True
