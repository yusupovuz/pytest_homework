def find_slope(points):
    if points[0]==points[2]:
        return 'undefined'
    return str((points[1]-points[3])//(points[0]-points[2]))
