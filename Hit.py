from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


MainUI,_ = loadUiType('test.ui')

class Hole:
    def __init__(self, address=None, size=None):
        self.address = address
        self.size = size

    def __str__(self) -> str:  # For Printing a Single Object
        return str(self.address) + " : " + str(self.size)

    def __repr__(self) -> str:  # For Printing List (Collection) of Objects
        return str(self.address) + " : " + str(self.size)


class Main(QMainWindow , MainUI):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Memory Management')
        self.SHOW()

    def single_draw(self, pro_segment, holes, memory_size):
        starting_address = []
        segment_data = []

        for key in pro_segment.keys():
            starting_address.append(key)
        for value in pro_segment.values():
            segment_data.append(value)

        scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black,3)
        memory_color = QtGui.QBrush(QtCore.Qt.black)
        holes_color = QtGui.QBrush(QtCore.Qt.darkGray)
        segments_color = QtGui.QBrush(QtCore.Qt.white)
        r = QtCore.QRectF(QtCore.QPointF(50, 0), QtCore.QSizeF(110, memory_size))
        scene.addRect(r, pen, memory_color)

        mem_start = QGraphicsSimpleTextItem('0')
        scene.addItem(mem_start)
        mem_start.setPos(0, -7)
        mem_start.setScale(1.4)
        mem_end = QGraphicsSimpleTextItem(str(memory_size))
        scene.addItem(mem_end)
        mem_end.setPos(0, memory_size-7)
        mem_end.setScale(1.4)
        for i in range(len(starting_address)):
            # Segment size
            r = QtCore.QRectF(QtCore.QPointF(50, starting_address[i]), QtCore.QSizeF(110,segment_data[i][2]))
            scene.addRect(r, pen, segments_color)
            # Segment name
            seg_name = QGraphicsSimpleTextItem(segment_data[i][1])
            scene.addItem(seg_name)
            seg_name.setPos(68, starting_address[i] + segment_data[i][2] / 2 - 10)
            seg_name.setScale(1.4)
            # Parent process of the segment
            pro_name = QGraphicsSimpleTextItem(segment_data[i][0])
            scene.addItem(pro_name)
            pro_name.setPos(68,starting_address[i]+segment_data[i][2]/2-25)
            pro_name.setScale(1.4)
            # Starting address of the segment
            start = QGraphicsSimpleTextItem(str(starting_address[i]))
            scene.addItem(start)
            start.setPos(0, starting_address[i]-7)
            start.setScale(1.4)
            # Ending address of the segment
            end = QGraphicsSimpleTextItem(str(starting_address[i]+segment_data[i][2]))
            scene.addItem(end)
            end.setPos(0, starting_address[i]+segment_data[i][2]-7)
            end.setScale(1.4)
            # ٍ Segment size
            seg_size = QGraphicsSimpleTextItem('Size: '+str(segment_data[i][2]))
            scene.addItem(seg_size)
            seg_size.setPos(68, starting_address[i] + segment_data[i][2] / 2 + 7)
            seg_size.setScale(1.4)

        for i in range(len(holes)):
            # Hole size
            r = QtCore.QRectF(QtCore.QPointF(50, holes[i].address), QtCore.QSizeF(110, holes[i].size))
            scene.addRect(r, pen, holes_color)
            # Hole starting address
            start = QGraphicsSimpleTextItem(str(holes[i].address))
            scene.addItem(start)
            start.setPos(0, holes[i].address - 7)
            start.setScale(1.4)
            # Hole ending address
            end = QGraphicsSimpleTextItem(str(holes[i].address + holes[i].size))
            scene.addItem(end)
            end.setPos(0, holes[i].address + holes[i].size - 7)
            end.setScale(1.4)
            # Holes size
            hole_size = QGraphicsSimpleTextItem('Size: ' + str(holes[i].size))
            scene.addItem(hole_size)
            hole_size.setPos(68, holes[i].address + holes[i].size / 2 -10)
            hole_size.setScale(1.4)


    def SHOW(self):
        x = {30: ['Process 1', 'Segment 1', 120], 200: ['Process 2', 'Segment 2', 75], 300: ['Process 3', 'Segment 3', 75]}
        h1 = Hole(275, 25)
        h2 = Hole(150, 50)
        h3 = Hole(400, 50)
        holes = [h1, h2, h3]
        self.single_draw(x, holes, 500)



def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

