def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        return n * extraLongFactorials(n - 1)