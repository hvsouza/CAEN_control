# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../move_files/move_files/about.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(798, 298)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 265, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../move_files/move_files/../../.repo_img/computer-nerd.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 471, 421))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        About.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(About)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        About.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(About)
        self.statusbar.setObjectName("statusbar")
        About.setStatusBar(self.statusbar)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.label_2.setText(_translate("About", "<html><head/><body><p>Author: Henrique Souza<br/>email: henriquevieira.souza@gmail.com<br/><br/>This GUI interface was create to make the operation of a CAEN digitizer easier</p><p><br/>Please refer to the GitHub repository for more information:<br/><a href=\"http://github.com/hvsouza/CAEN_Digitizer/\"><span style=\" text-decoration: underline; color:#007af4;\">CAEN Digitizer</span></a><br/><br/>A lot of effort was put in this GUI, please read the instructions. </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())