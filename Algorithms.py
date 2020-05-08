'''
Created by: Abdelhamied Amr 7/5/2020 21:02
'''
def First_Fit(segment,holes):
    pos = None
    for  hole in holes:
        if segment.size <= hole.size:
            pos =  hole
            break
    return pos
def Best_Fit(segment,holes):
    pass
