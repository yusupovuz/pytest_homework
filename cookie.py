def cookie(x):
    if type(x) == str:
        return 'Who ate the last cookie? It was Zach!'
    if type(x) == float or type(x) == int:
        return 'Who ate the last cookie? It was Monica!'
    return 'Who ate the last cookie? It was the dog!'