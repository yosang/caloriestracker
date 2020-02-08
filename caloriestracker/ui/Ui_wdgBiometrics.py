# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgBiometrics.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgBiometrics(object):
    def setupUi(self, wdgBiometrics):
        wdgBiometrics.setObjectName("wdgBiometrics")
        wdgBiometrics.resize(1012, 669)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(wdgBiometrics)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lbl = QtWidgets.QLabel(wdgBiometrics)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_6.addWidget(self.lbl)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(wdgBiometrics)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rad20days = QtWidgets.QRadioButton(self.groupBox)
        self.rad20days.setChecked(True)
        self.rad20days.setAutoExclusive(True)
        self.rad20days.setObjectName("rad20days")
        self.verticalLayout.addWidget(self.rad20days)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radMonth = QtWidgets.QRadioButton(self.groupBox)
        self.radMonth.setObjectName("radMonth")
        self.horizontalLayout.addWidget(self.radMonth)
        self.wdgYM = wdgYearMonth(self.groupBox)
        self.wdgYM.setObjectName("wdgYM")
        self.horizontalLayout.addWidget(self.wdgYM)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.tblBiometrics = myQTableWidget(wdgBiometrics)
        self.tblBiometrics.setObjectName("tblBiometrics")
        self.verticalLayout_4.addWidget(self.tblBiometrics)
        self.lblFound = QtWidgets.QLabel(wdgBiometrics)
        self.lblFound.setObjectName("lblFound")
        self.verticalLayout_4.addWidget(self.lblFound)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(wdgBiometrics)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_4.addWidget(self.line)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layTab = QtWidgets.QVBoxLayout()
        self.layTab.setObjectName("layTab")
        self.tabWidget = QtWidgets.QTabWidget(wdgBiometrics)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layWeight = QtWidgets.QVBoxLayout()
        self.layWeight.setObjectName("layWeight")
        self.verticalLayout_2.addLayout(self.layWeight)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layHeight = QtWidgets.QVBoxLayout()
        self.layHeight.setObjectName("layHeight")
        self.horizontalLayout_2.addLayout(self.layHeight)
        self.tabWidget.addTab(self.tab_2, "")
        self.layTab.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.layTab)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(wdgBiometrics)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cmbChart = QtWidgets.QComboBox(wdgBiometrics)
        self.cmbChart.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbChart.setObjectName("cmbChart")
        self.cmbChart.addItem("")
        self.cmbChart.addItem("")
        self.cmbChart.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbChart)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.actionBiometricsNew = QtWidgets.QAction(wdgBiometrics)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBiometricsNew.setIcon(icon)
        self.actionBiometricsNew.setObjectName("actionBiometricsNew")
        self.actionBiometricsDelete = QtWidgets.QAction(wdgBiometrics)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/caloriestracker/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBiometricsDelete.setIcon(icon1)
        self.actionBiometricsDelete.setObjectName("actionBiometricsDelete")
        self.actionBiometricsEdit = QtWidgets.QAction(wdgBiometrics)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/caloriestracker/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBiometricsEdit.setIcon(icon2)
        self.actionBiometricsEdit.setObjectName("actionBiometricsEdit")

        self.retranslateUi(wdgBiometrics)
        self.tabWidget.setCurrentIndex(0)
        self.cmbChart.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(wdgBiometrics)

    def retranslateUi(self, wdgBiometrics):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgBiometrics", "Your biometric information"))
        self.groupBox.setTitle(_translate("wdgBiometrics", "Select an option"))
        self.rad20days.setText(_translate("wdgBiometrics", "Show last 20 days"))
        self.radMonth.setText(_translate("wdgBiometrics", "Select a month"))
        self.lblFound.setText(_translate("wdgBiometrics", "Registers found"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("wdgBiometrics", "Weight"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("wdgBiometrics", "Height"))
        self.label.setText(_translate("wdgBiometrics", "Show in chart"))
        self.cmbChart.setItemText(0, _translate("wdgBiometrics", "All registers"))
        self.cmbChart.setItemText(1, _translate("wdgBiometrics", "Last year"))
        self.cmbChart.setItemText(2, _translate("wdgBiometrics", "Last three years"))
        self.actionBiometricsNew.setText(_translate("wdgBiometrics", "New biometric information"))
        self.actionBiometricsNew.setToolTip(_translate("wdgBiometrics", "New biometric information"))
        self.actionBiometricsDelete.setText(_translate("wdgBiometrics", "Delete biometric information"))
        self.actionBiometricsDelete.setToolTip(_translate("wdgBiometrics", "Delete biometric information"))
        self.actionBiometricsEdit.setText(_translate("wdgBiometrics", "Edit biometric information"))
        self.actionBiometricsEdit.setToolTip(_translate("wdgBiometrics", "Edit biometric information"))
from caloriestracker.ui.myqtablewidget import myQTableWidget
from caloriestracker.ui.wdgYearMonth import wdgYearMonth
import caloriestracker.images.caloriestracker_rc
