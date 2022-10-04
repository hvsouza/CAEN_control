#!/usr/bin/env python3

import os
from pathlib import Path
import sys

from ui_mainwindow import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def twinSample(self):
    val = self.ui.samplingRate_2.currentText()
    self.ui.samplingRate.setCurrentText(val)

def recompile(self):
    nwvfs = self.ui.nwvfs.text()
    if nwvfs == "":
        nwvfs = 10000

    passwrd = self.ui.passwrd.text()

    max_samplingRate = self.ui.adcMaximumRate.currentText()
    max_samplingRate = float(max_samplingRate.split(" ")[0])

    samplingRate = self.ui.samplingRate_2.currentText()
    samplingRate = float(samplingRate.split(" ")[0])

    factor = int(max_samplingRate/samplingRate)

    if factor == 0:
        QMessageBox.about(self,"ERROR!","ADC Nominal sampling should be higher or equal to Sampling rate !")
        return

    QMessageBox.about(self,"",f'Recompiling wavedump.\n\nSetting {nwvfs} as maximum for continuous writting.\n\nSampling rate set to {samplingRate} MSamples/s.\n\nCheck the terminal for sudo permissions, error messages and progress.')

    validate_sudo = f"printf {passwrd} | sudo -S -v"
    print("Validating...\n")
    result = os.system(validate_sudo)

    if result!=0:
        QMessageBox.about(self,"ERROR!","Error with sudo permissions, make sure you enter the correct password.\n\nType 'sudo -v' on the terminal.")
        print("Press enter to free the terminal...")
        return

    print("\n\n")
    recompile_command = f"bash ~/Documents/CAEN_Digitizer/recompile_wavedump.sh {nwvfs} {factor}"
    os.system(recompile_command)

    print("Press enter to free the terminal...")

    self.writeConfigFile(False);

    QMessageBox.about(self,"","Done!\n\nPlease restart wavedump.");