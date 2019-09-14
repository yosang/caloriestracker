# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/frmBiometricsAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmBiometricsAdd(object):
    def setupUi(self, frmBiometricsAdd):
        frmBiometricsAdd.setObjectName("frmBiometricsAdd")
        frmBiometricsAdd.setWindowModality(QtCore.Qt.WindowModal)
        frmBiometricsAdd.resize(600, 491)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmBiometricsAdd.setWindowIcon(icon)
        frmBiometricsAdd.setModal(True)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(frmBiometricsAdd)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl = QtWidgets.QLabel(frmBiometricsAdd)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("color: rgb(0, 128, 0);")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_3.addWidget(self.lbl)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(frmBiometricsAdd)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.txtName = QtWidgets.QLineEdit(frmBiometricsAdd)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout_14.addWidget(self.txtName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(frmBiometricsAdd)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cmbCompanies = QtWidgets.QComboBox(frmBiometricsAdd)
        self.cmbCompanies.setEditable(True)
        self.cmbCompanies.setObjectName("cmbCompanies")
        self.horizontalLayout_3.addWidget(self.cmbCompanies)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.groupBox = QtWidgets.QGroupBox(frmBiometricsAdd)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spnCalories = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spnCalories.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnCalories.setMaximum(1000000.0)
        self.spnCalories.setObjectName("spnCalories")
        self.horizontalLayout_5.addWidget(self.spnCalories)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spnAmount = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spnAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnAmount.setMinimum(1.0)
        self.spnAmount.setMaximum(1000000.0)
        self.spnAmount.setProperty("value", 100.0)
        self.spnAmount.setObjectName("spnAmount")
        self.horizontalLayout.addWidget(self.spnAmount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spnCarbohydrate = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spnCarbohydrate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnCarbohydrate.setMaximum(1000000.0)
        self.spnCarbohydrate.setObjectName("spnCarbohydrate")
        self.horizontalLayout_2.addWidget(self.spnCarbohydrate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.spnProtein = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spnProtein.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnProtein.setMaximum(1000000.0)
        self.spnProtein.setObjectName("spnProtein")
        self.horizontalLayout_7.addWidget(self.spnProtein)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spnFat = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spnFat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnFat.setMaximum(1000000.0)
        self.spnFat.setObjectName("spnFat")
        self.horizontalLayout_6.addWidget(self.spnFat)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spnFiber = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spnFiber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnFiber.setMaximum(1000000.0)
        self.spnFiber.setObjectName("spnFiber")
        self.horizontalLayout_4.addWidget(self.spnFiber)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_15.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(frmBiometricsAdd)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.spnSalt = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spnSalt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSalt.setMaximum(1000000.0)
        self.spnSalt.setObjectName("spnSalt")
        self.horizontalLayout_8.addWidget(self.spnSalt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.spnCholesterol = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spnCholesterol.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnCholesterol.setMaximum(1000000.0)
        self.spnCholesterol.setObjectName("spnCholesterol")
        self.horizontalLayout_9.addWidget(self.spnCholesterol)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.spnSodium = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spnSodium.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSodium.setMaximum(1000000.0)
        self.spnSodium.setObjectName("spnSodium")
        self.horizontalLayout_10.addWidget(self.spnSodium)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.spnPotassium = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spnPotassium.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnPotassium.setMaximum(1000000.0)
        self.spnPotassium.setObjectName("spnPotassium")
        self.horizontalLayout_11.addWidget(self.spnPotassium)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.spnSugar = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spnSugar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSugar.setMaximum(1000000.0)
        self.spnSugar.setObjectName("spnSugar")
        self.horizontalLayout_12.addWidget(self.spnSugar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.spnSaturatedFat = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spnSaturatedFat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSaturatedFat.setMaximum(1000000.0)
        self.spnSaturatedFat.setObjectName("spnSaturatedFat")
        self.horizontalLayout_13.addWidget(self.spnSaturatedFat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.bb = QtWidgets.QDialogButtonBox(frmBiometricsAdd)
        self.bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bb.setObjectName("bb")
        self.verticalLayout_3.addWidget(self.bb)
        self.horizontalLayout_16.addLayout(self.verticalLayout_3)

        self.retranslateUi(frmBiometricsAdd)
        QtCore.QMetaObject.connectSlotsByName(frmBiometricsAdd)

    def retranslateUi(self, frmBiometricsAdd):
        _translate = QtCore.QCoreApplication.translate
        frmBiometricsAdd.setWindowTitle(_translate("frmBiometricsAdd", "Managing products"))
        self.label_15.setText(_translate("frmBiometricsAdd", "Name of the product"))
        self.label_2.setText(_translate("frmBiometricsAdd", "Select a company"))
        self.groupBox.setTitle(_translate("frmBiometricsAdd", "Basic components information"))
        self.label_6.setText(_translate("frmBiometricsAdd", "Calories"))
        self.spnCalories.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_3.setText(_translate("frmBiometricsAdd", "Amount"))
        self.spnAmount.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_4.setText(_translate("frmBiometricsAdd", "Carbohidrates"))
        self.spnCarbohydrate.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_8.setText(_translate("frmBiometricsAdd", "Protein"))
        self.spnProtein.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_7.setText(_translate("frmBiometricsAdd", "Fat"))
        self.spnFat.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_5.setText(_translate("frmBiometricsAdd", "Fiber"))
        self.spnFiber.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.groupBox_2.setTitle(_translate("frmBiometricsAdd", "Additional information"))
        self.label_9.setText(_translate("frmBiometricsAdd", "Salt"))
        self.spnSalt.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_10.setText(_translate("frmBiometricsAdd", "Cholesterol"))
        self.spnCholesterol.setSuffix(_translate("frmBiometricsAdd", " mg"))
        self.label_11.setText(_translate("frmBiometricsAdd", "Sodium"))
        self.spnSodium.setSuffix(_translate("frmBiometricsAdd", " mg"))
        self.label_12.setText(_translate("frmBiometricsAdd", "Potassium"))
        self.spnPotassium.setSuffix(_translate("frmBiometricsAdd", " mg"))
        self.label_13.setText(_translate("frmBiometricsAdd", "Sugars"))
        self.spnSugar.setSuffix(_translate("frmBiometricsAdd", " g"))
        self.label_14.setText(_translate("frmBiometricsAdd", "Saturated fat"))
        self.spnSaturatedFat.setSuffix(_translate("frmBiometricsAdd", " g"))
import caloriestracker.images.caloriestracker_rc
