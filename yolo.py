import os
import sys
import asyncio
import json

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QFileDialog,
    QVBoxLayout,
    QMessageBox,
)
from PySide6.QtCore import QSettings
from PySide6 import QtCore
from PySide6.QtGui import QTextCursor

import qasync
import quantiphy

from ui_yolo import Ui_MainWindow
import ui_about, ui_settings
from fftwidget import FFTWidget
from thdwidget import THDWidget
from oscwidget import OscWidget
import engine as engine
import matplotlib_rc


company = "FM Homelab"
name = "yolo"

settingGroupSDG = "sdg"
settingsSDGIP = "ip"
settingSDGPort = "port"
settingSDGQueryDelay = "query_delay"
settingUseVisa = "use_visa"
settingGroupSDS = "sds"
settingSDSIP = "ip"
settingSDSPort = "port"
settingGroupTHD = "THD"
settingsTHDDirectory = "directory"


#
def bool2QCheckState(b):
    if b:
        return QtCore.Qt.CheckState.Checked
    else:
        return QtCore.Qt.CheckState.Unchecked


#
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.btnStart.clicked.connect(self.start_onclick)
        self.ui.btnStop.clicked.connect(self.stop_onclick)

        # Osc
        oscLayout = QVBoxLayout()
        self.ui.fraOsc2.setLayout(oscLayout)
        self.oscWidget = OscWidget()
        oscLayout.addWidget(self.oscWidget.canvas)

        # Zoom
        zoomLayout = QVBoxLayout()
        self.ui.fraZoom2.setLayout(zoomLayout)
        self.zoomWidget = OscWidget()
        zoomLayout.addWidget(self.zoomWidget.canvas)

        # FFT
        fftLayout = QVBoxLayout()
        self.ui.fraFFT2.setLayout(fftLayout)
        self.fftWidget = FFTWidget()
        fftLayout.addWidget(self.fftWidget.canvas)

        # THD vs Frequency plot
        thdLayout = QVBoxLayout()
        self.ui.pageSweep.setLayout(thdLayout)
        self.thdWidget = THDWidget()
        thdLayout.addWidget(self.thdWidget.canvas)

        # Set default values
        self.setControls()

        # Connect signals
        self.ui.tabSDGFixedSweep.currentChanged.connect(
            self.ui.stackTHD.setCurrentIndex
        )
        self.ui.tabSDGFixedSweep.currentChanged.connect(self.enablePlot)
        self.ui.checkUseSDG.stateChanged.connect(self.useSDGChanged)
        self.ui.actionOpenLRUControls.triggered.connect(self.openLRUControls)
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionSettings.triggered.connect(self.openSettings)

        self.readSettings()

    #
    def setControls(self):
        """
        This will fill the UI-controls with the 
        currently active values from the engine.        
        """
        
        def q(x):
            return quantiphy.Quantity(x).render()

        self.ui.checkUseSDG.setCheckState(bool2QCheckState(engine.sdgUseSDG()))
        self.ui.cboSDG_ch.setCurrentText(str(engine.sdgChannel()))
        self.ui.tabSDGModulation.setCurrentIndex(engine.sdgModulationToTabIndex[engine.sdgModulation()])
        self.ui.edtCW_amplitude.setText(q(engine.sdgCWAmplitude()))
        self.ui.edtAM_freq.setText(q(engine.sdgAMFrequency()))
        self.ui.edtAM_amplitude.setText(q(engine.sdgAMAmplitude()))
        self.ui.edtAM_modDepth.setText(q(engine.sdgAMModulationDepth()))
        self.ui.edtFM_freq.setText(q(engine.sdgFMFrequency()))
        self.ui.edtFM_amplitude.setText(q(engine.sdgFMAmplitude()))
        self.ui.edtFM_freqDev.setText(q(engine.sdgFMFrequencyDeviation()))
        self.ui.tabSDGFixedSweep.setCurrentIndex(engine.sdgFixSweepToTabIndex[engine.sdgFixSweep()])
        self.ui.edtSDGFixed_f0.setText(q(engine.sdgFixedF0()))
        self.ui.edtSDGSweep_minFreq.setText(q(engine.sdgSweepMinimumFrequency()))
        self.ui.edtSDGSweep_maxFreq.setText(q(engine.sdgSweepMaximumFrequency()))
        self.ui.edtSDGSweep_step.setText(q(engine.sdgSweepStep()))
        self.ui.cboSDS_ch.setCurrentText(str(engine.oscChannel()))
        self.ui.checkSDS_autoVertical.setCheckState(
            bool2QCheckState(engine.sdsAutoAdjustVertical())
        )
        self.ui.checkSDS_autoHorizontal.setCheckState(
            bool2QCheckState(engine.sdsAutoAdjustTimebase())
        )
        self.ui.edtSDSPeriods.setText(q(engine.sdsPeriods()))
        self.ui.edtTHDHarmonics.setText(q(engine.thdHarmonics()))
        self.ui.edtTHDFloor.setText(q(engine.thdFloor()))
        self.ui.edtTHDAverage.setText(q(engine.thdAverage()))
        self.ui.edtTHDAmplitude.setCheckState(
            bool2QCheckState(engine.thdPlotAmplitude())
        )
        self.ui.edtFFTPlotMinY.setText(q(engine.plotMinY()))
        self.ui.edtFFTPlotMaxY.setText(q(engine.plotMaxY()))
        self.enablePlot()

    #
    @QtCore.Slot()
    def openLRUControls(self):
        dir = os.path.dirname(QSettings(company, name).fileName())
        file = f"{dir}/lru_controls.json"
        if os.path.isfile(file):
            try:
                with open(file, "r") as file:
                    engine.active = json.load(file)
                self.setControls()
            except Exception as e:
                print(e)

    #
    def saveLRUControls(self):
        try:
            dir = os.path.dirname(QSettings(company, name).fileName())
            file = f"{dir}/lru_controls.json"
            with open(file, "w") as file:
                json.dump(engine.active, file)
        except Exception as e:
            print(e)

    #
    @QtCore.Slot()
    def useSDGChanged(self):
        useSDG = engine.qCheckState2Bool(self.ui.checkUseSDG.checkState())
        self.ui.cboSDG_ch.setEnabled(useSDG)
        self.ui.tabSDGModulation.setEnabled(useSDG)
        self.ui.tabSDGFixedSweep.setTabEnabled(1, useSDG)
        return

    @QtCore.Slot()
    def quit(self):
        self.saveLRUControls()
        print("Quit by Menu")
        os._exit(0)

    @QtCore.Slot()
    def enablePlot(self):
        """
        This will enable or disable the THD plot
        according to the current active tab
        fixed / swept operation.
        """
        fixed = self.ui.tabSDGFixedSweep.currentIndex() == 0
        self.ui.groupTHDPlot.setVisible(not fixed)

    #
    def readSettings(self):
        """
        This will read the settings from the QSettings.
        These are settings which do not change often
        like:
        - IP address of the SDG
        - Port of the SDG
        - query delay when sending commands
          to the SDG.
        - IP address of the SDS
        - Port of the SDS
        - Directory of the THD files
        - whether to use PyVisa or pydatacq
        """
        
        def valueToBool(value):
            return value.lower() == "true" if isinstance(value, str) else bool(value)

        settings = QSettings(company, name)
        settings.beginGroup(settingGroupSDG)
        engine.sdgIP = settings.value(settingsSDGIP, defaultValue=engine.sdgIP)
        try:
            engine.sdgPort = int(
                settings.value(settingSDGPort, defaultValue=engine.sdgPort)
            )
        except:
            engine.sdgPort = None
        try:
            engine.sdgQueryDelay = float(
                settings.value(settingSDGQueryDelay, defaultValue=engine.sdgQueryDelay)
            )
        except:
            engine.sdgQueryDelay = None
        engine.sdgUseVisa = valueToBool(
            settings.value(settingUseVisa, defaultValue=engine.sdgUseVisa)
        )
        settings.endGroup()
        settings.beginGroup(settingGroupSDS)
        engine.sdsIP = settings.value(settingSDSIP, defaultValue=engine.sdsIP)
        try:
            engine.sdsPort = int(
                settings.value(settingSDSPort, defaultValue=engine.sdsPort)
            )
        except:
            engine.sdsPort = None
        settings.endGroup()
        settings.beginGroup(settingGroupTHD)
        try:
            engine.thdDirectory = settings.value(
                settingsTHDDirectory, defaultValue=engine.thdDirectory
            )
        except:
            engine.thdDirectory = None
        settings.endGroup()

    @QtCore.Slot()
    def openSettings(self):
        """
        Will open the settings dialog.
        """
        
        class Settings(QDialog, ui_settings.Ui_Settings):

            def __init__(self, *args, **kwargs):
                QDialog.__init__(self, *args, **kwargs)
                self.setupUi(self)
                self.btnCancel.clicked.connect(self.reject)
                self.edtSDGIP.setText(engine.sdgIP)
                self.edtSDGPort.setText(str(engine.sdgPort))
                self.edtQueryDelay.setText(str(engine.sdgQueryDelay))
                self.radioPyvisa.setChecked(engine.sdgUseVisa)
                self.radioPydatacq.setChecked(not engine.sdgUseVisa)
                self.edtSDSIP.setText(engine.sdsIP)
                self.edtSDSPort.setText(str(engine.sdsPort))
                self.lblDirectory.setText(engine.thdDirectory)
                self.btnOk.clicked.connect(self.save)
                self.btnBrowseDirectory.clicked.connect(self.browseDirectory)

            def browseDirectory(self):
                directory = QFileDialog.getExistingDirectory(
                    parent=self, caption="Select Directory", dir=engine.thdDirectory
                )
                self.lblDirectory.setText(directory)

            def save(self):
                engine.sdgIP = self.edtSDGIP.text()
                engine.sdgPort = int(self.edtSDGPort.text())
                engine.sdgQueryDelay = float(self.edtQueryDelay.text())
                engine.sdgUseVisa = self.radioPyvisa.isChecked()
                engine.sdsIP = self.edtSDSIP.text()
                engine.sdsPort = int(self.edtSDSPort.text())
                engine.thdDirectory = self.lblDirectory.text()

                # Save settings
                settings = QSettings(company, name)
                settings.beginGroup(settingGroupSDG)
                settings.setValue(settingsSDGIP, engine.sdgIP)
                settings.setValue(settingSDGPort, engine.sdgPort)
                settings.setValue(settingSDGQueryDelay, float(engine.sdgQueryDelay))
                settings.setValue(settingUseVisa, engine.sdgUseVisa)
                settings.endGroup()
                settings.beginGroup(settingGroupSDS)
                settings.setValue(settingSDSIP, engine.sdsIP)
                settings.setValue(settingSDSPort, engine.sdsPort)
                settings.endGroup()
                settings.beginGroup(settingGroupTHD)
                settings.setValue(settingsTHDDirectory, engine.thdDirectory)
                settings.endGroup()

        self._settings = Settings()
        self._settings.exec()

    @QtCore.Slot()
    def about(self):
        """
        Will show the About dialog.
        """
        self._windowAbout = QDialog()
        ui = ui_about.Ui_Dialog()
        ui.setupUi(self._windowAbout)
        self._windowAbout.exec()

    #
    async def waitForFinish(self, eventFinish: asyncio.Event):
        """
        Wait for the engine to finish. When
        finished enable the parameter screen
        again.
        """
        await eventFinish.wait()
        self.enableControls(True)

    _tasks = set()

    @QtCore.Slot()
    def start_onclick(self):
        started, b = engine.start(self)
        if not started:
            # Show an error message
            err = b
            button = QMessageBox.critical(
                self, "Start Error", err, buttons=QMessageBox.Ok
            )
        else:
            eventRunFinished = b
            task = asyncio.create_task(
                self.waitForFinish(eventRunFinished), name="waitForFinish"
            )
            self._tasks.add(task)
            self.enableControls(False)

    @QtCore.Slot()
    def stop_onclick(self):
        stopped, err = engine.stop(self)
        if not stopped:
            # Show an error message
            button = QMessageBox.critical(
                self, "Stop Error", err, buttons=QMessageBox.Ok
            )

    #
    def enableControls(self, enabled):
        """
        Enables or disables the user controls.
        """
        self.ui.btnStart.setEnabled(enabled)
        self.ui.btnStop.setEnabled(not enabled)
        self.ui.widgetControls.setEnabled(enabled)

    #
    def print(self, text):
        """
        Prints a text in the communications pane.
        """
        comm = self.ui.textComm
        comm.moveCursor(QTextCursor.End)
        comm.insertPlainText(text)
        sb = comm.verticalScrollBar()
        sb.setValue(sb.maximum())


# @QtCore.Slot()
def exitHandler():
    close.set_result(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(exitHandler)

    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow()
    window.show()

    close = loop.create_future()

    with loop:
        loop.run_until_complete(close)

    window.saveLRUControls()
    print("Done")
    os._exit(0)
