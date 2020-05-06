from copy import deepcopy

import Algorithms


class Process:
    def __init__(self, Name="", S=None):
        if S is None:
            S = {}
        self.Name = Name  # Name of Process
        self.Segments = S  # Segments are defined in pairs of Name, Size
        self.Seg_Num = self.Segments.__len__()  # Number of Segments


# Guess We are Done
# Apparently Not

class Memory:
    def __init__(self, Size=0):
        self.Size = Size
        self.Holes = []
        # Make Holes As Objects
        # sort method from chat
        self.Pro_Seg = {}
        self.Processes = []

    def Add_Hole(self, Start, Size):
        for i in self.Holes:
            if Start < i + self.Holes[i] < Start+Size or i < Start + Size < i + self.Holes[i] or Start > self.Size or \
                    Start+Size > \
                    self.Size:
                print("Can't Add this Hole")
                return False
        # self.Holes[Start] = Size
        if self.Holes[i].StartAdress == Start + Size is not None:
            self.Holes[Start] += self.Holes[Start + Size]
            self.Holes.pop(Start + Size)
        for i in self.Holes:
            if i + self.Holes[i] == Start:
                self.Holes[i] += Size
                self.Holes.pop(Start)
                break
        return True

    def Allocate_Process(self, Pro, Algorithm):
        Address = None
        for s in Pro.Segments:
            if Algorithm == 0:
                # Put Algorithm Here
                Address = Algorithms.First_Fit(Pro.Segments[s], self)
            elif Algorithm == 1:
                # Put Algorithm Here
                Address = Algorithms.Best_Fit(Pro.Segments[s], self)
            # Whichever Algorithm used, Returns Start Address of Hole, else Returns None
            if Address is None:
                return False
            self.Fill_Hole(Address, Pro.Name, s, Pro.Segments[s])
            # Pro.Allocate_Segment(s)
        self.Processes.append(Pro)
        return True

    def Fill_Hole(self, Start, Pro, Name, Size):
        if self.Holes[Start] < Size:
            print("can't Put in Hole")
        else:
            if self.Holes[Start] - Size != 0:
                self.Add_Hole(Start + Size, self.Holes[Start] - Size)
            self.Pro_Seg[Start] = {"Process": Pro, "Name": Name, "Size": Size}
            self.Holes.pop(Start)

    def DeAllocate(self, Pro):
        try:
            self.Processes.index(Pro)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            return
        temp = deepcopy(self.Pro_Seg)
        for i in self.Pro_Seg:
            if self.Pro_Seg[i]["Process"] == Pro.Name:
                self.Add_Hole(i, self.Pro_Seg[i]["Size"])
                temp.pop(i)
        self.Processes.remove(Pro)
        self.Pro_Seg = deepcopy(temp)
        del temp

# Now We Are Done
