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

from datetime import datetime


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

    def loadRunLog(self, frunlog):
        with open(frunlog,'r') as file:
            self.textrunlog = file.read()

        try:
            lines = [l for l in self.textrunlog.split("\n")[3:]]
            self.textrunlog = '\n'.join(lines)
            self.rlui.runlogfield.setPlainText(self.textrunlog)
        except:
            QMessageBox.critical(self, "ERROR!!!", "Could not load the runlog")

    def saveRunLog(self, pathconfig, finishingrun = False):

        filename = 'runlog.info'
        if not self.isprimary:
            filename = 'runlog_2.info'

        frunlog = f'{pathconfig}/{filename}'

        texttowrite = self.rlui.runlogfield.toPlainText() # get whatever is already there...

        if not os.path.exists(frunlog): # if file files does not exist, if subrun is 0, fine
            if self.keep_ask_log:
                has_new_log = self.showDiagRunLog()
                if has_new_log: texttowrite = self.rlui.runlogfield.toPlainText() # get whatever is already there...
                else: return

        if os.path.exists(frunlog): # if it exists..
            if finishingrun and self.nofilesmove: # If user is finishing run, and no file was moved, no reason to save things
                return
            try:
                with open(frunlog, 'r') as f:
                    dumpline = f.readline()
                    if not dumpline.startswith('#'): # if the first line is not the comment for date and time
                        f.seek(0)
                    else:
                        dumpline = f.readline() # skip one extra line
                        dumpline = f.readline() # skip two extra line
                    oldrunlog = f.read()
            except IOError:
                QMessageBox.critical(self, "ERROR!", "Something went wrong :x\nPrinting file info for debugging...")
                print(f'File that failed to open: {frunlog}')
            if oldrunlog != texttowrite:
                answer = QMessageBox.question(self, "", f"Run log file already exist in this directory with a different text.\nOverwrite it anyway?", QMessageBox.Yes, QMessageBox.No)
                if answer == QMessageBox.No:
                    return

        if not texttowrite.strip() or texttowrite.strip() == self.standardlog.strip():
            return
            

        try:
            with open(frunlog,'w') as f:
                now = datetime.now()
                f.write('# Run log save time:\n')
                f.write(f'# {now}\n\n')
                f.write(texttowrite)
        except IOError:
            QMessageBox.critical(self, "ERROR!", "Could not save the run log")
            print(frunlog)


    def setAskRunLog(self):
       self.keep_ask_log = self.ui.askrunlog.isChecked()


    def closeRunLog(self):
        if not self.rlui.runlogfield.toPlainText().strip():
            self.rlui.runlogfield.setPlainText(self.standardlog)
        self.RunLog.close()
