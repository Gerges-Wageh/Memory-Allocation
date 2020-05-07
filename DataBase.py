from copy import deepcopy

import Algorithms
# Algorithms Should Return Hole Object, not Hole.address


class Process:
    def __init__(self, Name="", S=None):
        if S is None:
            S = {}
        self.Name = Name  # Name of Process
        self.Segments = S  # Segments are defined in pairs of Name, Size
        self.Seg_Num = self.Segments.__len__()  # Number of Segments


# Guess We are Done
# Apparently Not


class Hole:
    def __init__(self, address=None, size=None):
        self.address = address
        self.size = size

    def __str__(self) -> str:  # For Printing a Single Object
        return str(self.address) + " : " + str(self.size)

    def __repr__(self) -> str:  # For Printing List (Collection) of Objects
        return str(self.address) + " : " + str(self.size)


# Now We Are Done
# Nope


class Memory:
    def __init__(self, Size=0):
        self.Size = Size
        self.Holes = []
        # Make Holes As Objects
        # sort method from chat
        self.Pro_Seg = {}
        self.Processes = []

    def Add_Hole(self, hole):
        added = False
        for i in self.Holes:
            if hole.address < i.address + i.size < hole.address + hole.size or \
                    i.address < hole.address + hole.size < i.address + i.size or \
                    hole.address > self.Size or \
                    hole.address + hole.size > self.Size:
                print("Can't Add this Hole")
                return False
        # self.Holes[Start] = Size
        for i in self.Holes:
            if i.address == hole.address + hole.size:
                i.size += hole.size
                i.address = hole.address
                added = True
                break
        for i in self.Holes:
            if i.address + i.size == hole.address:
                i.size += hole.size
                added = True
                break
        if not added:
            self.Holes.append(hole)
            sorted(self.Holes, key=lambda Hole: Hole.size)
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

    def Fill_Hole(self, HoLe, Pro, Name, Size):
        if HoLe.size < Size:
            print("can't Put in Hole")
        else:
            if HoLe.size - Size != 0:
                hole = Hole(HoLe.address + Size, HoLe.size - Size)
                self.Add_Hole(hole)
                del hole
            self.Pro_Seg[HoLe.address] = {"Process": Pro, "Name": Name, "Size": Size}

    def DeAllocate(self, Pro):
        try:
            self.Processes.index(Pro)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            return
        temp = deepcopy(self.Pro_Seg)
        for i in self.Pro_Seg:
            if self.Pro_Seg[i]["Process"] == Pro.Name:
                hole = Hole(i, self.Pro_Seg[i]["Size"])
                self.Add_Hole(hole)
                temp.pop(i)
                del hole
        self.Processes.remove(Pro)
        self.Pro_Seg = deepcopy(temp)
        del temp

# Please Tell Me We are Done
# Yep
# I Hope
