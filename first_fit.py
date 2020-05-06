def first_fit(segment, holes):
    pos = None
    for hole in holes.items():
        if segment.size <= hole[1]:
            pos = hole[0]
            break
    return pos
