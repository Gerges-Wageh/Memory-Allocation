def BestFit(se, holes):
    minv = None
    for k in holes:
        if (k.size() >= se):
            if (minv == None):
                minv = k
            elif (k.size() < minv.size()):
                minv = k
    for k in holes:
        if (k == minv and k.address < minv.address):
            minv = k
    return minv
