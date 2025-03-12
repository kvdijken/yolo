# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutQYAPVs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(650, 469)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(Dialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClose = QPushButton(self.frame)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.btnClose.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("Dialog", u"**Yolo: **\n"
"\n"
"**Distortion Analysis with a Signal generator and Oscilloscope**\n"
"\n"
"FM Homelab, K. van Dijken\n"
"\n"
"February 2025\n"
"\n"
"version 0.9\n"
"\n"
"With Yolo you can perform distortion analysis on a signal obtained from an\n"
"oscilloscope. The signal can be fed to the oscilloscope in various ways:\n"
"\n"
"- from a unknown source\n"
"\n"
"- from a signal generator programmed by Yolo\n"
"\n"
"When a signal generator programmed by Yolo is used, the signal can be\n"
"\n"
"- a CW (continuous wave) signal\n"
"\n"
"- an AM modulated signal\n"
"\n"
"- an FM modulated signal\n"
"\n"
"For AM and FM modulated signals the signal from the signal generator has to be\n"
"fed to a demodulator whose output is connected to the input of the oscilloscope.\n"
"\n"
"For any type of signal (CW, AM modulated, FM modulated) a frequency sweep can\n"
"be programmed from Yolo. This allows the THD to be analysed over a frequency\n"
"range. For a CW signal, the CW frequency will be swept. For AM and FM modulated\n"
""
                        "signals the modulation frequency will be swept.\n"
"\n"
"For AM and FM modulated signals, the carrier frequency and amplitude can be\n"
"set. For AM the modulation depth can be set. For FM modulation the frequency\n"
"deviation can be set.\n"
"\n"
"For THD analysis you can set the number of harmonics to take into account, as\n"
"well as the minimum signal level of harmonics. Also you can average THD\n"
"calculation over a number of samples.\n"
"\n"
"Yolo proves several views of the provided waveform. \n"
"\n"
"- a plot of the full waveform\n"
"\n"
"- a 2-period plot of the wave\n"
"\n"
"- a FFT plot of the full wave\n"
"\n"
"- a display of THD, s0 and s1 (in fixed mode)\n"
"\n"
"- a plot of THD and s0 versus frequency (in swept mode)\n"
"\n"
" \n"
"\n"
"Sources on github: https://github.com/kvdijken/yolo\n"
"\n"
"Only tested with:\n"
"\n"
"- Siglent SDS1202X-E oscilloscope\n"
"\n"
"- Siglent SDG1032X signal generator\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Cantarell'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:7px; margin-bottom:7px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">Yolo: </span></p>\n"
"<p align=\"center\" style=\" margin-top:7px; margin-bottom:7px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Distortion Analysis with a Signal generator and Oscilloscope</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FM Homelab, K. van Dijken</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">February 2025</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">version 0.9</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">With Yolo you can perform distortion analysis on a signal obtained from an oscilloscope. The signal can be f"
                        "ed to the oscilloscope in various ways:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- from a unknown source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- from a signal generator programmed by Yolo</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When a signal generator programmed by Yolo is used, the signal can be</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- a CW (continuous wave) signal</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- an AM modulated signal</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- an FM modulated signal</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For AM and FM modulated signals the signal from the signal generator has to be fed to a demodulator whose output is connected to the input of the oscilloscope.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; ma"
                        "rgin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For any type of signal (CW, AM modulated, FM modulated) a frequency sweep can be programmed from Yolo. This allows the THD to be analysed over a frequency range. For a CW signal, the CW frequency will be swept. For AM and FM modulated signals the modulation frequency will be swept.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For AM and FM modulated signals, the carrier frequency and amplitude can be set. For AM the modulation depth can be set. For FM modulation the frequency deviation can be set.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-b"
                        "ottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For THD analysis you can set the number of harmonics to take into account, as well as the minimum signal level of harmonics. Also you can average THD calculation over a number of samples.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Yolo proves several views of the provided waveform. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- a plot of the full waveform</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text"
                        "-indent:0px;\">- a 2-period plot of the wave</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- a FFT plot of the full wave</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- a display of THD, s<span style=\" vertical-align:sub;\">0</span> and s<span style=\" vertical-align:sub;\">1</span> (in fixed mode)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- a plot of THD and s<span style=\" vertical-align:sub;\">0</span> versus frequency (in swept mode)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" vertical-align:super;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sources on github: http"
                        "s://github.com/kvdijken/yolo</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Only tested with:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Siglent SDS1202X-E oscilloscope</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Siglent SDG1032X signal generator</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btnClose.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

