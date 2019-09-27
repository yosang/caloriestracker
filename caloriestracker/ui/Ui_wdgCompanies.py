# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgCompanies.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgCompanies(object):
    def setupUi(self, wdgCompanies):
        wdgCompanies.setObjectName("wdgCompanies")
        wdgCompanies.resize(1012, 669)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgCompanies)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl = QtWidgets.QLabel(wdgCompanies)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_3.addWidget(self.lbl)
        self.groupBox = QtWidgets.QGroupBox(wdgCompanies)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt = QtWidgets.QLineEdit(self.groupBox)
        self.txt.setObjectName("txt")
        self.horizontalLayout.addWidget(self.txt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.cmd = QtWidgets.QToolButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cmd.setIcon(icon)
        self.cmd.setObjectName("cmd")
        self.horizontalLayout_3.addWidget(self.cmd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setEnabled(False)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tblCompanies = myQTableWidget(wdgCompanies)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblCompanies.sizePolicy().hasHeightForWidth())
        self.tblCompanies.setSizePolicy(sizePolicy)
        self.tblCompanies.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblCompanies.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCompanies.setAlternatingRowColors(True)
        self.tblCompanies.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCompanies.setObjectName("tblCompanies")
        self.tblCompanies.setColumnCount(0)
        self.tblCompanies.setRowCount(0)
        self.tblCompanies.horizontalHeader().setStretchLastSection(False)
        self.tblCompanies.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tblCompanies)
        self.lblFound = QtWidgets.QLabel(wdgCompanies)
        self.lblFound.setObjectName("lblFound")
        self.verticalLayout_3.addWidget(self.lblFound)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.actionCompanyNew = QtWidgets.QAction(wdgCompanies)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/caloriestracker/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompanyNew.setIcon(icon1)
        self.actionCompanyNew.setObjectName("actionCompanyNew")
        self.actionCompanyDelete = QtWidgets.QAction(wdgCompanies)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/caloriestracker/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompanyDelete.setIcon(icon2)
        self.actionCompanyDelete.setObjectName("actionCompanyDelete")
        self.actionCompanyEdit = QtWidgets.QAction(wdgCompanies)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/caloriestracker/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCompanyEdit.setIcon(icon3)
        self.actionCompanyEdit.setObjectName("actionCompanyEdit")

        self.retranslateUi(wdgCompanies)
        QtCore.QMetaObject.connectSlotsByName(wdgCompanies)

    def retranslateUi(self, wdgCompanies):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgCompanies", "Companies list"))
        self.groupBox.setTitle(_translate("wdgCompanies", "Select your search"))
        self.label.setText(_translate("wdgCompanies", "Add a search string"))
        self.lblFound.setText(_translate("wdgCompanies", "Registers found"))
        self.actionCompanyNew.setText(_translate("wdgCompanies", "New company"))
        self.actionCompanyNew.setToolTip(_translate("wdgCompanies", "New company"))
        self.actionCompanyDelete.setText(_translate("wdgCompanies", "Delete company"))
        self.actionCompanyDelete.setToolTip(_translate("wdgCompanies", "Delete company"))
        self.actionCompanyEdit.setText(_translate("wdgCompanies", "Edit company"))
        self.actionCompanyEdit.setToolTip(_translate("wdgCompanies", "Edit company"))
from caloriestracker.ui.myqtablewidget import myQTableWidget
import caloriestracker.images.caloriestracker_rc
