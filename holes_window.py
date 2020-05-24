# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'holes_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import DavidDatabase


class Ui_holes_Form(object):
    total_memory_for_holes_window = DavidDatabase.Memory()
    processes_list = []
    size_adjusted = False

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 437)

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # Style Sheet
        Form.setStyleSheet('background-color:lightyellow')

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        self.row_index = 0

        self.mem_size_entry = QtWidgets.QLineEdit(Form)
        self.mem_size_entry.setGeometry(QtCore.QRect(390, 130, 113, 20))
        self.mem_size_entry.setText("")
        self.mem_size_entry.setObjectName("mem_size_entry")

        self.mem_size_btn = QtWidgets.QPushButton(Form)
        self.mem_size_btn.setGeometry(QtCore.QRect(415, 160, 60, 25))
        self.mem_size_btn.setObjectName("mem_size_btn")

        self.mem_size_label = QtWidgets.QLabel(Form)
        self.mem_size_label.setGeometry(QtCore.QRect(400, 110, 101, 20))
        self.mem_size_label.setObjectName("mem_size_label")

        self.holes_title_label = QtWidgets.QLabel(Form)
        self.holes_title_label.setGeometry(QtCore.QRect(120, 10, 167, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.holes_title_label.setFont(font)
        self.holes_title_label.setObjectName("holes_title_label")
        self.starting_address_entry = QtWidgets.QLineEdit(Form)
        self.starting_address_entry.setGeometry(QtCore.QRect(30, 70, 113, 20))
        self.starting_address_entry.setObjectName("starting_address_entry")
        self.size_entry = QtWidgets.QLineEdit(Form)
        self.size_entry.setGeometry(QtCore.QRect(240, 70, 113, 20))
        self.size_entry.setObjectName("size_entry")
        self.starting_address_label = QtWidgets.QLabel(Form)
        self.starting_address_label.setGeometry(QtCore.QRect(36, 99, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.starting_address_label.setFont(font)
        self.starting_address_label.setObjectName("starting_address_label")
        self.size_label = QtWidgets.QLabel(Form)
        self.size_label.setGeometry(QtCore.QRect(280, 100, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.size_label.setFont(font)
        self.size_label.setObjectName("size_label")
        self.submit_hole_btn = QtWidgets.QPushButton(Form)
        self.submit_hole_btn.setGeometry(QtCore.QRect(180, 390, 75, 23))
        self.submit_hole_btn.setObjectName("submit_hole_btn")
        self.holes_table = QtWidgets.QTableWidget(Form)
        self.holes_table.setGeometry(QtCore.QRect(100, 160, 231, 221))
        # self.holes_table.setRowCount(0)
        self.holes_table.setColumnCount(2)
        self.holes_table.setObjectName("holes_table")
        self.starting_address_label_2 = QtWidgets.QLabel(Form)
        self.starting_address_label_2.setGeometry(QtCore.QRect(105, 157, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.starting_address_label_2.setFont(font)
        self.starting_address_label_2.setObjectName("starting_address_label_2")
        self.size_label_2 = QtWidgets.QLabel(Form)
        self.size_label_2.setGeometry(QtCore.QRect(240, 157, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.size_label_2.setFont(font)
        self.size_label_2.setObjectName("size_label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(100, 180, 231, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(100, 160, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(330, 160, 3, 61))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(215, 160, 3, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(100, 161, 231, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # styling sheets
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        self.starting_address_entry.setStyleSheet('background-color:white')
        self.size_entry.setStyleSheet('background-color:white')
        self.submit_hole_btn.setStyleSheet('background-color:slategray')
        self.mem_size_entry.setStyleSheet("background-color:white")
        self.mem_size_btn.setStyleSheet("background-color:slategray")
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################

        # Connection to the button
        self.submit_hole_btn.clicked.connect(self.submit_hole_clicked)
        self.mem_size_btn.clicked.connect(self.adjust_mem_size_clicked)

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        for i in self.total_memory_for_holes_window.Holes:
            self.holes_table.insertRow(self.row_index)
            self.holes_table.setItem(self.row_index, 0,
                                     QtWidgets.QTableWidgetItem(str(i.address)))
            self.holes_table.setItem(self.row_index, 1, QtWidgets.QTableWidgetItem(str(i.size)))
            self.row_index += 1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Holes Window"))
        self.holes_title_label.setText(_translate("Form", "Holes Window"))
        self.starting_address_label.setText(_translate("Form", "Starting address"))
        self.size_label.setText(_translate("Form", "Size"))
        self.submit_hole_btn.setText(_translate("Form", "submit hole"))
        self.starting_address_label_2.setText(_translate("Form", "Starting address"))
        self.size_label_2.setText(_translate("Form", "Size"))
        self.mem_size_btn.setText(_translate("segment_Form", "Adjust Size"))
        self.mem_size_label.setText(_translate("MainWindow", "Enter Memory Size"))

    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    # Button handling event function

    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    def submit_hole_clicked(self):
        if self.size_adjusted or self.total_memory_for_holes_window.Size != 0:
            try:
                if self.total_memory_for_holes_window.Size < int(self.starting_address_entry.text())+int(self.size_entry.text()):
                    error_msg = QtWidgets.QMessageBox()
                    error_msg.setWindowTitle("Memory Size Error")
                    error_msg.setText("Hole exceeds Memory Limit")
                    error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                    error_msg.exec_()
                else:
                    # adding the hole to the database
                    hole_1 = DavidDatabase.Hole(int(self.starting_address_entry.text()), int(self.size_entry.text()))
                    added_hole_return_value = Ui_holes_Form.total_memory_for_holes_window.Add_Hole(hole_1, Ui_holes_Form.
                                                                                                   total_memory_for_holes_window.
                                                                                                   Pro_Seg)
                    if not added_hole_return_value:
                        error_msg = QtWidgets.QMessageBox()
                        error_msg.setWindowTitle("Hole Entry Error")
                        error_msg.setText("Hole can't be Added")
                        error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                        error_msg.exec_()
                        return
                    print(Ui_holes_Form.total_memory_for_holes_window.Holes)
                    self.holes_table.insertRow(self.row_index)
                    self.holes_table.setItem(self.row_index, 0,
                                             QtWidgets.QTableWidgetItem(self.starting_address_entry.text()))
                    self.holes_table.setItem(self.row_index, 1, QtWidgets.QTableWidgetItem(self.size_entry.text()))
                    self.row_index += 1
                self.starting_address_entry.clear()
                self.size_entry.clear()
            except:
                error_msg = QtWidgets.QMessageBox()
                error_msg.setWindowTitle("Hole Entry Error")
                error_msg.setText("Please enter Valid Hole Data")
                error_msg.setIcon(QtWidgets.QMessageBox.Critical)
                error_msg.exec_()
        else:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Hole Entry Error")
            error_msg.setText("Please enter Memory Size First")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()
        #####

    def adjust_mem_size_clicked(self):
        try:
            Ui_holes_Form.total_memory_for_holes_window.Size = int(self.mem_size_entry.text())
            self.size_adjusted = True
        except:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setWindowTitle("Memory Size Error")
            error_msg.setText("Please enter Valid Memory Size")
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.exec_()
        self.mem_size_entry.clear()
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_holes_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
