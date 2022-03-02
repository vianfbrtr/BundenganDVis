# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dial_nadab2s5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dial_nada_b2s5(object):
    def setupUi(self, dial_nada_b2s5):
        dial_nada_b2s5.setObjectName("dial_nada_b2s5")
        dial_nada_b2s5.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dial_nada_b2s5.sizePolicy().hasHeightForWidth())
        dial_nada_b2s5.setSizePolicy(sizePolicy)
        dial_nada_b2s5.setMinimumSize(QtCore.QSize(600, 400))
        dial_nada_b2s5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(dial_nada_b2s5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dial_nada_b2s5)
        self.label.setMaximumSize(QtCore.QSize(400, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("export/s5.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(dial_nada_b2s5)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(dial_nada_b2s5)
        QtCore.QMetaObject.connectSlotsByName(dial_nada_b2s5)

    def retranslateUi(self, dial_nada_b2s5):
        _translate = QtCore.QCoreApplication.translate
        dial_nada_b2s5.setWindowTitle(_translate("dial_nada_b2s5", "Deteksi Nada"))
        self.label_2.setText(_translate("dial_nada_b2s5", "Dengan mengambil titik dengan perbedaan tinggi yang cukup besar, dapat dipisahkan frekuensi bundengan dengan frekuensi <i>noise</i>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dial_nada_b2s5 = QtWidgets.QDialog()
    ui = Ui_dial_nada_b2s5()
    ui.setupUi(dial_nada_b2s5)
    dial_nada_b2s5.show()
    sys.exit(app.exec_())

