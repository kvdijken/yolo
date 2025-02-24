import os
import sys
import asyncio

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QVBoxLayout,
    QMessageBox,
    QWidget,
)
from PySide6.QtCore import QSettings
from PySide6 import QtCore
from PySide6.QtGui import QTextCursor

import qasync

from ui_yolo import Ui_MainWindow
import ui_about, ui_settings
from fftwidget import FFTWidget
from thdwidget import THDWidget
from oscwidget import OscWidget
import engine as engine


company = "FM Homelab"
name = "yolo"

settingGroupSDG = 'sdg'
settingsSDGIP = "ip"
settingSDGPort = "port"
settingSDGQueryDelay = 'query_delay'
settingUseVisa = "use_visa"
settingGroupSDS = 'sds'
settingSDSIP = "ip"
settingSDSPort = "port"


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
        self.ui.cboSDG_ch.setCurrentText(str(engine.sdgChannel()))
        self.ui.edtCW_amplitude.setText(str(engine.sdgCWAmplitude()))
        self.ui.edtAM_freq.setText(engine.sdgAMFrequency())
        self.ui.edtAM_amplitude.setText(str(engine.SDGAMAmplitude()))
        self.ui.edtAM_modDepth.setText(str(engine.SDGAMModulationDepth()))
        self.ui.edtFM_freq.setText(str(engine.SDGFMFrequency()))
        self.ui.edtFM_amplitude.setText(str(engine.SDGFMAmplitude()))
        self.ui.edtFM_freqDev.setText(str(engine.SDGFMFrequencyDeviation()))
        self.ui.edtSDGFixed_f0.setText(str(engine.SDGFixedF0()))
        self.ui.edtSDGSweep_minFreq.setText(str(engine.SDGSweepMinimumFrequency()))
        self.ui.edtSDGSweep_maxFreq.setText(str(engine.SDGSweepMaximumFrequency()))
        self.ui.edtSDGSweep_step.setText(str(engine.SDGSweepStep()))
        self.ui.cboSDS_ch.setCurrentText(str(engine.oscChannel()))
        self.ui.checkSDS_autoVertical.setCheckState(
            bool2QCheckState(engine.sdsAutoAdjustVertical())
        )
        self.ui.checkSDS_autoHorizontal.setCheckState(
            bool2QCheckState(engine.sdsAutoAdjustTimebase())
        )
        self.ui.edtSDSPeriods.setText(str(engine.sdsPeriods()))
        self.ui.edtTHDHarmonics.setText(str(engine.thdHarmonics()))
        self.ui.edtTHDFloor.setText(str(engine.thdFloor()))
        self.ui.edtTHDAverage.setText(str(engine.thdAverage()))
        self.ui.edtTHDAmplitude.setCheckState(
            bool2QCheckState(engine.thdPlotAmplitude())
        )
        self.ui.edtFFTPlotMinY.setText(str(engine.plotMinY()))
        self.ui.edtFFTPlotMaxY.setText(str(engine.plotMaxY()))

        self.ui.tabSDGFixedSweep.currentChanged.connect(
            self.ui.stackTHD.setCurrentIndex
        )
        self.ui.tabSDGFixedSweep.currentChanged.connect(self.enablePlot)
        self.ui.checkUseSDG.stateChanged.connect(self.useSDGChanged)

        self.enablePlot()

        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionSettings.triggered.connect(self.openSettings)
        self.loop = loop
        
        self.readSettings()
        

    @QtCore.Slot()
    def useSDGChanged(self):
        useSDG = engine.qCheckState2Bool(self.ui.checkUseSDG.checkState())
        self.ui.cboSDG_ch.setEnabled(useSDG)
        self.ui.tabSDGModulation.setEnabled(useSDG)
        self.ui.tabSDGFixedSweep.setTabEnabled(1, useSDG)
        return

    @QtCore.Slot()
    def quit(self):
        self.writeSettings()
        print("Done")
        os._exit(0)

    @QtCore.Slot()
    def enablePlot(self):
        fixed = self.ui.tabSDGFixedSweep.currentIndex() == 0
        self.ui.groupTHDPlot.setVisible(not fixed)

    def readSettings(self):
        
        def valueToBool(value):
            return value.lower() == 'true' if isinstance(value, str) else bool(value)        
        
        settings = QSettings(company,name)
        settings.beginGroup(settingGroupSDG)
        engine.sdgIP = settings.value(settingsSDGIP,defaultValue=engine.sdgIP)
        engine.sdgPort = int(settings.value(settingSDGPort,defaultValue=engine.sdgPort))
        engine.sdgQueryDelay = float(settings.value(settingSDGQueryDelay,defaultValue=engine.sdgQueryDelay))
        engine.sdgUseVisa = valueToBool(settings.value(settingUseVisa,defaultValue=engine.sdgUseVisa))
        settings.endGroup()
        settings.beginGroup(settingGroupSDS)
        engine.sdsIP = settings.value(settingSDSIP,defaultValue=engine.sdsIP)
        engine.sdsPort = int(settings.value(settingSDSPort,defaultValue=engine.sdsPort))
        settings.endGroup()
    
    @QtCore.Slot()
    def openSettings(self):
        
        class Settings(QDialog, ui_settings.Ui_Settings):
            
            def __init__(self,*args,**kwargs):
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
                self.btnOk.clicked.connect(self.save)
            
            def save(self):
                engine.sdgIP = self.edtSDGIP.text()
                engine.sdgPort = int(self.edtSDGPort.text())
                engine.sdgQueryDelay = float(self.edtQueryDelay.text())
                engine.sdgUseVisa = self.radioPyvisa.isChecked()
                engine.sdsIP = self.edtSDSIP.text()
                engine.sdsPort = int(self.edtSDSPort.text())
                
                # Save settings
                settings = QSettings(company,name)
                settings.beginGroup(settingGroupSDG)
                settings.setValue(settingsSDGIP,engine.sdgIP)
                settings.setValue(settingSDGPort,engine.sdgPort)
                settings.setValue(settingSDGQueryDelay,float(engine.sdgQueryDelay))
                settings.setValue(settingUseVisa,engine.sdgUseVisa)
                settings.endGroup()
                settings.beginGroup(settingGroupSDS)
                settings.setValue(settingSDSIP,engine.sdsIP)
                settings.setValue(settingSDSPort,engine.sdsPort)
                settings.endGroup()
                
        self._settings = Settings()
        self._settings.show()

        
    @QtCore.Slot()
    def about(self):
        self._windowAbout = QMainWindow()
        ui = ui_about.Ui_MainWindow()
        ui.setupUi(self._windowAbout)
        self._windowAbout.show()

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
    print("Done")
    os._exit(0)
