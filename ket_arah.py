# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arah.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ket_arah_polar(object):
    def setupUi(self, ket_arah_polar):
        ket_arah_polar.setObjectName("ket_arah_polar")
        ket_arah_polar.resize(500, 500)
        ket_arah_polar.setMinimumSize(QtCore.QSize(500, 500))
        ket_arah_polar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(ket_arah_polar)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ket_arah_polar)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(ket_arah_polar)
        QtCore.QMetaObject.connectSlotsByName(ket_arah_polar)

    def retranslateUi(self, ket_arah_polar):
        _translate = QtCore.QCoreApplication.translate
        ket_arah_polar.setWindowTitle(_translate("ket_arah_polar", "Posisi Bundengan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ket_arah_polar = QtWidgets.QDialog()
    ui = Ui_ket_arah_polar()
    ui.setupUi(ket_arah_polar)
    ket_arah_polar.show()
    sys.exit(app.exec_())

