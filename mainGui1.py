# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGui1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from mem_drawing3 import *
from holes_window import Ui_holes_Form
from segments_window import Ui_segment_Form
from copy import deepcopy



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 600)

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # style sheet
        MainWindow.setStyleSheet('background-color:	lightyellow')
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(8)

        self.submit_hole_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_hole_button.setGeometry(QtCore.QRect(220, 182, 120, 60))
        self.submit_hole_button.setObjectName("submit_hole_button")
        self.submit_process_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_process_button.setGeometry(QtCore.QRect(220, 310, 120, 60))
        self.submit_process_button.setObjectName("submit_process_button")

        self.submit_all_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_all_btn.setGeometry(QtCore.QRect(200, 470, 151, 60))
        self.submit_all_btn.setObjectName("submit_all_btn")

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(70, -20, 461, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuForm = QtWidgets.QMenu(self.menubar)
        self.menuForm.setObjectName("menuForm")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_All = QtWidgets.QAction(MainWindow)
        self.actionSave_All.setObjectName("actionSave_All")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionSelect_AlL = QtWidgets.QAction(MainWindow)
        self.actionSelect_AlL.setObjectName("actionSelect_AlL")
        self.actionHorizontal_Lay_Out = QtWidgets.QAction(MainWindow)
        self.actionHorizontal_Lay_Out.setObjectName("actionHorizontal_Lay_Out")
        self.actionVertical_Lay_Out = QtWidgets.QAction(MainWindow)
        self.actionVertical_Lay_Out.setObjectName("actionVertical_Lay_Out")
        self.actionToolbars = QtWidgets.QAction(MainWindow)
        self.actionToolbars.setObjectName("actionToolbars")
        self.actionPrefrences = QtWidgets.QAction(MainWindow)
        self.actionPrefrences.setObjectName("actionPrefrences")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionAbout_project = QtWidgets.QAction(MainWindow)
        self.actionAbout_project.setObjectName("actionAbout_project")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionSelect_AlL)
        self.menuForm.addAction(self.actionHorizontal_Lay_Out)
        self.menuForm.addAction(self.actionVertical_Lay_Out)
        self.menuView.addAction(self.actionToolbars)
        self.menuSettings.addAction(self.actionPrefrences)
        self.menuWindow.addAction(self.actionMaximize)
        self.menuWindow.addAction(self.actionMinimize)
        self.menuHelp.addAction(self.actionAbout_project)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # style sheets

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        self.submit_hole_button.setStyleSheet('background-color:lightblue ')
        self.submit_process_button.setStyleSheet('background-color:lightblue')
        self.submit_all_btn.setStyleSheet('background-color:lightblue')
        self.menubar.setStyleSheet('background-color:mediumaquamarine')

        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        # Buttons Handling Events connections
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        self.submit_hole_button.clicked.connect(self.submit_hole_clicked)
        self.submit_process_button.clicked.connect(self.submit_process_clicked)
        self.submit_all_btn.clicked.connect(self.show_memory_layout_clicked)
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################
        ##############################################################################################################################

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Memory Allocation Project"))
        self.submit_hole_button.setText(_translate("MainWindow", "Add Holes"))
        self.submit_process_button.setText(_translate("MainWindow", "Add process"))
        self.submit_all_btn.setText(_translate("MainWindow", "Show Memory Layout"))
        self.title_label.setText(_translate("MainWindow", "Memory Allocation Project using Segmentation"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuForm.setTitle(_translate("MainWindow", "Form"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionSave_All.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionSelect_AlL.setText(_translate("MainWindow", "Select AlL"))
        self.actionHorizontal_Lay_Out.setText(_translate("MainWindow", "Horizontal Lay Out"))
        self.actionVertical_Lay_Out.setText(_translate("MainWindow", "Vertical Lay Out"))
        self.actionToolbars.setText(_translate("MainWindow", "Toolbars"))
        self.actionToolbars.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionPrefrences.setText(_translate("MainWindow", "Prefrences"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionAbout_project.setText(_translate("MainWindow", "About project"))

    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    # Buttons Handling Events functions
    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    ##############################################################################################################################
    def submit_hole_clicked(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_holes_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()

    def submit_process_clicked(self):
        self.segment_Form = QtWidgets.QWidget()
        self.ui = Ui_segment_Form()
        self.ui.setupUi(self.segment_Form)
        self.ui.process_list_table.itemClicked.connect(self.ui.fill_seg_table)
        self.segment_Form.show()

    def show_memory_layout_clicked(self):
        self.Form = QMainWindow()
        self.ui = Main()
        self.ui.setupUi(self.Form)
        for i in Ui_holes_Form.processes_list:
            Ui_holes_Form.total_memory_for_holes_window.DeAllocate(i.Name)
        self.ui.SHOW()
        self.ui.pro_choose.activated \
            .connect(self.ui.show_segments_table)
        self.ui.dealloc_reserve.clicked.connect(self.ui.reserve)
        self.ui.alloc_all.clicked.connect(self.ui.allocate_process_clicked)
        self.ui.alloc.clicked.connect(self.ui.alloc_btn)
        # self.ui.show_segments_table({30: ['Process 1', 'Segment 1', 120], 200: ['Process 2', 'Segment 1', 75], 300: ['Process 2', 'Segment 2', 75]})
        self.Form.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
