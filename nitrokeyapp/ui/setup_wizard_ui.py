# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup-wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PINSetup(object):
    def setupUi(self, PINSetup):
        PINSetup.setObjectName("PINSetup")
        PINSetup.resize(439, 309)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wizardPage1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.wizardPage1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.wizardPage1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.wizardPage1)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        PINSetup.addPage(self.wizardPage1)
        self.wizardPage = QtWidgets.QWizardPage()
        self.wizardPage.setObjectName("wizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.wizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.line_2 = QtWidgets.QFrame(self.wizardPage)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.wizardPage)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.wizardPage)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.wizardPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.wizardPage)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.wizardPage)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.wizardPage)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        PINSetup.addPage(self.wizardPage)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.wizardPage2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.wizardPage2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.wizardPage2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 1, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.wizardPage2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 4, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.wizardPage2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.wizardPage2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.wizardPage2)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 6, 0, 1, 3)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_3.addItem(spacerItem4, 5, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.wizardPage2)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 3, 2, 1, 1)
        PINSetup.addPage(self.wizardPage2)

        self.retranslateUi(PINSetup)
        QtCore.QMetaObject.connectSlotsByName(PINSetup)

    def retranslateUi(self, PINSetup):
        _translate = QtCore.QCoreApplication.translate
        PINSetup.setWindowTitle(_translate("PINSetup", "Wizard"))
        self.label_2.setText(
            _translate(
                "PINSetup",
                "This Guided Setup Wizard leads you through the process of setting up your PIN's, which are essential to use your Nitrokey device. ",
            )
        )
        self.label.setText(_translate("PINSetup", "Nitrokey Setup"))
        self.label_3.setText(
            _translate("PINSetup", "Your PINs can also be changed later again.")
        )
        self.label_4.setText(_translate("PINSetup", "User PIN Setup"))
        self.label_6.setText(_translate("PINSetup", "new User PIN:"))
        self.label_7.setText(_translate("PINSetup", "confirm new User PIN:"))
        self.label_5.setText(
            _translate(
                "PINSetup",
                "The Nitrokey is protected by a User PIN, \n"
                "only 3 entries are possible until the device is locked. \n"
                "Choose a User PIN between 6-20 characters. \n"
                "",
            )
        )
        self.label_10.setText(_translate("PINSetup", "confirm new Admin PIN:"))
        self.label_12.setText(_translate("PINSetup", "new Admin PIN:"))
        self.label_9.setText(_translate("PINSetup", "Admin PIN Setup"))
        self.label_11.setText(
            _translate(
                "PINSetup",
                "To unlock a blocked Nitrokey, you need an Admin PIN.\n"
                "choose a PIN between 6-20 characters. \n"
                "",
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PINSetup = QtWidgets.QWizard()
    ui = Ui_PINSetup()
    ui.setupUi(PINSetup)
    PINSetup.show()
    sys.exit(app.exec_())