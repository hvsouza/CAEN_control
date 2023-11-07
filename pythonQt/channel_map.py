#!/usr/bin/env python3
## ________________________________________ ##
## Author: Henrique Souza
## Filename: channel_map.py
## Created: 2023-11-07
## ________________________________________ ##


import os
from pathlib import Path
import sys

from ui_mainwindow import Ui_MainWindow
from ui_channel_map import Ui_ChannelMap

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import subprocess as sp
import csv

class ChannelMapper():
    ChannelMap:QtWidgets.QMainWindow
    ui:Ui_MainWindow
    cmui:Ui_ChannelMap

    def doneChannelMap(self):
        self.ChannelMap.close()

    def loadSearchMap(self):
        dirnow = self.ui.primary_name.text()
        mfile, mfilter = QtWidgets.QFileDialog.getOpenFileName(self, "Find Files", f'{self.default_path}/{dirnow}', "*.log")
        self.showChannelMap()

        if not mfile: # if nothing was selected, get out
            return

        self.loadChannelMap(mfile)

    def loadChannelMap(self, fmapchannel):
        chmap:dict
        with open(fmapchannel, newline='') as csvfile:
            linedump = csv.DictReader(csvfile, delimiter=',')
            for x in linedump:
                self.chmap[x['channel']] = x['name']
                self.chmapui[x['channel']].setText(x['name'])

    def cleanChannelMap(self):
        for k, v in self.chmapui.items():
            v.setText('')
