# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dial_b2s4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog_compareb2s4(object):
    def setupUi(self, dialog_compareb2s4):
        dialog_compareb2s4.setObjectName("dialog_compareb2s4")
        dialog_compareb2s4.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_compareb2s4)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(dialog_compareb2s4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.n1_cekbox = QtWidgets.QCheckBox(self.frame)
        self.n1_cekbox.setObjectName("n1_cekbox")
        self.verticalLayout_2.addWidget(self.n1_cekbox)
        self.n2_cekbox = QtWidgets.QCheckBox(self.frame)
        self.n2_cekbox.setObjectName("n2_cekbox")
        self.verticalLayout_2.addWidget(self.n2_cekbox)
        self.n3_cekbox = QtWidgets.QCheckBox(self.frame)
        self.n3_cekbox.setObjectName("n3_cekbox")
        self.verticalLayout_2.addWidget(self.n3_cekbox)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(dialog_compareb2s4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.apply_btn = QtWidgets.QPushButton(self.frame_2)
        self.apply_btn.setObjectName("apply_btn")
        self.horizontalLayout.addWidget(self.apply_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.frame_2)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(220, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(dialog_compareb2s4)
        QtCore.QMetaObject.connectSlotsByName(dialog_compareb2s4)

    def retranslateUi(self, dialog_compareb2s4):
        _translate = QtCore.QCoreApplication.translate
        dialog_compareb2s4.setWindowTitle(_translate("dialog_compareb2s4", "Pilih nada senar 4"))
        self.n1_cekbox.setText(_translate("dialog_compareb2s4", "Nada Pertama (228,5 Hz)"))
        self.n2_cekbox.setText(_translate("dialog_compareb2s4", "Nada Kedua (451,1 Hz)"))
        self.n3_cekbox.setText(_translate("dialog_compareb2s4", "Nada Ketiga (1306,6 Hz)"))
        self.apply_btn.setText(_translate("dialog_compareb2s4", "Lihat"))
        self.cancel_btn.setText(_translate("dialog_compareb2s4", "Batal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_compareb2s4 = QtWidgets.QDialog()
    ui = Ui_dialog_compareb2s4()
    ui.setupUi(dialog_compareb2s4)
    dialog_compareb2s4.show()
    sys.exit(app.exec_())

