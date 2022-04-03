# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1430, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1430, 750))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 575))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.table_widget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_widget.sizePolicy().hasHeightForWidth())
        self.table_widget.setSizePolicy(sizePolicy)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(0)
        self.table_widget.setRowCount(0)
        self.gridLayout.addWidget(self.table_widget, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputLabel.sizePolicy().hasHeightForWidth())
        self.inputLabel.setSizePolicy(sizePolicy)
        self.inputLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.inputLabel.setMaximumSize(QtCore.QSize(16777215, 28))
        self.inputLabel.setWordWrap(True)
        self.inputLabel.setObjectName("inputLabel")
        self.horizontalLayout_6.addWidget(self.inputLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 36))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 36))
        self.lineEdit.setToolTip("")
        self.lineEdit.setStyleSheet("padding-left: 10px;\n"
"padding-right: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(80, 36))
        self.clearButton.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(115, 115, 115);")
        self.clearButton.setShortcut("")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_5.addWidget(self.clearButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setMinimumSize(QtCore.QSize(160, 36))
        self.infoLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet("color: rgb(6, 172, 6);")
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout.addWidget(self.infoLabel)
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy)
        self.resultLabel.setMinimumSize(QtCore.QSize(0, 36))
        self.resultLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.resultLabel.setStyleSheet("padding-left: 10px;\n"
"padding-right: 10px;")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        self.horizontalLayout.addWidget(self.resultLabel)
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        self.timeLabel.setMinimumSize(QtCore.QSize(160, 36))
        self.timeLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalLayout.addWidget(self.timeLabel)
        self.scanTimelabel = QtWidgets.QLabel(self.centralwidget)
        self.scanTimelabel.setMinimumSize(QtCore.QSize(160, 0))
        self.scanTimelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scanTimelabel.setObjectName("scanTimelabel")
        self.horizontalLayout.addWidget(self.scanTimelabel)
        self.timeLeftLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLeftLabel.sizePolicy().hasHeightForWidth())
        self.timeLeftLabel.setSizePolicy(sizePolicy)
        self.timeLeftLabel.setMinimumSize(QtCore.QSize(180, 36))
        self.timeLeftLabel.setMaximumSize(QtCore.QSize(16777215, 36))
        self.timeLeftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLeftLabel.setObjectName("timeLeftLabel")
        self.horizontalLayout.addWidget(self.timeLeftLabel)
        spacerItem = QtWidgets.QSpacerItem(16, 36, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.saveLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveLabel.sizePolicy().hasHeightForWidth())
        self.saveLabel.setSizePolicy(sizePolicy)
        self.saveLabel.setMinimumSize(QtCore.QSize(340, 0))
        self.saveLabel.setMaximumSize(QtCore.QSize(10000, 28))
        self.saveLabel.setWordWrap(True)
        self.saveLabel.setObjectName("saveLabel")
        self.horizontalLayout_11.addWidget(self.saveLabel)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setToolTip("")
        self.saveButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(142, 12, 234);")
        self.saveButton.setShortcut("")
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_11.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.proxyButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyButton.sizePolicy().hasHeightForWidth())
        self.proxyButton.setSizePolicy(sizePolicy)
        self.proxyButton.setMinimumSize(QtCore.QSize(0, 36))
        self.proxyButton.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.proxyButton.setFont(font)
        self.proxyButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(115, 115, 115);")
        self.proxyButton.setShortcut("")
        self.proxyButton.setObjectName("proxyButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.proxyButton)
        self.horizontalLayout_2.addWidget(self.proxyButton)
        self.soundButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soundButton.sizePolicy().hasHeightForWidth())
        self.soundButton.setSizePolicy(sizePolicy)
        self.soundButton.setMinimumSize(QtCore.QSize(0, 36))
        self.soundButton.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.soundButton.setFont(font)
        self.soundButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(115, 115, 115);")
        self.soundButton.setShortcut("")
        self.soundButton.setObjectName("soundButton")
        self.buttonGroup.addButton(self.soundButton)
        self.horizontalLayout_2.addWidget(self.soundButton)
        self.autoExcelButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.autoExcelButton.sizePolicy().hasHeightForWidth())
        self.autoExcelButton.setSizePolicy(sizePolicy)
        self.autoExcelButton.setMinimumSize(QtCore.QSize(0, 36))
        self.autoExcelButton.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.autoExcelButton.setFont(font)
        self.autoExcelButton.setToolTipDuration(-1)
        self.autoExcelButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(115, 115, 115);")
        self.autoExcelButton.setShortcut("")
        self.autoExcelButton.setObjectName("autoExcelButton")
        self.buttonGroup.addButton(self.autoExcelButton)
        self.horizontalLayout_2.addWidget(self.autoExcelButton)
        self.horizontalLayout_2.setStretch(0, 28)
        self.horizontalLayout_2.setStretch(1, 28)
        self.horizontalLayout_2.setStretch(2, 44)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(0, 36))
        self.stopButton.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("background-color: rgb(239, 119, 21);\n"
"color: rgb(255, 255, 255);")
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_3.addWidget(self.stopButton)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(0, 36))
        self.startButton.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(6, 172, 6);\n"
"color: rgb(255, 255, 255);")
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_3.addWidget(self.startButton)
        self.horizontalLayout_3.setStretch(0, 50)
        self.horizontalLayout_3.setStretch(1, 50)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.horizontalLayout_10.setStretch(0, 60)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_10.setStretch(2, 35)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputLabel.setText(_translate("MainWindow", "Введите поисковой запрос:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "поисковый запрос"))
        self.clearButton.setText(_translate("MainWindow", "CLEAR"))
        self.infoLabel.setText(_translate("MainWindow", "информация"))
        self.resultLabel.setText(_translate("MainWindow", "результаты поиска (0/0)"))
        self.timeLabel.setText(_translate("MainWindow", "общее время 00:00:00"))
        self.scanTimelabel.setText(_translate("MainWindow", "время скана 00:00:00"))
        self.timeLeftLabel.setText(_translate("MainWindow", "оставшееся время 00:00:00"))
        self.saveLabel.setText(_translate("MainWindow", "Сохранить в .xlsx формате. Сохраненные данные можно найти в папке results в корневой папке парсера."))
        self.saveButton.setText(_translate("MainWindow", "SAVE"))
        self.proxyButton.setText(_translate("MainWindow", "PROXY OFF"))
        self.soundButton.setText(_translate("MainWindow", "SOUND OFF"))
        self.autoExcelButton.setToolTip(_translate("MainWindow", "auto start Excel on save on/off"))
        self.autoExcelButton.setText(_translate("MainWindow", "AUTO EXCEL OFF"))
        self.stopButton.setText(_translate("MainWindow", "СТОП"))
        self.startButton.setText(_translate("MainWindow", "СТАРТ"))
