#!/usr/bin/env python3
## ________________________________________ ##
## Author: Henrique Souza
## Filename: run_log.py
## Created: 2023-11-07
## ________________________________________ ##

import os
from pathlib import Path
import sys

from ui_mainwindow import Ui_MainWindow
from ui_run_log import Ui_RunLog

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import subprocess as sp

class RunLogger():
    RunLog:QtWidgets.QMainWindow
    ui:Ui_MainWindow
    rlui:Ui_RunLog

    def loadSearchRunLog(self):
        dirnow = self.ui.primary_name.text()
        mfile, mfilter = QtWidgets.QFileDialog.getOpenFileName(self, "Find Files", f'{self.default_path}/{dirnow}', "*.info")
        self.showRunLog()

        if not mfile: # if nothing was selected, get out
            return

        self.loadRunLog(mfile)

    def loadRunLog(self, fmapchannel):
        with open(fmapchannel,'r') as file:
            self.textrunlog = file.read()
        self.rlui.runlogfield.setPlainText(self.textrunlog)
