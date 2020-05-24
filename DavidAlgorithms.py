def First_Fit(segment, holes):
    pos = None
    for hole in holes:
        if segment <= hole.size:
            pos = hole
            break
    return pos


def best_fit(segment, holes):
    min_hole = None
    for hole in holes:
        if hole.size == segment:
            min_hole = hole
            break
        elif hole.size > segment:
            if min_hole is None:
                min_hole = hole
            elif min_hole.size > hole.size:
                min_hole = hole
    return min_hole
