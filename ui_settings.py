from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(305, 380)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.fraSettings = QFrame(Settings)
        self.fraSettings.setObjectName(u"fraSettings")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fraSettings.sizePolicy().hasHeightForWidth())
        self.fraSettings.setSizePolicy(sizePolicy)
        self.fraSettings.setFrameShape(QFrame.StyledPanel)
        self.fraSettings.setFrameShadow(QFrame.Raised)
        self.fraSettings.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.fraSettings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupSignalGenerator = QGroupBox(self.fraSettings)
        self.groupSignalGenerator.setObjectName(u"groupSignalGenerator")
        self.formLayout = QFormLayout(self.groupSignalGenerator)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupSignalGenerator)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(self.groupSignalGenerator)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.edtSDGIP = QLineEdit(self.groupSignalGenerator)
        self.edtSDGIP.setObjectName(u"edtSDGIP")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edtSDGIP)

        self.radioPydatacq = QRadioButton(self.groupSignalGenerator)
        self.radioPydatacq.setObjectName(u"radioPydatacq")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.radioPydatacq)

        self.radioPyvisa = QRadioButton(self.groupSignalGenerator)
        self.radioPyvisa.setObjectName(u"radioPyvisa")
        self.radioPyvisa.setChecked(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.radioPyvisa)

        self.edtSDGPort = QLineEdit(self.groupSignalGenerator)
        self.edtSDGPort.setObjectName(u"edtSDGPort")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edtSDGPort)

        self.label_5 = QLabel(self.groupSignalGenerator)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.edtQueryDelay = QLineEdit(self.groupSignalGenerator)
        self.edtQueryDelay.setObjectName(u"edtQueryDelay")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edtQueryDelay)


        self.verticalLayout_2.addWidget(self.groupSignalGenerator)

        self.groupOscilloscope = QGroupBox(self.fraSettings)
        self.groupOscilloscope.setObjectName(u"groupOscilloscope")
        self.formLayout_2 = QFormLayout(self.groupOscilloscope)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.groupOscilloscope)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_4 = QLabel(self.groupOscilloscope)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.edtSDSIP = QLineEdit(self.groupOscilloscope)
        self.edtSDSIP.setObjectName(u"edtSDSIP")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.edtSDSIP)

        self.edtSDSPort = QLineEdit(self.groupOscilloscope)
        self.edtSDSPort.setObjectName(u"edtSDSPort")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.edtSDSPort)


        self.verticalLayout_2.addWidget(self.groupOscilloscope)

        self.fraButtons = QFrame(self.fraSettings)
        self.fraButtons.setObjectName(u"fraButtons")
        self.fraButtons.setFrameShape(QFrame.NoFrame)
        self.fraButtons.setFrameShadow(QFrame.Raised)
        self.fraButtons.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnCancel = QPushButton(self.fraButtons)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnOk = QPushButton(self.fraButtons)
        self.btnOk.setObjectName(u"btnOk")

        self.horizontalLayout.addWidget(self.btnOk)


        self.verticalLayout_2.addWidget(self.fraButtons)


        self.verticalLayout.addWidget(self.fraSettings)

        QWidget.setTabOrder(self.edtSDGIP, self.edtSDGPort)
        QWidget.setTabOrder(self.edtSDGPort, self.edtQueryDelay)
        QWidget.setTabOrder(self.edtQueryDelay, self.radioPyvisa)
        QWidget.setTabOrder(self.radioPyvisa, self.radioPydatacq)
        QWidget.setTabOrder(self.radioPydatacq, self.edtSDSIP)
        QWidget.setTabOrder(self.edtSDSIP, self.edtSDSPort)
        QWidget.setTabOrder(self.edtSDSPort, self.btnOk)
        QWidget.setTabOrder(self.btnOk, self.btnCancel)

        self.retranslateUi(Settings)
        self.btnCancel.clicked.connect(Settings.close)
        self.btnOk.clicked.connect(Settings.accept)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.groupSignalGenerator.setTitle(QCoreApplication.translate("Settings", u"Signal Generator", None))
        self.label.setText(QCoreApplication.translate("Settings", u"IP", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"port", None))
        self.radioPydatacq.setText(QCoreApplication.translate("Settings", u"Use pydatacq", None))
        self.radioPyvisa.setText(QCoreApplication.translate("Settings", u"Use pyvisa", None))
        self.edtSDGPort.setText("")
        self.label_5.setText(QCoreApplication.translate("Settings", u"Query delay (s)", None))
        self.groupOscilloscope.setTitle(QCoreApplication.translate("Settings", u"Oscillosope", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"IP", None))
        self.label_4.setText(QCoreApplication.translate("Settings", u"port", None))
        self.btnCancel.setText(QCoreApplication.translate("Settings", u"Cancel", None))
        self.btnOk.setText(QCoreApplication.translate("Settings", u"OK", None))
    # retranslateUi

