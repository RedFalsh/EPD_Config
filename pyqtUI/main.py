# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sun Nov 27 14:53:11 2016
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setObjectName("groupBox_9")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_9)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.pushButton_InfReadInformation = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_InfReadInformation.setObjectName("pushButton_InfReadInformation")
        self.horizontalLayout_9.addWidget(self.pushButton_InfReadInformation)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(self.groupBox_9)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.progressBarInfRead = QtWidgets.QProgressBar(self.groupBox_9)
        self.progressBarInfRead.setProperty("value", 0)
        self.progressBarInfRead.setObjectName("progressBarInfRead")
        self.horizontalLayout_9.addWidget(self.progressBarInfRead)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_9)
        self.label_27 = QtWidgets.QLabel(self.groupBox_9)
        self.label_27.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_21)
        self.label_3 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_22)
        self.label_26 = QtWidgets.QLabel(self.groupBox_9)
        self.label_26.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_23.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_23)
        self.label_25 = QtWidgets.QLabel(self.groupBox_9)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_24)
        self.label_24 = QtWidgets.QLabel(self.groupBox_9)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_25.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_25)
        self.label_28 = QtWidgets.QLabel(self.groupBox_9)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_26.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_26.setFont(font)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_26)
        self.label_20 = QtWidgets.QLabel(self.groupBox_9)
        self.label_20.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_29.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_29)
        self.label_21 = QtWidgets.QLabel(self.groupBox_9)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_30.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_30.setFont(font)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_30)
        self.gridLayout_2.addWidget(self.groupBox_9, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_OpenSerial = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OpenSerial.setEnabled(True)
        self.pushButton_OpenSerial.setObjectName("pushButton_OpenSerial")
        self.horizontalLayout_2.addWidget(self.pushButton_OpenSerial)
        self.comboBox_ComNum = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_ComNum.setObjectName("comboBox_ComNum")
        self.horizontalLayout_2.addWidget(self.comboBox_ComNum)
        self.pushButton_UpdateSerialShow = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_UpdateSerialShow.setObjectName("pushButton_UpdateSerialShow")
        self.horizontalLayout_2.addWidget(self.pushButton_UpdateSerialShow)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_7)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.LabelRole, spacerItem5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.pushButton_Style = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_Style.setObjectName("pushButton_Style")
        self.horizontalLayout_8.addWidget(self.pushButton_Style)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.pushButton_InfWriteInformation = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_InfWriteInformation.setObjectName("pushButton_InfWriteInformation")
        self.horizontalLayout_8.addWidget(self.pushButton_InfWriteInformation)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.progressBarInfWrite = QtWidgets.QProgressBar(self.groupBox_7)
        self.progressBarInfWrite.setProperty("value", 0)
        self.progressBarInfWrite.setObjectName("progressBarInfWrite")
        self.horizontalLayout_8.addWidget(self.progressBarInfWrite)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_8)
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_19 = QtWidgets.QLabel(self.groupBox_7)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_14 = QtWidgets.QLabel(self.groupBox_7)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_12 = QtWidgets.QLabel(self.groupBox_7)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_18 = QtWidgets.QLabel(self.groupBox_7)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_15 = QtWidgets.QLabel(self.groupBox_7)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_17)
        self.label_17 = QtWidgets.QLabel(self.groupBox_7)
        self.label_17.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_18)
        self.gridLayout_2.addWidget(self.groupBox_7, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_9.setTitle(_translate("MainWindow", "读取信息"))
        self.pushButton_InfReadInformation.setText(_translate("MainWindow", "获取信息"))
        self.label_10.setText(_translate("MainWindow", "读取进度："))
        self.label_27.setText(_translate("MainWindow", "仪器编号"))
        self.label_3.setText(_translate("MainWindow", "用户编号"))
        self.label_26.setText(_translate("MainWindow", "剂量阈值(uSv)"))
        self.label_25.setText(_translate("MainWindow", "剂量率阈值(uSv)"))
        self.label_24.setText(_translate("MainWindow", "时间间隔存储(s)"))
        self.label_28.setText(_translate("MainWindow", "仪器日期"))
        self.label_20.setText(_translate("MainWindow", "累积剂量清零"))
        self.label_21.setText(_translate("MainWindow", "仪器出厂编号"))
        self.groupBox.setTitle(_translate("MainWindow", "串口操作"))
        self.pushButton_OpenSerial.setText(_translate("MainWindow", "打开串口"))
        self.pushButton_UpdateSerialShow.setText(_translate("MainWindow", "更新串口"))
        self.groupBox_7.setTitle(_translate("MainWindow", "配置信息"))
        self.pushButton_Style.setText(_translate("MainWindow", "参考格式"))
        self.pushButton_InfWriteInformation.setText(_translate("MainWindow", "开始配置"))
        self.label_9.setText(_translate("MainWindow", "配置进度："))
        self.label_16.setText(_translate("MainWindow", "仪器编号"))
        self.label_2.setText(_translate("MainWindow", "用户编号"))
        self.label_19.setText(_translate("MainWindow", "剂量阈值(uSv)"))
        self.label_14.setText(_translate("MainWindow", "剂量率阈值(uSv)"))
        self.label_12.setText(_translate("MainWindow", "时间间隔存储(s)"))
        self.label_18.setText(_translate("MainWindow", "仪器日期"))
        self.label_15.setText(_translate("MainWindow", "累积剂量清零"))
        self.label_17.setText(_translate("MainWindow", "仪器出厂编号"))

