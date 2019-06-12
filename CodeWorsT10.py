def distance(x1, y1, x2, y2):
    side1 = x1-x2
    side2 = y1-y2
    dist = (side1**2+side2**2)**0.5
    dist_round = round(dist,2)
    return dist_round