def invert(l):
    c = []
    i = 0
    while i<len(l):
        c += [l[i]*(-1)]
        i+=1
    return c        