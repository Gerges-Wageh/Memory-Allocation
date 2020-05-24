from copy import deepcopy

import DavidAlgorithms
# Algorithms Should Return Hole Object, not Hole.address


class Process:
    def __init__(self, Name="", S=None):
        if S is None:
            S = {}
        self.Name = Name  # Name of Process
        self.Segments = S  # Segments are defined in pairs of Name, Size
        self.Seg_Num = 0  # Number of Segments

    def __repr__(self) -> str:
        return self.Name

    def __str__(self) -> str:
        return self.Name


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

    def __eq__(self, o) -> bool:
        return self.address == o.address and self.size == o.size


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

    def Add_Hole(self, hole, Pro_Seg):
        added = False
        if hole.address > self.Size or \
                hole.address + hole.size > self.Size:
            # print("Cant add this whole")
            return False
        for i in self.Holes:
            if hole.address < i.address + i.size <= hole.address + hole.size or \
                    i.address < hole.address + hole.size <= i.address + i.size:
                # print("Can't Add this Hole")
                return False
        for i in Pro_Seg:
            if hole.address < i + Pro_Seg[i]["Size"] <= hole.address + hole.size or \
                    i < hole.address + hole.size <= i + Pro_Seg[i]["Size"]:
                return False
        # self.Holes[Start] = Size
        for i in self.Holes:
            if i.address == hole.address + hole.size:
                i.size += hole.size
                i.address = hole.address
                added = True
                hole.address = i.address
                hole.size = i.size
                break
        for i in self.Holes:
            if i.address + i.size == hole.address:
                i.size += hole.size
                added = True
                try:
                    self.Holes.remove(hole)
                except ValueError:
                    break
        if not added:
            self.Holes.append(hole)
            self.Holes = sorted(self.Holes, key=lambda Hole: Hole.address)
        return True

    def Allocate_Segment(self, Pro, Seg_Name, Seg_Size, Algorithm):
        # This is used in Allocate Button as following, give it Process name "String",
        # Segment Name "Key in Pro.Segments", Segment Size "Value in Pro.Segments",
        # And a number (0 for first fit, 1 for best fit)
        Address = None
        try:  # this line Should be in the button main loop, not here
            self.Processes.index(Pro)
            return True
        except ValueError:
            for s in self.Pro_Seg.values():
                if s["Process"] == Pro and s["Name"] == Seg_Name:
                    return True
            if Algorithm == 0:
                # Put Algorithm Here
                Address = DavidAlgorithms.First_Fit(Seg_Size, self.Holes)
            elif Algorithm == 1:
                # Put Algorithm Here
                Address = DavidAlgorithms.best_fit(Seg_Size, self.Holes)
            if Address is None:
                self.DeAllocate(Pro)
                return False
            self.Fill_Hole(Address, Pro, Seg_Name, Seg_Size)
            return True

    def Allocate_Process(self, Pro, Algorithm):
        Address = None
        try:
            if self.Processes.index(Pro.Name):
                return True
        except ValueError:
            for s in Pro.Segments:
                if Algorithm == 0:
                    # Put Algorithm Here
                    Address = DavidAlgorithms.First_Fit(Pro.Segments[s], self.Holes)
                elif Algorithm == 1:
                    # Put Algorithm Here
                    Address = DavidAlgorithms.best_fit(Pro.Segments[s], self.Holes)
                if Address is None:
                    self.DeAllocate(Pro)
                    return False
                self.Fill_Hole(Address, Pro.Name, s, Pro.Segments[s])
            self.Processes.append(Pro.Name)
            return True

    def Fill_Hole(self, HoLe, Pro, Name, Size):
        if HoLe.size < Size:
            print("can't Put in Hole")
        else:
            self.Holes.remove(HoLe)
            if HoLe.size - Size != 0:
                hole = Hole(HoLe.address + Size, HoLe.size - Size)
                self.Add_Hole(hole, self.Pro_Seg)
                del hole
            self.Pro_Seg[HoLe.address] = {"Process": Pro, "Name": Name, "Size": Size}

    def DeAllocate(self, Pro):
        try:
            self.Processes.index(Pro)
            temp = deepcopy(self.Pro_Seg)
            for i in self.Pro_Seg:
                if self.Pro_Seg[i]["Process"] == Pro:
                    hole = Hole(i, self.Pro_Seg[i]["Size"])
                    temp.pop(i)
                    self.Add_Hole(hole, temp)
                    del hole
            self.Pro_Seg = deepcopy(temp)
            del temp
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

            return
        self.Processes.remove(Pro)
        # Remove Process from Original List
