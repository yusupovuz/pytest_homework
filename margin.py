def close_compare(a, b, m = 0):
    if abs(a-b)<=m:
        return 0
    if a<b:
        return -1
    if a>b:
        return 1
    