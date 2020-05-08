def BestFit(se, holes):
    minHole = None
    for k in holes:
        if (k.size() >= se):
            if(minHole == None):
                minHole = k
            elif(minHole.size()>k.size()):
                minHole=k
    return minHole
    return minHole