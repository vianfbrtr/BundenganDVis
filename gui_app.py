# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1280, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mainLayout = QtWidgets.QWidget(mainWindow)
        self.mainLayout.setObjectName("mainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainLayout)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QFrame(self.mainLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.side_menu.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.side_menu.setFont(font)
        self.side_menu.setStyleSheet("QFrame{\n"
"background-color: rgb(247, 247, 248);\n"
"border-right: 0.5px solid rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 0px solid;\n"
"    color: rgb(77, 77, 77);\n"
"    background-color: rgb(247, 247, 248);\n"
"    padding-top: 18px;\n"
"    padding-bottom:18px;\n"
"    padding-left: 20px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-left: 3px solid #303f9f;\n"
"    \n"
"}")
        self.side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout.setContentsMargins(0, 0, 1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.beranda_button = QtWidgets.QPushButton(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.beranda_button.sizePolicy().hasHeightForWidth())
        self.beranda_button.setSizePolicy(sizePolicy)
        self.beranda_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/hut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.beranda_button.setIcon(icon1)
        self.beranda_button.setIconSize(QtCore.QSize(20, 20))
        self.beranda_button.setObjectName("beranda_button")
        self.verticalLayout.addWidget(self.beranda_button)
        self.bund1_button = QtWidgets.QPushButton(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bund1_button.sizePolicy().hasHeightForWidth())
        self.bund1_button.setSizePolicy(sizePolicy)
        self.bund1_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/logoBund1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bund1_button.setIcon(icon2)
        self.bund1_button.setIconSize(QtCore.QSize(20, 20))
        self.bund1_button.setObjectName("bund1_button")
        self.verticalLayout.addWidget(self.bund1_button)
        self.bund2_button = QtWidgets.QPushButton(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bund2_button.sizePolicy().hasHeightForWidth())
        self.bund2_button.setSizePolicy(sizePolicy)
        self.bund2_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/logoBund2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bund2_button.setIcon(icon3)
        self.bund2_button.setIconSize(QtCore.QSize(20, 20))
        self.bund2_button.setObjectName("bund2_button")
        self.verticalLayout.addWidget(self.bund2_button)
        self.compare_button = QtWidgets.QPushButton(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compare_button.sizePolicy().hasHeightForWidth())
        self.compare_button.setSizePolicy(sizePolicy)
        self.compare_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/compare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.compare_button.setIcon(icon4)
        self.compare_button.setIconSize(QtCore.QSize(20, 20))
        self.compare_button.setObjectName("compare_button")
        self.verticalLayout.addWidget(self.compare_button)
        self.help_button = QtWidgets.QPushButton(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help_button.sizePolicy().hasHeightForWidth())
        self.help_button.setSizePolicy(sizePolicy)
        self.help_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_button.setIcon(icon5)
        self.help_button.setIconSize(QtCore.QSize(20, 20))
        self.help_button.setObjectName("help_button")
        self.verticalLayout.addWidget(self.help_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.about_button = QtWidgets.QPushButton(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_button.sizePolicy().hasHeightForWidth())
        self.about_button.setSizePolicy(sizePolicy)
        self.about_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_button.setIcon(icon6)
        self.about_button.setIconSize(QtCore.QSize(20, 20))
        self.about_button.setObjectName("about_button")
        self.verticalLayout.addWidget(self.about_button)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_view = QtWidgets.QFrame(self.mainLayout)
        self.main_view.setMinimumSize(QtCore.QSize(1080, 0))
        self.main_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_view.setObjectName("main_view")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_view)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pages_widget = QtWidgets.QStackedWidget(self.main_view)
        self.pages_widget.setObjectName("pages_widget")
        self.beranda_page = QtWidgets.QWidget()
        self.beranda_page.setObjectName("beranda_page")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.beranda_page)
        self.verticalLayout_59.setContentsMargins(40, 20, 0, 0)
        self.verticalLayout_59.setSpacing(15)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.label_4 = QtWidgets.QLabel(self.beranda_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 200))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_59.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.beranda_page)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_59.addWidget(self.line)
        self.frame_66 = QtWidgets.QFrame(self.beranda_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy)
        self.frame_66.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_66.setObjectName("frame_66")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_66)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setSpacing(20)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.frame_66)
        self.scrollArea_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 508, 444))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.horizontalLayout_72 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.label_67 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy)
        self.label_67.setMinimumSize(QtCore.QSize(504, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_67.setFont(font)
        self.label_67.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_67.setWordWrap(True)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_72.addWidget(self.label_67)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_53.addWidget(self.scrollArea_4)
        self.frame_67 = QtWidgets.QFrame(self.frame_66)
        self.frame_67.setMinimumSize(QtCore.QSize(510, 0))
        self.frame_67.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_67.setObjectName("frame_67")
        self.label_68 = QtWidgets.QLabel(self.frame_67)
        self.label_68.setGeometry(QtCore.QRect(10, -10, 504, 711))
        self.label_68.setText("")
        self.label_68.setPixmap(QtGui.QPixmap("images/bundengan_home.png"))
        self.label_68.setObjectName("label_68")
        self.horizontalLayout_53.addWidget(self.frame_67)
        self.verticalLayout_59.addWidget(self.frame_66)
        self.pages_widget.addWidget(self.beranda_page)
        self.bund1_page = QtWidgets.QWidget()
        self.bund1_page.setObjectName("bund1_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.bund1_page)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_bund1 = QtWidgets.QStackedWidget(self.bund1_page)
        self.stackedWidget_bund1.setObjectName("stackedWidget_bund1")
        self.choice_bund1 = QtWidgets.QWidget()
        self.choice_bund1.setObjectName("choice_bund1")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.choice_bund1)
        self.verticalLayout_40.setContentsMargins(10, 10, 10, 0)
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_2 = QtWidgets.QLabel(self.choice_bund1)
        self.label_2.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_40.addWidget(self.label_2)
        self.frame_2 = QtWidgets.QFrame(self.choice_bund1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1112, 1150))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_64.setSpacing(20)
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.frame_68 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy)
        self.frame_68.setMinimumSize(QtCore.QSize(0, 360))
        self.frame_68.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.frame_68)
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.label_69 = QtWidgets.QLabel(self.frame_68)
        self.label_69.setMinimumSize(QtCore.QSize(640, 0))
        self.label_69.setText("")
        self.label_69.setPixmap(QtGui.QPixmap("images/welcome_bund1.png"))
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_54.addWidget(self.label_69)
        spacerItem1 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem1)
        self.verticalLayout_64.addWidget(self.frame_68)
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_64.addWidget(self.textBrowser)
        self.frame_69 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_69.sizePolicy().hasHeightForWidth())
        self.frame_69.setSizePolicy(sizePolicy)
        self.frame_69.setMinimumSize(QtCore.QSize(0, 650))
        self.frame_69.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.frame_69)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setSpacing(20)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.frame_70 = QtWidgets.QFrame(self.frame_69)
        self.frame_70.setMinimumSize(QtCore.QSize(640, 0))
        self.frame_70.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.frame_70)
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_65.setSpacing(20)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.label_70 = QtWidgets.QLabel(self.frame_70)
        self.label_70.setMinimumSize(QtCore.QSize(0, 360))
        self.label_70.setText("")
        self.label_70.setPixmap(QtGui.QPixmap("images/welcome_bund1_a.png"))
        self.label_70.setObjectName("label_70")
        self.verticalLayout_65.addWidget(self.label_70)
        self.label_71 = QtWidgets.QLabel(self.frame_70)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_71.setFont(font)
        self.label_71.setStyleSheet("QLabel{\n"
"    padding-left: 20px;\n"
"    padding-right:20px;\n"
"}")
        self.label_71.setWordWrap(True)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_65.addWidget(self.label_71)
        self.horizontalLayout_55.addWidget(self.frame_70)
        self.frame_72 = QtWidgets.QFrame(self.frame_69)
        self.frame_72.setMinimumSize(QtCore.QSize(452, 0))
        self.frame_72.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_72.setObjectName("frame_72")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.frame_72)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.label_74 = QtWidgets.QLabel(self.frame_72)
        self.label_74.setText("")
        self.label_74.setPixmap(QtGui.QPixmap("images/welcome_bund1_b.png"))
        self.label_74.setObjectName("label_74")
        self.horizontalLayout_56.addWidget(self.label_74)
        self.horizontalLayout_55.addWidget(self.frame_72)
        self.verticalLayout_64.addWidget(self.frame_69)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.addWidget(self.scrollArea_2)
        self.frame_44 = QtWidgets.QFrame(self.frame_2)
        self.frame_44.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_44.setStyleSheet("QPushButton{\n"
"    color: rgb(77, 77, 77);\n"
"    border: 0.5px solid rgb(191, 191, 191);\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.frame_44.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_44.setObjectName("frame_44")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_44)
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_39.setSpacing(15)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.b1s1_button = QtWidgets.QPushButton(self.frame_44)
        self.b1s1_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s1_button.setObjectName("b1s1_button")
        self.verticalLayout_39.addWidget(self.b1s1_button)
        self.b1s2_button = QtWidgets.QPushButton(self.frame_44)
        self.b1s2_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s2_button.setObjectName("b1s2_button")
        self.verticalLayout_39.addWidget(self.b1s2_button)
        self.b1s3_button = QtWidgets.QPushButton(self.frame_44)
        self.b1s3_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s3_button.setObjectName("b1s3_button")
        self.verticalLayout_39.addWidget(self.b1s3_button)
        self.b1s4_button = QtWidgets.QPushButton(self.frame_44)
        self.b1s4_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s4_button.setObjectName("b1s4_button")
        self.verticalLayout_39.addWidget(self.b1s4_button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.frame_44)
        self.verticalLayout_40.addWidget(self.frame_2)
        self.stackedWidget_bund1.addWidget(self.choice_bund1)
        self.b1senar1 = QtWidgets.QWidget()
        self.b1senar1.setObjectName("b1senar1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.b1senar1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.b1senar1)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.back_button_b1s1 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b1s1.sizePolicy().hasHeightForWidth())
        self.back_button_b1s1.setSizePolicy(sizePolicy)
        self.back_button_b1s1.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b1s1.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b1s1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b1s1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_button_b1s1.setIcon(icon7)
        self.back_button_b1s1.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b1s1.setObjectName("back_button_b1s1")
        self.horizontalLayout_4.addWidget(self.back_button_b1s1)
        self.title_b1s = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s.setFont(font)
        self.title_b1s.setObjectName("title_b1s")
        self.horizontalLayout_4.addWidget(self.title_b1s)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.label_7 = QtWidgets.QLabel(self.b1senar1)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.b1senar1_tabWidget = QtWidgets.QTabWidget(self.b1senar1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b1senar1_tabWidget.sizePolicy().hasHeightForWidth())
        self.b1senar1_tabWidget.setSizePolicy(sizePolicy)
        self.b1senar1_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b1senar1_tabWidget.setObjectName("b1senar1_tabWidget")
        self.b1senar1_measure = QtWidgets.QWidget()
        self.b1senar1_measure.setObjectName("b1senar1_measure")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.b1senar1_measure)
        self.horizontalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.b1senar1_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b1senar1_mesh_plotLayout.setObjectName("b1senar1_mesh_plotLayout")
        self.horizontalLayout_5.addLayout(self.b1senar1_mesh_plotLayout)
        self.frame_5 = QtWidgets.QFrame(self.b1senar1_measure)
        self.frame_5.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("images/b1_fig_s1.png"))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.b1senar1_tabWidget.addTab(self.b1senar1_measure, "")
        self.b1senar1_polar = QtWidgets.QWidget()
        self.b1senar1_polar.setObjectName("b1senar1_polar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.b1senar1_polar)
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.b1senar1_layoutPolar = QtWidgets.QVBoxLayout()
        self.b1senar1_layoutPolar.setObjectName("b1senar1_layoutPolar")
        self.horizontalLayout_6.addLayout(self.b1senar1_layoutPolar)
        self.frame_6 = QtWidgets.QFrame(self.b1senar1_polar)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_10.addWidget(self.label_9)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(15)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.b1s1n1_cekbox = QtWidgets.QCheckBox(self.frame_7)
        self.b1s1n1_cekbox.setObjectName("b1s1n1_cekbox")
        self.verticalLayout_11.addWidget(self.b1s1n1_cekbox)
        self.b1s1n2_cekbox = QtWidgets.QCheckBox(self.frame_7)
        self.b1s1n2_cekbox.setObjectName("b1s1n2_cekbox")
        self.verticalLayout_11.addWidget(self.b1s1n2_cekbox)
        self.b1s1n3_cekbox = QtWidgets.QCheckBox(self.frame_7)
        self.b1s1n3_cekbox.setObjectName("b1s1n3_cekbox")
        self.verticalLayout_11.addWidget(self.b1s1n3_cekbox)
        self.b1s1n4_cekbox = QtWidgets.QCheckBox(self.frame_7)
        self.b1s1n4_cekbox.setObjectName("b1s1n4_cekbox")
        self.verticalLayout_11.addWidget(self.b1s1n4_cekbox)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b1s1_applyBtn = QtWidgets.QPushButton(self.frame_8)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b1s1_applyBtn.setFont(font)
        self.b1s1_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s1_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b1s1_applyBtn.setObjectName("b1s1_applyBtn")
        self.horizontalLayout_7.addWidget(self.b1s1_applyBtn)
        self.b1s1_peakBtn = QtWidgets.QPushButton(self.frame_8)
        self.b1s1_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b1s1_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s1_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b1s1_peakBtn.setObjectName("b1s1_peakBtn")
        self.horizontalLayout_7.addWidget(self.b1s1_peakBtn)
        self.verticalLayout_11.addWidget(self.frame_8)
        self.verticalLayout_10.addWidget(self.frame_7)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setMinimumSize(QtCore.QSize(0, 250))
        self.label_10.setMaximumSize(QtCore.QSize(250, 250))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_10.addWidget(self.label_10)
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.b1senar1_tabWidget.addTab(self.b1senar1_polar, "")
        self.verticalLayout_7.addWidget(self.b1senar1_tabWidget)
        self.stackedWidget_bund1.addWidget(self.b1senar1)
        self.b1senar2 = QtWidgets.QWidget()
        self.b1senar2.setObjectName("b1senar2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.b1senar2)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_9 = QtWidgets.QFrame(self.b1senar2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_9.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.back_button_b1s2 = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b1s2.sizePolicy().hasHeightForWidth())
        self.back_button_b1s2.setSizePolicy(sizePolicy)
        self.back_button_b1s2.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b1s2.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b1s2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b1s2.setText("")
        self.back_button_b1s2.setIcon(icon7)
        self.back_button_b1s2.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b1s2.setObjectName("back_button_b1s2")
        self.horizontalLayout_8.addWidget(self.back_button_b1s2)
        self.title_b1s_2 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_2.setFont(font)
        self.title_b1s_2.setObjectName("title_b1s_2")
        self.horizontalLayout_8.addWidget(self.title_b1s_2)
        self.verticalLayout_14.addWidget(self.frame_9)
        self.label_11 = QtWidgets.QLabel(self.b1senar2)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11)
        self.b1senar2_tabWidget = QtWidgets.QTabWidget(self.b1senar2)
        self.b1senar2_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b1senar2_tabWidget.setObjectName("b1senar2_tabWidget")
        self.b1senar2_measure = QtWidgets.QWidget()
        self.b1senar2_measure.setObjectName("b1senar2_measure")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.b1senar2_measure)
        self.horizontalLayout_9.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.b1senar2_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b1senar2_mesh_plotLayout.setObjectName("b1senar2_mesh_plotLayout")
        self.horizontalLayout_9.addLayout(self.b1senar2_mesh_plotLayout)
        self.frame_10 = QtWidgets.QFrame(self.b1senar2_measure)
        self.frame_10.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.frame_10)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setMinimumSize(QtCore.QSize(0, 400))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("images/b1_fig_s2.png"))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.horizontalLayout_9.addWidget(self.frame_10)
        self.b1senar2_tabWidget.addTab(self.b1senar2_measure, "")
        self.b1senar1_polar_2 = QtWidgets.QWidget()
        self.b1senar1_polar_2.setObjectName("b1senar1_polar_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.b1senar1_polar_2)
        self.horizontalLayout_10.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.b1senar2_layout_polar = QtWidgets.QVBoxLayout()
        self.b1senar2_layout_polar.setObjectName("b1senar2_layout_polar")
        self.horizontalLayout_10.addLayout(self.b1senar2_layout_polar)
        self.frame_11 = QtWidgets.QFrame(self.b1senar1_polar_2)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_11.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_14 = QtWidgets.QLabel(self.frame_11)
        self.label_14.setMinimumSize(QtCore.QSize(0, 100))
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_12.addWidget(self.label_14)
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(15)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.b1s2n1_cekbox = QtWidgets.QCheckBox(self.frame_12)
        self.b1s2n1_cekbox.setObjectName("b1s2n1_cekbox")
        self.verticalLayout_13.addWidget(self.b1s2n1_cekbox)
        self.b1s2n2_cekbox = QtWidgets.QCheckBox(self.frame_12)
        self.b1s2n2_cekbox.setObjectName("b1s2n2_cekbox")
        self.verticalLayout_13.addWidget(self.b1s2n2_cekbox)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.b1s2_applyBtn = QtWidgets.QPushButton(self.frame_13)
        self.b1s2_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s2_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b1s2_applyBtn.setObjectName("b1s2_applyBtn")
        self.horizontalLayout_11.addWidget(self.b1s2_applyBtn)
        self.b1s2_peakBtn = QtWidgets.QPushButton(self.frame_13)
        self.b1s2_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b1s2_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s2_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b1s2_peakBtn.setObjectName("b1s2_peakBtn")
        self.horizontalLayout_11.addWidget(self.b1s2_peakBtn)
        self.verticalLayout_13.addWidget(self.frame_13)
        self.verticalLayout_12.addWidget(self.frame_12)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem3)
        self.label_15 = QtWidgets.QLabel(self.frame_11)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(250, 250))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15)
        self.horizontalLayout_10.addWidget(self.frame_11)
        self.b1senar2_tabWidget.addTab(self.b1senar1_polar_2, "")
        self.verticalLayout_14.addWidget(self.b1senar2_tabWidget)
        self.stackedWidget_bund1.addWidget(self.b1senar2)
        self.b1senar3 = QtWidgets.QWidget()
        self.b1senar3.setObjectName("b1senar3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.b1senar3)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_18 = QtWidgets.QFrame(self.b1senar3)
        self.frame_18.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_18.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(15)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.back_button_b1s3 = QtWidgets.QPushButton(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b1s3.sizePolicy().hasHeightForWidth())
        self.back_button_b1s3.setSizePolicy(sizePolicy)
        self.back_button_b1s3.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b1s3.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b1s3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b1s3.setText("")
        self.back_button_b1s3.setIcon(icon7)
        self.back_button_b1s3.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b1s3.setObjectName("back_button_b1s3")
        self.horizontalLayout_15.addWidget(self.back_button_b1s3)
        self.title_b1s_3 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_3.setFont(font)
        self.title_b1s_3.setObjectName("title_b1s_3")
        self.horizontalLayout_15.addWidget(self.title_b1s_3)
        self.verticalLayout_18.addWidget(self.frame_18)
        self.label_20 = QtWidgets.QLabel(self.b1senar3)
        self.label_20.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_18.addWidget(self.label_20)
        self.b1senar3_tabWidget = QtWidgets.QTabWidget(self.b1senar3)
        self.b1senar3_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b1senar3_tabWidget.setObjectName("b1senar3_tabWidget")
        self.b1senar3_measure = QtWidgets.QWidget()
        self.b1senar3_measure.setObjectName("b1senar3_measure")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.b1senar3_measure)
        self.horizontalLayout_12.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.b1senar3_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b1senar3_mesh_plotLayout.setObjectName("b1senar3_mesh_plotLayout")
        self.horizontalLayout_12.addLayout(self.b1senar3_mesh_plotLayout)
        self.frame_14 = QtWidgets.QFrame(self.b1senar3_measure)
        self.frame_14.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.frame_14)
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_15.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.frame_14)
        self.label_17.setMinimumSize(QtCore.QSize(0, 400))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("images/b1_fig_s3.png"))
        self.label_17.setObjectName("label_17")
        self.verticalLayout_15.addWidget(self.label_17)
        self.horizontalLayout_12.addWidget(self.frame_14)
        self.b1senar3_tabWidget.addTab(self.b1senar3_measure, "")
        self.b1senar1_polar_3 = QtWidgets.QWidget()
        self.b1senar1_polar_3.setObjectName("b1senar1_polar_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.b1senar1_polar_3)
        self.horizontalLayout_13.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.b1senar3_layout_polar = QtWidgets.QVBoxLayout()
        self.b1senar3_layout_polar.setObjectName("b1senar3_layout_polar")
        self.horizontalLayout_13.addLayout(self.b1senar3_layout_polar)
        self.frame_15 = QtWidgets.QFrame(self.b1senar1_polar_3)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_15.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_18 = QtWidgets.QLabel(self.frame_15)
        self.label_18.setMinimumSize(QtCore.QSize(0, 100))
        self.label_18.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_16.addWidget(self.label_18)
        self.frame_16 = QtWidgets.QFrame(self.frame_15)
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.b1s3n1_cekbox = QtWidgets.QCheckBox(self.frame_16)
        self.b1s3n1_cekbox.setObjectName("b1s3n1_cekbox")
        self.verticalLayout_17.addWidget(self.b1s3n1_cekbox)
        self.b1s3n2_cekbox = QtWidgets.QCheckBox(self.frame_16)
        self.b1s3n2_cekbox.setObjectName("b1s3n2_cekbox")
        self.verticalLayout_17.addWidget(self.b1s3n2_cekbox)
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.b1s3_applyBtn = QtWidgets.QPushButton(self.frame_17)
        self.b1s3_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s3_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b1s3_applyBtn.setObjectName("b1s3_applyBtn")
        self.horizontalLayout_14.addWidget(self.b1s3_applyBtn)
        self.b1s3_peakBtn = QtWidgets.QPushButton(self.frame_17)
        self.b1s3_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b1s3_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s3_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b1s3_peakBtn.setObjectName("b1s3_peakBtn")
        self.horizontalLayout_14.addWidget(self.b1s3_peakBtn)
        self.verticalLayout_17.addWidget(self.frame_17)
        self.verticalLayout_16.addWidget(self.frame_16)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem4)
        self.label_19 = QtWidgets.QLabel(self.frame_15)
        self.label_19.setMinimumSize(QtCore.QSize(0, 250))
        self.label_19.setMaximumSize(QtCore.QSize(250, 250))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_16.addWidget(self.label_19)
        self.horizontalLayout_13.addWidget(self.frame_15)
        self.b1senar3_tabWidget.addTab(self.b1senar1_polar_3, "")
        self.verticalLayout_18.addWidget(self.b1senar3_tabWidget)
        self.stackedWidget_bund1.addWidget(self.b1senar3)
        self.b1senar4 = QtWidgets.QWidget()
        self.b1senar4.setObjectName("b1senar4")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.b1senar4)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_22.setSpacing(10)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_19 = QtWidgets.QFrame(self.b1senar4)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_19.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.back_button_b1s4 = QtWidgets.QPushButton(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b1s4.sizePolicy().hasHeightForWidth())
        self.back_button_b1s4.setSizePolicy(sizePolicy)
        self.back_button_b1s4.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b1s4.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b1s4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b1s4.setText("")
        self.back_button_b1s4.setIcon(icon7)
        self.back_button_b1s4.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b1s4.setObjectName("back_button_b1s4")
        self.horizontalLayout_16.addWidget(self.back_button_b1s4)
        self.title_b1s_4 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_4.setFont(font)
        self.title_b1s_4.setObjectName("title_b1s_4")
        self.horizontalLayout_16.addWidget(self.title_b1s_4)
        self.verticalLayout_22.addWidget(self.frame_19)
        self.label_25 = QtWidgets.QLabel(self.b1senar4)
        self.label_25.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_22.addWidget(self.label_25)
        self.b1senar4_tabWidget = QtWidgets.QTabWidget(self.b1senar4)
        self.b1senar4_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b1senar4_tabWidget.setObjectName("b1senar4_tabWidget")
        self.b1senar4_measure = QtWidgets.QWidget()
        self.b1senar4_measure.setObjectName("b1senar4_measure")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.b1senar4_measure)
        self.horizontalLayout_17.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.b1senar4_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b1senar4_mesh_plotLayout.setObjectName("b1senar4_mesh_plotLayout")
        self.horizontalLayout_17.addLayout(self.b1senar4_mesh_plotLayout)
        self.frame_20 = QtWidgets.QFrame(self.b1senar4_measure)
        self.frame_20.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_20.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_21 = QtWidgets.QLabel(self.frame_20)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setWordWrap(True)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_19.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.frame_20)
        self.label_22.setMinimumSize(QtCore.QSize(0, 400))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("images/b1_fig_s4.png"))
        self.label_22.setObjectName("label_22")
        self.verticalLayout_19.addWidget(self.label_22)
        self.horizontalLayout_17.addWidget(self.frame_20)
        self.b1senar4_tabWidget.addTab(self.b1senar4_measure, "")
        self.b1senar1_polar_4 = QtWidgets.QWidget()
        self.b1senar1_polar_4.setObjectName("b1senar1_polar_4")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.b1senar1_polar_4)
        self.horizontalLayout_18.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.b1senar4_layout_polar = QtWidgets.QVBoxLayout()
        self.b1senar4_layout_polar.setObjectName("b1senar4_layout_polar")
        self.horizontalLayout_18.addLayout(self.b1senar4_layout_polar)
        self.frame_21 = QtWidgets.QFrame(self.b1senar1_polar_4)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_21.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_21.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_23 = QtWidgets.QLabel(self.frame_21)
        self.label_23.setMinimumSize(QtCore.QSize(0, 100))
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_20.addWidget(self.label_23)
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(15)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.b1s4n1_cekbox = QtWidgets.QCheckBox(self.frame_22)
        self.b1s4n1_cekbox.setObjectName("b1s4n1_cekbox")
        self.verticalLayout_21.addWidget(self.b1s4n1_cekbox)
        self.b1s4n2_cekbox = QtWidgets.QCheckBox(self.frame_22)
        self.b1s4n2_cekbox.setObjectName("b1s4n2_cekbox")
        self.verticalLayout_21.addWidget(self.b1s4n2_cekbox)
        self.frame_23 = QtWidgets.QFrame(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_23.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.b1s4_applyBtn = QtWidgets.QPushButton(self.frame_23)
        self.b1s4_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s4_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b1s4_applyBtn.setObjectName("b1s4_applyBtn")
        self.horizontalLayout_19.addWidget(self.b1s4_applyBtn)
        self.b1s4_peakBtn = QtWidgets.QPushButton(self.frame_23)
        self.b1s4_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b1s4_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1s4_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b1s4_peakBtn.setObjectName("b1s4_peakBtn")
        self.horizontalLayout_19.addWidget(self.b1s4_peakBtn)
        self.verticalLayout_21.addWidget(self.frame_23)
        self.verticalLayout_20.addWidget(self.frame_22)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem5)
        self.label_24 = QtWidgets.QLabel(self.frame_21)
        self.label_24.setMinimumSize(QtCore.QSize(0, 250))
        self.label_24.setMaximumSize(QtCore.QSize(250, 250))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_20.addWidget(self.label_24)
        self.horizontalLayout_18.addWidget(self.frame_21)
        self.b1senar4_tabWidget.addTab(self.b1senar1_polar_4, "")
        self.verticalLayout_22.addWidget(self.b1senar4_tabWidget)
        self.stackedWidget_bund1.addWidget(self.b1senar4)
        self.verticalLayout_4.addWidget(self.stackedWidget_bund1)
        self.pages_widget.addWidget(self.bund1_page)
        self.bund2_page = QtWidgets.QWidget()
        self.bund2_page.setObjectName("bund2_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bund2_page)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget_bund2 = QtWidgets.QStackedWidget(self.bund2_page)
        self.stackedWidget_bund2.setObjectName("stackedWidget_bund2")
        self.choice_bund2 = QtWidgets.QWidget()
        self.choice_bund2.setObjectName("choice_bund2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.choice_bund2)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.choice_bund2)
        self.label.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.choice_bund2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1112, 1150))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_67.setSpacing(20)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.frame_77 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_77.sizePolicy().hasHeightForWidth())
        self.frame_77.setSizePolicy(sizePolicy)
        self.frame_77.setMinimumSize(QtCore.QSize(0, 360))
        self.frame_77.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.horizontalLayout_61 = QtWidgets.QHBoxLayout(self.frame_77)
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName("horizontalLayout_61")
        self.label_78 = QtWidgets.QLabel(self.frame_77)
        self.label_78.setMinimumSize(QtCore.QSize(640, 0))
        self.label_78.setText("")
        self.label_78.setPixmap(QtGui.QPixmap("images/bund2_welcome_vvvv copy 2.png"))
        self.label_78.setObjectName("label_78")
        self.horizontalLayout_61.addWidget(self.label_78)
        spacerItem6 = QtWidgets.QSpacerItem(73, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_61.addItem(spacerItem6)
        self.verticalLayout_67.addWidget(self.frame_77)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setOpenExternalLinks(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_67.addWidget(self.textBrowser_2)
        self.frame_74 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_74.sizePolicy().hasHeightForWidth())
        self.frame_74.setSizePolicy(sizePolicy)
        self.frame_74.setMinimumSize(QtCore.QSize(0, 650))
        self.frame_74.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.frame_74)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setSpacing(20)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.frame_75 = QtWidgets.QFrame(self.frame_74)
        self.frame_75.setMinimumSize(QtCore.QSize(640, 0))
        self.frame_75.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout(self.frame_75)
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_66.setSpacing(20)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.label_75 = QtWidgets.QLabel(self.frame_75)
        self.label_75.setMinimumSize(QtCore.QSize(0, 360))
        self.label_75.setText("")
        self.label_75.setPixmap(QtGui.QPixmap("images/bund2_welcome_vvvv copy 3.png"))
        self.label_75.setObjectName("label_75")
        self.verticalLayout_66.addWidget(self.label_75)
        self.label_76 = QtWidgets.QLabel(self.frame_75)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_76.setFont(font)
        self.label_76.setStyleSheet("QLabel{\n"
"    padding-left: 20px;\n"
"    padding-right:20px;\n"
"}")
        self.label_76.setWordWrap(True)
        self.label_76.setObjectName("label_76")
        self.verticalLayout_66.addWidget(self.label_76)
        self.horizontalLayout_59.addWidget(self.frame_75)
        self.frame_76 = QtWidgets.QFrame(self.frame_74)
        self.frame_76.setMinimumSize(QtCore.QSize(452, 0))
        self.frame_76.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_76.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_76.setObjectName("frame_76")
        self.horizontalLayout_60 = QtWidgets.QHBoxLayout(self.frame_76)
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName("horizontalLayout_60")
        self.label_77 = QtWidgets.QLabel(self.frame_76)
        self.label_77.setText("")
        self.label_77.setPixmap(QtGui.QPixmap("images/bund2_welcome_vvvv copy 4.png"))
        self.label_77.setObjectName("label_77")
        self.horizontalLayout_60.addWidget(self.label_77)
        self.horizontalLayout_59.addWidget(self.frame_76)
        self.verticalLayout_67.addWidget(self.frame_74)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_3.setStyleSheet("QPushButton{\n"
"    color: rgb(77, 77, 77);\n"
"    border: 0.5px solid rgb(191, 191, 191);\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.b2s1_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s1_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s1_button.setObjectName("b2s1_button")
        self.verticalLayout_6.addWidget(self.b2s1_button)
        self.b2s2_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s2_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s2_button.setObjectName("b2s2_button")
        self.verticalLayout_6.addWidget(self.b2s2_button)
        self.b2s3_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s3_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s3_button.setObjectName("b2s3_button")
        self.verticalLayout_6.addWidget(self.b2s3_button)
        self.b2s4_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s4_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s4_button.setObjectName("b2s4_button")
        self.verticalLayout_6.addWidget(self.b2s4_button)
        self.b2s5_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s5_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s5_button.setObjectName("b2s5_button")
        self.verticalLayout_6.addWidget(self.b2s5_button)
        self.b2s6_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s6_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s6_button.setObjectName("b2s6_button")
        self.verticalLayout_6.addWidget(self.b2s6_button)
        self.b2s7_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s7_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s7_button.setObjectName("b2s7_button")
        self.verticalLayout_6.addWidget(self.b2s7_button)
        self.b2s8_button = QtWidgets.QPushButton(self.frame_3)
        self.b2s8_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s8_button.setObjectName("b2s8_button")
        self.verticalLayout_6.addWidget(self.b2s8_button)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout_5.addWidget(self.frame)
        self.stackedWidget_bund2.addWidget(self.choice_bund2)
        self.b2senar1 = QtWidgets.QWidget()
        self.b2senar1.setObjectName("b2senar1")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.b2senar1)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_24 = QtWidgets.QFrame(self.b2senar1)
        self.frame_24.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_24.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_24.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.back_button_b2s1 = QtWidgets.QPushButton(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s1.sizePolicy().hasHeightForWidth())
        self.back_button_b2s1.setSizePolicy(sizePolicy)
        self.back_button_b2s1.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s1.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s1.setText("")
        self.back_button_b2s1.setIcon(icon7)
        self.back_button_b2s1.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s1.setObjectName("back_button_b2s1")
        self.horizontalLayout_20.addWidget(self.back_button_b2s1)
        self.title_b1s_5 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_5.setFont(font)
        self.title_b1s_5.setObjectName("title_b1s_5")
        self.horizontalLayout_20.addWidget(self.title_b1s_5)
        self.verticalLayout_23.addWidget(self.frame_24)
        self.label_26 = QtWidgets.QLabel(self.b2senar1)
        self.label_26.setMinimumSize(QtCore.QSize(0, 30))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_23.addWidget(self.label_26)
        self.b2senar1_tabWidget = QtWidgets.QTabWidget(self.b2senar1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2senar1_tabWidget.sizePolicy().hasHeightForWidth())
        self.b2senar1_tabWidget.setSizePolicy(sizePolicy)
        self.b2senar1_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar1_tabWidget.setObjectName("b2senar1_tabWidget")
        self.b2senar1_measure = QtWidgets.QWidget()
        self.b2senar1_measure.setObjectName("b2senar1_measure")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.b2senar1_measure)
        self.horizontalLayout_21.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.b2senar1_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar1_mesh_plotLayout.setObjectName("b2senar1_mesh_plotLayout")
        self.horizontalLayout_21.addLayout(self.b2senar1_mesh_plotLayout)
        self.frame_25 = QtWidgets.QFrame(self.b2senar1_measure)
        self.frame_25.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_25.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_27 = QtWidgets.QLabel(self.frame_25)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_27.setWordWrap(True)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_24.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.frame_25)
        self.label_28.setMinimumSize(QtCore.QSize(0, 0))
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig1.png"))
        self.label_28.setObjectName("label_28")
        self.verticalLayout_24.addWidget(self.label_28)
        self.horizontalLayout_21.addWidget(self.frame_25)
        self.b2senar1_tabWidget.addTab(self.b2senar1_measure, "")
        self.b2senar1_polar = QtWidgets.QWidget()
        self.b2senar1_polar.setObjectName("b2senar1_polar")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.b2senar1_polar)
        self.horizontalLayout_22.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.b2senar1_layoutPolar = QtWidgets.QVBoxLayout()
        self.b2senar1_layoutPolar.setObjectName("b2senar1_layoutPolar")
        self.horizontalLayout_22.addLayout(self.b2senar1_layoutPolar)
        self.frame_26 = QtWidgets.QFrame(self.b2senar1_polar)
        self.frame_26.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_26.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_26.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_29 = QtWidgets.QLabel(self.frame_26)
        self.label_29.setMinimumSize(QtCore.QSize(0, 100))
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_25.addWidget(self.label_29)
        self.frame_27 = QtWidgets.QFrame(self.frame_26)
        self.frame_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(15)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.b2s1n1_cekbox = QtWidgets.QCheckBox(self.frame_27)
        self.b2s1n1_cekbox.setObjectName("b2s1n1_cekbox")
        self.verticalLayout_26.addWidget(self.b2s1n1_cekbox)
        self.b2s1n2_cekbox = QtWidgets.QCheckBox(self.frame_27)
        self.b2s1n2_cekbox.setObjectName("b2s1n2_cekbox")
        self.verticalLayout_26.addWidget(self.b2s1n2_cekbox)
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.b2s1_applyBtn = QtWidgets.QPushButton(self.frame_28)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b2s1_applyBtn.setFont(font)
        self.b2s1_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s1_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s1_applyBtn.setObjectName("b2s1_applyBtn")
        self.horizontalLayout_23.addWidget(self.b2s1_applyBtn)
        self.b2s1_peakBtn = QtWidgets.QPushButton(self.frame_28)
        self.b2s1_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s1_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s1_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s1_peakBtn.setObjectName("b2s1_peakBtn")
        self.horizontalLayout_23.addWidget(self.b2s1_peakBtn)
        self.verticalLayout_26.addWidget(self.frame_28)
        self.verticalLayout_25.addWidget(self.frame_27)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem8)
        self.label_30 = QtWidgets.QLabel(self.frame_26)
        self.label_30.setMinimumSize(QtCore.QSize(0, 250))
        self.label_30.setMaximumSize(QtCore.QSize(250, 250))
        self.label_30.setText("")
        self.label_30.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_25.addWidget(self.label_30)
        self.horizontalLayout_22.addWidget(self.frame_26)
        self.b2senar1_tabWidget.addTab(self.b2senar1_polar, "")
        self.verticalLayout_23.addWidget(self.b2senar1_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar1)
        self.b2senar2 = QtWidgets.QWidget()
        self.b2senar2.setObjectName("b2senar2")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.b2senar2)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_29 = QtWidgets.QFrame(self.b2senar2)
        self.frame_29.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_29.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.back_button_b2s2 = QtWidgets.QPushButton(self.frame_29)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s2.sizePolicy().hasHeightForWidth())
        self.back_button_b2s2.setSizePolicy(sizePolicy)
        self.back_button_b2s2.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s2.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s2.setText("")
        self.back_button_b2s2.setIcon(icon7)
        self.back_button_b2s2.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s2.setObjectName("back_button_b2s2")
        self.horizontalLayout_24.addWidget(self.back_button_b2s2)
        self.title_b1s_6 = QtWidgets.QLabel(self.frame_29)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_6.setFont(font)
        self.title_b1s_6.setObjectName("title_b1s_6")
        self.horizontalLayout_24.addWidget(self.title_b1s_6)
        self.verticalLayout_27.addWidget(self.frame_29)
        self.label_31 = QtWidgets.QLabel(self.b2senar2)
        self.label_31.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_27.addWidget(self.label_31)
        self.b2senar2_tabWidget = QtWidgets.QTabWidget(self.b2senar2)
        self.b2senar2_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar2_tabWidget.setObjectName("b2senar2_tabWidget")
        self.b2senar2_measure = QtWidgets.QWidget()
        self.b2senar2_measure.setObjectName("b2senar2_measure")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.b2senar2_measure)
        self.horizontalLayout_25.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.b2senar2_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar2_mesh_plotLayout.setObjectName("b2senar2_mesh_plotLayout")
        self.horizontalLayout_25.addLayout(self.b2senar2_mesh_plotLayout)
        self.frame_30 = QtWidgets.QFrame(self.b2senar2_measure)
        self.frame_30.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_30.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_32 = QtWidgets.QLabel(self.frame_30)
        self.label_32.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_28.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.frame_30)
        self.label_33.setMinimumSize(QtCore.QSize(0, 400))
        self.label_33.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig2.png"))
        self.label_33.setObjectName("label_33")
        self.verticalLayout_28.addWidget(self.label_33)
        self.horizontalLayout_25.addWidget(self.frame_30)
        self.b2senar2_tabWidget.addTab(self.b2senar2_measure, "")
        self.b2senar2_polar = QtWidgets.QWidget()
        self.b2senar2_polar.setObjectName("b2senar2_polar")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.b2senar2_polar)
        self.horizontalLayout_26.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.b2senar2_layout_polar = QtWidgets.QVBoxLayout()
        self.b2senar2_layout_polar.setObjectName("b2senar2_layout_polar")
        self.horizontalLayout_26.addLayout(self.b2senar2_layout_polar)
        self.frame_31 = QtWidgets.QFrame(self.b2senar2_polar)
        self.frame_31.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_31.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_31.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_34 = QtWidgets.QLabel(self.frame_31)
        self.label_34.setMinimumSize(QtCore.QSize(0, 100))
        self.label_34.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_29.addWidget(self.label_34)
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy)
        self.frame_32.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(15)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.b2s2n1_cekbox = QtWidgets.QCheckBox(self.frame_32)
        self.b2s2n1_cekbox.setObjectName("b2s2n1_cekbox")
        self.verticalLayout_30.addWidget(self.b2s2n1_cekbox)
        self.b2s2n2_cekbox = QtWidgets.QCheckBox(self.frame_32)
        self.b2s2n2_cekbox.setObjectName("b2s2n2_cekbox")
        self.verticalLayout_30.addWidget(self.b2s2n2_cekbox)
        self.frame_33 = QtWidgets.QFrame(self.frame_32)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy)
        self.frame_33.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_33.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.b2s2_applyBtn = QtWidgets.QPushButton(self.frame_33)
        self.b2s2_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s2_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s2_applyBtn.setObjectName("b2s2_applyBtn")
        self.horizontalLayout_27.addWidget(self.b2s2_applyBtn)
        self.b2s2_peakBtn = QtWidgets.QPushButton(self.frame_33)
        self.b2s2_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s2_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s2_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s2_peakBtn.setObjectName("b2s2_peakBtn")
        self.horizontalLayout_27.addWidget(self.b2s2_peakBtn)
        self.verticalLayout_30.addWidget(self.frame_33)
        self.verticalLayout_29.addWidget(self.frame_32)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem9)
        self.label_35 = QtWidgets.QLabel(self.frame_31)
        self.label_35.setMinimumSize(QtCore.QSize(0, 0))
        self.label_35.setMaximumSize(QtCore.QSize(250, 250))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_29.addWidget(self.label_35)
        self.horizontalLayout_26.addWidget(self.frame_31)
        self.b2senar2_tabWidget.addTab(self.b2senar2_polar, "")
        self.verticalLayout_27.addWidget(self.b2senar2_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar2)
        self.b2senar3 = QtWidgets.QWidget()
        self.b2senar3.setObjectName("b2senar3")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.b2senar3)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.frame_34 = QtWidgets.QFrame(self.b2senar3)
        self.frame_34.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_34.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_34.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setSpacing(15)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.back_button_b2s3 = QtWidgets.QPushButton(self.frame_34)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s3.sizePolicy().hasHeightForWidth())
        self.back_button_b2s3.setSizePolicy(sizePolicy)
        self.back_button_b2s3.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s3.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s3.setText("")
        self.back_button_b2s3.setIcon(icon7)
        self.back_button_b2s3.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s3.setObjectName("back_button_b2s3")
        self.horizontalLayout_28.addWidget(self.back_button_b2s3)
        self.title_b1s_7 = QtWidgets.QLabel(self.frame_34)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_7.setFont(font)
        self.title_b1s_7.setObjectName("title_b1s_7")
        self.horizontalLayout_28.addWidget(self.title_b1s_7)
        self.verticalLayout_31.addWidget(self.frame_34)
        self.label_36 = QtWidgets.QLabel(self.b2senar3)
        self.label_36.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_31.addWidget(self.label_36)
        self.b2senar3_tabWidget = QtWidgets.QTabWidget(self.b2senar3)
        self.b2senar3_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar3_tabWidget.setObjectName("b2senar3_tabWidget")
        self.b2senar3_measure = QtWidgets.QWidget()
        self.b2senar3_measure.setObjectName("b2senar3_measure")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.b2senar3_measure)
        self.horizontalLayout_29.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.b2senar3_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar3_mesh_plotLayout.setObjectName("b2senar3_mesh_plotLayout")
        self.horizontalLayout_29.addLayout(self.b2senar3_mesh_plotLayout)
        self.frame_35 = QtWidgets.QFrame(self.b2senar3_measure)
        self.frame_35.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_35.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_37 = QtWidgets.QLabel(self.frame_35)
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_32.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.frame_35)
        self.label_38.setMinimumSize(QtCore.QSize(0, 400))
        self.label_38.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_38.setText("")
        self.label_38.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig3.png"))
        self.label_38.setObjectName("label_38")
        self.verticalLayout_32.addWidget(self.label_38)
        self.horizontalLayout_29.addWidget(self.frame_35)
        self.b2senar3_tabWidget.addTab(self.b2senar3_measure, "")
        self.b2senar3_polar = QtWidgets.QWidget()
        self.b2senar3_polar.setObjectName("b2senar3_polar")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.b2senar3_polar)
        self.horizontalLayout_30.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.b2senar3_layout_polar = QtWidgets.QVBoxLayout()
        self.b2senar3_layout_polar.setObjectName("b2senar3_layout_polar")
        self.horizontalLayout_30.addLayout(self.b2senar3_layout_polar)
        self.frame_36 = QtWidgets.QFrame(self.b2senar3_polar)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_36.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_36.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_39 = QtWidgets.QLabel(self.frame_36)
        self.label_39.setMinimumSize(QtCore.QSize(0, 100))
        self.label_39.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_39.setWordWrap(True)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_33.addWidget(self.label_39)
        self.frame_37 = QtWidgets.QFrame(self.frame_36)
        self.frame_37.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(15)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.b2s3n1_cekbox = QtWidgets.QCheckBox(self.frame_37)
        self.b2s3n1_cekbox.setObjectName("b2s3n1_cekbox")
        self.verticalLayout_34.addWidget(self.b2s3n1_cekbox)
        self.b2s3n2_cekbox = QtWidgets.QCheckBox(self.frame_37)
        self.b2s3n2_cekbox.setObjectName("b2s3n2_cekbox")
        self.verticalLayout_34.addWidget(self.b2s3n2_cekbox)
        self.b2s3n3_cekbox = QtWidgets.QCheckBox(self.frame_37)
        self.b2s3n3_cekbox.setObjectName("b2s3n3_cekbox")
        self.verticalLayout_34.addWidget(self.b2s3n3_cekbox)
        self.b2s3n4_cekbox = QtWidgets.QCheckBox(self.frame_37)
        self.b2s3n4_cekbox.setObjectName("b2s3n4_cekbox")
        self.verticalLayout_34.addWidget(self.b2s3n4_cekbox)
        self.frame_38 = QtWidgets.QFrame(self.frame_37)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy)
        self.frame_38.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_38.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.b2s3_applyBtn = QtWidgets.QPushButton(self.frame_38)
        self.b2s3_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s3_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s3_applyBtn.setObjectName("b2s3_applyBtn")
        self.horizontalLayout_31.addWidget(self.b2s3_applyBtn)
        self.b2s3_peakBtn = QtWidgets.QPushButton(self.frame_38)
        self.b2s3_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s3_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s3_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s3_peakBtn.setObjectName("b2s3_peakBtn")
        self.horizontalLayout_31.addWidget(self.b2s3_peakBtn)
        self.verticalLayout_34.addWidget(self.frame_38)
        self.verticalLayout_33.addWidget(self.frame_37)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_33.addItem(spacerItem10)
        self.label_40 = QtWidgets.QLabel(self.frame_36)
        self.label_40.setMinimumSize(QtCore.QSize(0, 250))
        self.label_40.setMaximumSize(QtCore.QSize(250, 250))
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_40.setScaledContents(True)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_33.addWidget(self.label_40)
        self.horizontalLayout_30.addWidget(self.frame_36)
        self.b2senar3_tabWidget.addTab(self.b2senar3_polar, "")
        self.verticalLayout_31.addWidget(self.b2senar3_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar3)
        self.b2senar4 = QtWidgets.QWidget()
        self.b2senar4.setObjectName("b2senar4")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.b2senar4)
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_39 = QtWidgets.QFrame(self.b2senar4)
        self.frame_39.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_39.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_39.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_39)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setSpacing(15)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.back_button_b2s4 = QtWidgets.QPushButton(self.frame_39)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s4.sizePolicy().hasHeightForWidth())
        self.back_button_b2s4.setSizePolicy(sizePolicy)
        self.back_button_b2s4.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s4.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s4.setText("")
        self.back_button_b2s4.setIcon(icon7)
        self.back_button_b2s4.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s4.setObjectName("back_button_b2s4")
        self.horizontalLayout_32.addWidget(self.back_button_b2s4)
        self.title_b1s_8 = QtWidgets.QLabel(self.frame_39)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_8.setFont(font)
        self.title_b1s_8.setObjectName("title_b1s_8")
        self.horizontalLayout_32.addWidget(self.title_b1s_8)
        self.verticalLayout_35.addWidget(self.frame_39)
        self.label_41 = QtWidgets.QLabel(self.b2senar4)
        self.label_41.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_35.addWidget(self.label_41)
        self.b2senar4_tabWidget = QtWidgets.QTabWidget(self.b2senar4)
        self.b2senar4_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar4_tabWidget.setObjectName("b2senar4_tabWidget")
        self.b2senar4_measure = QtWidgets.QWidget()
        self.b2senar4_measure.setObjectName("b2senar4_measure")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.b2senar4_measure)
        self.horizontalLayout_33.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.b2senar4_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar4_mesh_plotLayout.setObjectName("b2senar4_mesh_plotLayout")
        self.horizontalLayout_33.addLayout(self.b2senar4_mesh_plotLayout)
        self.frame_40 = QtWidgets.QFrame(self.b2senar4_measure)
        self.frame_40.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_40.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.label_42 = QtWidgets.QLabel(self.frame_40)
        self.label_42.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_42.setWordWrap(True)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_36.addWidget(self.label_42)
        self.label_43 = QtWidgets.QLabel(self.frame_40)
        self.label_43.setMinimumSize(QtCore.QSize(0, 400))
        self.label_43.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig4.png"))
        self.label_43.setObjectName("label_43")
        self.verticalLayout_36.addWidget(self.label_43)
        self.horizontalLayout_33.addWidget(self.frame_40)
        self.b2senar4_tabWidget.addTab(self.b2senar4_measure, "")
        self.b2senar4_polar = QtWidgets.QWidget()
        self.b2senar4_polar.setObjectName("b2senar4_polar")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.b2senar4_polar)
        self.horizontalLayout_34.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.b2senar4_layout_polar = QtWidgets.QVBoxLayout()
        self.b2senar4_layout_polar.setObjectName("b2senar4_layout_polar")
        self.horizontalLayout_34.addLayout(self.b2senar4_layout_polar)
        self.frame_41 = QtWidgets.QFrame(self.b2senar4_polar)
        self.frame_41.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_41.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_41.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_41)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.label_44 = QtWidgets.QLabel(self.frame_41)
        self.label_44.setMinimumSize(QtCore.QSize(0, 100))
        self.label_44.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_44.setWordWrap(True)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_37.addWidget(self.label_44)
        self.frame_42 = QtWidgets.QFrame(self.frame_41)
        self.frame_42.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_42)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setSpacing(15)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.b2s4n1_cekbox = QtWidgets.QCheckBox(self.frame_42)
        self.b2s4n1_cekbox.setObjectName("b2s4n1_cekbox")
        self.verticalLayout_38.addWidget(self.b2s4n1_cekbox)
        self.b2s4n2_cekbox = QtWidgets.QCheckBox(self.frame_42)
        self.b2s4n2_cekbox.setObjectName("b2s4n2_cekbox")
        self.verticalLayout_38.addWidget(self.b2s4n2_cekbox)
        self.b2s4n3_cekbox = QtWidgets.QCheckBox(self.frame_42)
        self.b2s4n3_cekbox.setObjectName("b2s4n3_cekbox")
        self.verticalLayout_38.addWidget(self.b2s4n3_cekbox)
        self.frame_43 = QtWidgets.QFrame(self.frame_42)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy)
        self.frame_43.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_43.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.b2s4_applyBtn = QtWidgets.QPushButton(self.frame_43)
        self.b2s4_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s4_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s4_applyBtn.setObjectName("b2s4_applyBtn")
        self.horizontalLayout_35.addWidget(self.b2s4_applyBtn)
        self.b2s4_peakBtn = QtWidgets.QPushButton(self.frame_43)
        self.b2s4_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s4_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s4_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s4_peakBtn.setObjectName("b2s4_peakBtn")
        self.horizontalLayout_35.addWidget(self.b2s4_peakBtn)
        self.verticalLayout_38.addWidget(self.frame_43)
        self.verticalLayout_37.addWidget(self.frame_42)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_37.addItem(spacerItem11)
        self.label_45 = QtWidgets.QLabel(self.frame_41)
        self.label_45.setMinimumSize(QtCore.QSize(0, 250))
        self.label_45.setMaximumSize(QtCore.QSize(250, 250))
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_37.addWidget(self.label_45)
        self.horizontalLayout_34.addWidget(self.frame_41)
        self.b2senar4_tabWidget.addTab(self.b2senar4_polar, "")
        self.verticalLayout_35.addWidget(self.b2senar4_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar4)
        self.b2senar5 = QtWidgets.QWidget()
        self.b2senar5.setObjectName("b2senar5")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout(self.b2senar5)
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_48.setSpacing(10)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.frame_50 = QtWidgets.QFrame(self.b2senar5)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_50.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_50.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_50.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_40.setSpacing(15)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.back_button_b2s5 = QtWidgets.QPushButton(self.frame_50)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s5.sizePolicy().hasHeightForWidth())
        self.back_button_b2s5.setSizePolicy(sizePolicy)
        self.back_button_b2s5.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s5.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s5.setText("")
        self.back_button_b2s5.setIcon(icon7)
        self.back_button_b2s5.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s5.setObjectName("back_button_b2s5")
        self.horizontalLayout_40.addWidget(self.back_button_b2s5)
        self.title_b1s_10 = QtWidgets.QLabel(self.frame_50)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_10.setFont(font)
        self.title_b1s_10.setObjectName("title_b1s_10")
        self.horizontalLayout_40.addWidget(self.title_b1s_10)
        self.verticalLayout_48.addWidget(self.frame_50)
        self.label_55 = QtWidgets.QLabel(self.b2senar5)
        self.label_55.setMinimumSize(QtCore.QSize(0, 30))
        self.label_55.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_48.addWidget(self.label_55)
        self.b2senar5_tabWidget = QtWidgets.QTabWidget(self.b2senar5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2senar5_tabWidget.sizePolicy().hasHeightForWidth())
        self.b2senar5_tabWidget.setSizePolicy(sizePolicy)
        self.b2senar5_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar5_tabWidget.setObjectName("b2senar5_tabWidget")
        self.b2senar5_measure = QtWidgets.QWidget()
        self.b2senar5_measure.setObjectName("b2senar5_measure")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.b2senar5_measure)
        self.horizontalLayout_41.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.b2senar5_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar5_mesh_plotLayout.setObjectName("b2senar5_mesh_plotLayout")
        self.horizontalLayout_41.addLayout(self.b2senar5_mesh_plotLayout)
        self.frame_51 = QtWidgets.QFrame(self.b2senar5_measure)
        self.frame_51.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_51.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.label_51 = QtWidgets.QLabel(self.frame_51)
        self.label_51.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_51.setWordWrap(True)
        self.label_51.setObjectName("label_51")
        self.verticalLayout_45.addWidget(self.label_51)
        self.label_52 = QtWidgets.QLabel(self.frame_51)
        self.label_52.setMinimumSize(QtCore.QSize(0, 0))
        self.label_52.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_52.setText("")
        self.label_52.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig5.png"))
        self.label_52.setObjectName("label_52")
        self.verticalLayout_45.addWidget(self.label_52)
        self.horizontalLayout_41.addWidget(self.frame_51)
        self.b2senar5_tabWidget.addTab(self.b2senar5_measure, "")
        self.b2senar5_polar = QtWidgets.QWidget()
        self.b2senar5_polar.setObjectName("b2senar5_polar")
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout(self.b2senar5_polar)
        self.horizontalLayout_42.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.b2senar5_layoutPolar = QtWidgets.QVBoxLayout()
        self.b2senar5_layoutPolar.setObjectName("b2senar5_layoutPolar")
        self.horizontalLayout_42.addLayout(self.b2senar5_layoutPolar)
        self.frame_52 = QtWidgets.QFrame(self.b2senar5_polar)
        self.frame_52.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_52.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_52.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_53 = QtWidgets.QLabel(self.frame_52)
        self.label_53.setMinimumSize(QtCore.QSize(0, 100))
        self.label_53.setWordWrap(True)
        self.label_53.setObjectName("label_53")
        self.verticalLayout_46.addWidget(self.label_53)
        self.frame_53 = QtWidgets.QFrame(self.frame_52)
        self.frame_53.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_47.setSpacing(15)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.b2s5n1_cekbox = QtWidgets.QCheckBox(self.frame_53)
        self.b2s5n1_cekbox.setObjectName("b2s5n1_cekbox")
        self.verticalLayout_47.addWidget(self.b2s5n1_cekbox)
        self.b2s5n2_cekbox = QtWidgets.QCheckBox(self.frame_53)
        self.b2s5n2_cekbox.setObjectName("b2s5n2_cekbox")
        self.verticalLayout_47.addWidget(self.b2s5n2_cekbox)
        self.frame_54 = QtWidgets.QFrame(self.frame_53)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy)
        self.frame_54.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_54.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.frame_54)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.b2s5_applyBtn = QtWidgets.QPushButton(self.frame_54)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b2s5_applyBtn.setFont(font)
        self.b2s5_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s5_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s5_applyBtn.setObjectName("b2s5_applyBtn")
        self.horizontalLayout_43.addWidget(self.b2s5_applyBtn)
        self.b2s5_peakBtn = QtWidgets.QPushButton(self.frame_54)
        self.b2s5_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s5_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s5_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s5_peakBtn.setObjectName("b2s5_peakBtn")
        self.horizontalLayout_43.addWidget(self.b2s5_peakBtn)
        self.verticalLayout_47.addWidget(self.frame_54)
        self.verticalLayout_46.addWidget(self.frame_53)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_46.addItem(spacerItem12)
        self.label_54 = QtWidgets.QLabel(self.frame_52)
        self.label_54.setMinimumSize(QtCore.QSize(0, 250))
        self.label_54.setMaximumSize(QtCore.QSize(250, 250))
        self.label_54.setText("")
        self.label_54.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_54.setScaledContents(True)
        self.label_54.setObjectName("label_54")
        self.verticalLayout_46.addWidget(self.label_54)
        self.horizontalLayout_42.addWidget(self.frame_52)
        self.b2senar5_tabWidget.addTab(self.b2senar5_polar, "")
        self.verticalLayout_48.addWidget(self.b2senar5_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar5)
        self.b2senar6 = QtWidgets.QWidget()
        self.b2senar6.setObjectName("b2senar6")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.b2senar6)
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_44.setSpacing(10)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.frame_49 = QtWidgets.QFrame(self.b2senar6)
        self.frame_49.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_49.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_49.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_49)
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39.setSpacing(15)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.back_button_b2s6 = QtWidgets.QPushButton(self.frame_49)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s6.sizePolicy().hasHeightForWidth())
        self.back_button_b2s6.setSizePolicy(sizePolicy)
        self.back_button_b2s6.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s6.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s6.setText("")
        self.back_button_b2s6.setIcon(icon7)
        self.back_button_b2s6.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s6.setObjectName("back_button_b2s6")
        self.horizontalLayout_39.addWidget(self.back_button_b2s6)
        self.title_b1s_9 = QtWidgets.QLabel(self.frame_49)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_9.setFont(font)
        self.title_b1s_9.setObjectName("title_b1s_9")
        self.horizontalLayout_39.addWidget(self.title_b1s_9)
        self.verticalLayout_44.addWidget(self.frame_49)
        self.label_50 = QtWidgets.QLabel(self.b2senar6)
        self.label_50.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_44.addWidget(self.label_50)
        self.b2senar6_tabWidget = QtWidgets.QTabWidget(self.b2senar6)
        self.b2senar6_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar6_tabWidget.setObjectName("b2senar6_tabWidget")
        self.b2senar6_measure = QtWidgets.QWidget()
        self.b2senar6_measure.setObjectName("b2senar6_measure")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.b2senar6_measure)
        self.horizontalLayout_36.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.b2senar6_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar6_mesh_plotLayout.setObjectName("b2senar6_mesh_plotLayout")
        self.horizontalLayout_36.addLayout(self.b2senar6_mesh_plotLayout)
        self.frame_45 = QtWidgets.QFrame(self.b2senar6_measure)
        self.frame_45.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_45.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.label_46 = QtWidgets.QLabel(self.frame_45)
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_46.setWordWrap(True)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_41.addWidget(self.label_46)
        self.label_47 = QtWidgets.QLabel(self.frame_45)
        self.label_47.setMinimumSize(QtCore.QSize(0, 400))
        self.label_47.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_47.setText("")
        self.label_47.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig6.png"))
        self.label_47.setObjectName("label_47")
        self.verticalLayout_41.addWidget(self.label_47)
        self.horizontalLayout_36.addWidget(self.frame_45)
        self.b2senar6_tabWidget.addTab(self.b2senar6_measure, "")
        self.b2senar6_polar = QtWidgets.QWidget()
        self.b2senar6_polar.setObjectName("b2senar6_polar")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.b2senar6_polar)
        self.horizontalLayout_37.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.b2senar6_layoutPolar = QtWidgets.QVBoxLayout()
        self.b2senar6_layoutPolar.setObjectName("b2senar6_layoutPolar")
        self.horizontalLayout_37.addLayout(self.b2senar6_layoutPolar)
        self.frame_46 = QtWidgets.QFrame(self.b2senar6_polar)
        self.frame_46.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_46.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_46.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.label_48 = QtWidgets.QLabel(self.frame_46)
        self.label_48.setMinimumSize(QtCore.QSize(0, 100))
        self.label_48.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_48.setWordWrap(True)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_42.addWidget(self.label_48)
        self.frame_47 = QtWidgets.QFrame(self.frame_46)
        self.frame_47.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setSpacing(15)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.b2s6n1_cekbox = QtWidgets.QCheckBox(self.frame_47)
        self.b2s6n1_cekbox.setObjectName("b2s6n1_cekbox")
        self.verticalLayout_43.addWidget(self.b2s6n1_cekbox)
        self.b2s6n2_cekbox = QtWidgets.QCheckBox(self.frame_47)
        self.b2s6n2_cekbox.setObjectName("b2s6n2_cekbox")
        self.verticalLayout_43.addWidget(self.b2s6n2_cekbox)
        self.b2s6n3_cekbox = QtWidgets.QCheckBox(self.frame_47)
        self.b2s6n3_cekbox.setObjectName("b2s6n3_cekbox")
        self.verticalLayout_43.addWidget(self.b2s6n3_cekbox)
        self.b2s6n4_cekbox = QtWidgets.QCheckBox(self.frame_47)
        self.b2s6n4_cekbox.setObjectName("b2s6n4_cekbox")
        self.verticalLayout_43.addWidget(self.b2s6n4_cekbox)
        self.frame_48 = QtWidgets.QFrame(self.frame_47)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy)
        self.frame_48.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_48.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.b2s6_applyBtn = QtWidgets.QPushButton(self.frame_48)
        self.b2s6_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s6_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s6_applyBtn.setObjectName("b2s6_applyBtn")
        self.horizontalLayout_38.addWidget(self.b2s6_applyBtn)
        self.b2s6_peakBtn = QtWidgets.QPushButton(self.frame_48)
        self.b2s6_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s6_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s6_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s6_peakBtn.setObjectName("b2s6_peakBtn")
        self.horizontalLayout_38.addWidget(self.b2s6_peakBtn)
        self.verticalLayout_43.addWidget(self.frame_48)
        self.verticalLayout_42.addWidget(self.frame_47)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_42.addItem(spacerItem13)
        self.label_49 = QtWidgets.QLabel(self.frame_46)
        self.label_49.setMinimumSize(QtCore.QSize(0, 250))
        self.label_49.setMaximumSize(QtCore.QSize(250, 250))
        self.label_49.setText("")
        self.label_49.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_49.setScaledContents(True)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_42.addWidget(self.label_49)
        self.horizontalLayout_37.addWidget(self.frame_46)
        self.b2senar6_tabWidget.addTab(self.b2senar6_polar, "")
        self.verticalLayout_44.addWidget(self.b2senar6_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar6)
        self.b2senar7 = QtWidgets.QWidget()
        self.b2senar7.setObjectName("b2senar7")
        self.verticalLayout_52 = QtWidgets.QVBoxLayout(self.b2senar7)
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_52.setSpacing(10)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.frame_55 = QtWidgets.QFrame(self.b2senar7)
        self.frame_55.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_55.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_55.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_55.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.frame_55)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setSpacing(15)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.back_button_b2s7 = QtWidgets.QPushButton(self.frame_55)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s7.sizePolicy().hasHeightForWidth())
        self.back_button_b2s7.setSizePolicy(sizePolicy)
        self.back_button_b2s7.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s7.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s7.setText("")
        self.back_button_b2s7.setIcon(icon7)
        self.back_button_b2s7.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s7.setObjectName("back_button_b2s7")
        self.horizontalLayout_44.addWidget(self.back_button_b2s7)
        self.title_b1s_11 = QtWidgets.QLabel(self.frame_55)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_11.setFont(font)
        self.title_b1s_11.setObjectName("title_b1s_11")
        self.horizontalLayout_44.addWidget(self.title_b1s_11)
        self.verticalLayout_52.addWidget(self.frame_55)
        self.label_60 = QtWidgets.QLabel(self.b2senar7)
        self.label_60.setMinimumSize(QtCore.QSize(0, 30))
        self.label_60.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_52.addWidget(self.label_60)
        self.b2senar7_tabWidget = QtWidgets.QTabWidget(self.b2senar7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2senar7_tabWidget.sizePolicy().hasHeightForWidth())
        self.b2senar7_tabWidget.setSizePolicy(sizePolicy)
        self.b2senar7_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar7_tabWidget.setObjectName("b2senar7_tabWidget")
        self.b2senar7_measure = QtWidgets.QWidget()
        self.b2senar7_measure.setObjectName("b2senar7_measure")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.b2senar7_measure)
        self.horizontalLayout_45.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.b2senar7_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar7_mesh_plotLayout.setObjectName("b2senar7_mesh_plotLayout")
        self.horizontalLayout_45.addLayout(self.b2senar7_mesh_plotLayout)
        self.frame_56 = QtWidgets.QFrame(self.b2senar7_measure)
        self.frame_56.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_56.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.frame_56)
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        self.label_56 = QtWidgets.QLabel(self.frame_56)
        self.label_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_56.setWordWrap(True)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_49.addWidget(self.label_56)
        self.label_57 = QtWidgets.QLabel(self.frame_56)
        self.label_57.setMinimumSize(QtCore.QSize(0, 0))
        self.label_57.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_57.setText("")
        self.label_57.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig7.png"))
        self.label_57.setObjectName("label_57")
        self.verticalLayout_49.addWidget(self.label_57)
        self.horizontalLayout_45.addWidget(self.frame_56)
        self.b2senar7_tabWidget.addTab(self.b2senar7_measure, "")
        self.b2senar7_polar = QtWidgets.QWidget()
        self.b2senar7_polar.setObjectName("b2senar7_polar")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.b2senar7_polar)
        self.horizontalLayout_46.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.b2senar7_layoutPolar = QtWidgets.QVBoxLayout()
        self.b2senar7_layoutPolar.setObjectName("b2senar7_layoutPolar")
        self.horizontalLayout_46.addLayout(self.b2senar7_layoutPolar)
        self.frame_57 = QtWidgets.QFrame(self.b2senar7_polar)
        self.frame_57.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_57.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_57.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_57)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.label_58 = QtWidgets.QLabel(self.frame_57)
        self.label_58.setMinimumSize(QtCore.QSize(0, 100))
        self.label_58.setWordWrap(True)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_50.addWidget(self.label_58)
        self.frame_58 = QtWidgets.QFrame(self.frame_57)
        self.frame_58.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout(self.frame_58)
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_51.setSpacing(15)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.b2s7n1_cekbox = QtWidgets.QCheckBox(self.frame_58)
        self.b2s7n1_cekbox.setObjectName("b2s7n1_cekbox")
        self.verticalLayout_51.addWidget(self.b2s7n1_cekbox)
        self.b2s7n2_cekbox = QtWidgets.QCheckBox(self.frame_58)
        self.b2s7n2_cekbox.setObjectName("b2s7n2_cekbox")
        self.verticalLayout_51.addWidget(self.b2s7n2_cekbox)
        self.frame_59 = QtWidgets.QFrame(self.frame_58)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy)
        self.frame_59.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_59.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.frame_59)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.b2s7_applyBtn = QtWidgets.QPushButton(self.frame_59)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b2s7_applyBtn.setFont(font)
        self.b2s7_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s7_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s7_applyBtn.setObjectName("b2s7_applyBtn")
        self.horizontalLayout_47.addWidget(self.b2s7_applyBtn)
        self.b2s7_peakBtn = QtWidgets.QPushButton(self.frame_59)
        self.b2s7_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s7_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s7_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s7_peakBtn.setObjectName("b2s7_peakBtn")
        self.horizontalLayout_47.addWidget(self.b2s7_peakBtn)
        self.verticalLayout_51.addWidget(self.frame_59)
        self.verticalLayout_50.addWidget(self.frame_58)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_50.addItem(spacerItem14)
        self.label_59 = QtWidgets.QLabel(self.frame_57)
        self.label_59.setMinimumSize(QtCore.QSize(0, 250))
        self.label_59.setMaximumSize(QtCore.QSize(250, 250))
        self.label_59.setText("")
        self.label_59.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_59.setScaledContents(True)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_50.addWidget(self.label_59)
        self.horizontalLayout_46.addWidget(self.frame_57)
        self.b2senar7_tabWidget.addTab(self.b2senar7_polar, "")
        self.verticalLayout_52.addWidget(self.b2senar7_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar7)
        self.b2senar8 = QtWidgets.QWidget()
        self.b2senar8.setObjectName("b2senar8")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.b2senar8)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setSpacing(10)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.frame_60 = QtWidgets.QFrame(self.b2senar8)
        self.frame_60.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_60.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_60.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.frame_60.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.frame_60)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setSpacing(15)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.back_button_b2s8 = QtWidgets.QPushButton(self.frame_60)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button_b2s8.sizePolicy().hasHeightForWidth())
        self.back_button_b2s8.setSizePolicy(sizePolicy)
        self.back_button_b2s8.setMinimumSize(QtCore.QSize(40, 40))
        self.back_button_b2s8.setMaximumSize(QtCore.QSize(40, 40))
        self.back_button_b2s8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button_b2s8.setText("")
        self.back_button_b2s8.setIcon(icon7)
        self.back_button_b2s8.setIconSize(QtCore.QSize(16, 16))
        self.back_button_b2s8.setObjectName("back_button_b2s8")
        self.horizontalLayout_48.addWidget(self.back_button_b2s8)
        self.title_b1s_12 = QtWidgets.QLabel(self.frame_60)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.title_b1s_12.setFont(font)
        self.title_b1s_12.setObjectName("title_b1s_12")
        self.horizontalLayout_48.addWidget(self.title_b1s_12)
        self.verticalLayout_56.addWidget(self.frame_60)
        self.label_65 = QtWidgets.QLabel(self.b2senar8)
        self.label_65.setMinimumSize(QtCore.QSize(0, 30))
        self.label_65.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.verticalLayout_56.addWidget(self.label_65)
        self.b2senar8_tabWidget = QtWidgets.QTabWidget(self.b2senar8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b2senar8_tabWidget.sizePolicy().hasHeightForWidth())
        self.b2senar8_tabWidget.setSizePolicy(sizePolicy)
        self.b2senar8_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.b2senar8_tabWidget.setObjectName("b2senar8_tabWidget")
        self.b2senar8_measure = QtWidgets.QWidget()
        self.b2senar8_measure.setObjectName("b2senar8_measure")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.b2senar8_measure)
        self.horizontalLayout_49.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.b2senar8_mesh_plotLayout = QtWidgets.QVBoxLayout()
        self.b2senar8_mesh_plotLayout.setObjectName("b2senar8_mesh_plotLayout")
        self.horizontalLayout_49.addLayout(self.b2senar8_mesh_plotLayout)
        self.frame_61 = QtWidgets.QFrame(self.b2senar8_measure)
        self.frame_61.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_61.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        self.label_61 = QtWidgets.QLabel(self.frame_61)
        self.label_61.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_61.setWordWrap(True)
        self.label_61.setObjectName("label_61")
        self.verticalLayout_53.addWidget(self.label_61)
        self.label_62 = QtWidgets.QLabel(self.frame_61)
        self.label_62.setMinimumSize(QtCore.QSize(0, 0))
        self.label_62.setMaximumSize(QtCore.QSize(16777215, 400))
        self.label_62.setText("")
        self.label_62.setPixmap(QtGui.QPixmap("images/Skripsi_bund2_fig8.png"))
        self.label_62.setObjectName("label_62")
        self.verticalLayout_53.addWidget(self.label_62)
        self.horizontalLayout_49.addWidget(self.frame_61)
        self.b2senar8_tabWidget.addTab(self.b2senar8_measure, "")
        self.b2senar8_polar = QtWidgets.QWidget()
        self.b2senar8_polar.setObjectName("b2senar8_polar")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.b2senar8_polar)
        self.horizontalLayout_50.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.b2senar8_layoutPolar = QtWidgets.QVBoxLayout()
        self.b2senar8_layoutPolar.setObjectName("b2senar8_layoutPolar")
        self.horizontalLayout_50.addLayout(self.b2senar8_layoutPolar)
        self.frame_62 = QtWidgets.QFrame(self.b2senar8_polar)
        self.frame_62.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_62.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_62.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.frame_62)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.label_63 = QtWidgets.QLabel(self.frame_62)
        self.label_63.setMinimumSize(QtCore.QSize(0, 100))
        self.label_63.setWordWrap(True)
        self.label_63.setObjectName("label_63")
        self.verticalLayout_54.addWidget(self.label_63)
        self.frame_63 = QtWidgets.QFrame(self.frame_62)
        self.frame_63.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_63)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(15)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.b2s8n1_cekbox = QtWidgets.QCheckBox(self.frame_63)
        self.b2s8n1_cekbox.setObjectName("b2s8n1_cekbox")
        self.verticalLayout_55.addWidget(self.b2s8n1_cekbox)
        self.b2s8n2_cekbox = QtWidgets.QCheckBox(self.frame_63)
        self.b2s8n2_cekbox.setObjectName("b2s8n2_cekbox")
        self.verticalLayout_55.addWidget(self.b2s8n2_cekbox)
        self.frame_64 = QtWidgets.QFrame(self.frame_63)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy)
        self.frame_64.setMinimumSize(QtCore.QSize(296, 0))
        self.frame_64.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.frame_64)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.b2s8_applyBtn = QtWidgets.QPushButton(self.frame_64)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.b2s8_applyBtn.setFont(font)
        self.b2s8_applyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s8_applyBtn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(11, 10, 52);\n"
"}")
        self.b2s8_applyBtn.setObjectName("b2s8_applyBtn")
        self.horizontalLayout_51.addWidget(self.b2s8_applyBtn)
        self.b2s8_peakBtn = QtWidgets.QPushButton(self.frame_64)
        self.b2s8_peakBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.b2s8_peakBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2s8_peakBtn.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    color: #303f9f;\n"
"    border-radius:4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"}")
        self.b2s8_peakBtn.setObjectName("b2s8_peakBtn")
        self.horizontalLayout_51.addWidget(self.b2s8_peakBtn)
        self.verticalLayout_55.addWidget(self.frame_64)
        self.verticalLayout_54.addWidget(self.frame_63)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_54.addItem(spacerItem15)
        self.label_64 = QtWidgets.QLabel(self.frame_62)
        self.label_64.setMinimumSize(QtCore.QSize(0, 250))
        self.label_64.setMaximumSize(QtCore.QSize(250, 250))
        self.label_64.setText("")
        self.label_64.setPixmap(QtGui.QPixmap("images/clue_polar.png"))
        self.label_64.setScaledContents(True)
        self.label_64.setObjectName("label_64")
        self.verticalLayout_54.addWidget(self.label_64)
        self.horizontalLayout_50.addWidget(self.frame_62)
        self.b2senar8_tabWidget.addTab(self.b2senar8_polar, "")
        self.verticalLayout_56.addWidget(self.b2senar8_tabWidget)
        self.stackedWidget_bund2.addWidget(self.b2senar8)
        self.verticalLayout_3.addWidget(self.stackedWidget_bund2)
        self.pages_widget.addWidget(self.bund2_page)
        self.compare_page = QtWidgets.QWidget()
        self.compare_page.setObjectName("compare_page")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.compare_page)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.label_3 = QtWidgets.QLabel(self.compare_page)
        self.label_3.setMinimumSize(QtCore.QSize(0, 125))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_60.addWidget(self.label_3)
        self.compare_tabWidget = QtWidgets.QTabWidget(self.compare_page)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.compare_tabWidget.setFont(font)
        self.compare_tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 0; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border-bottom: 1px solid rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-radius: 0px;\n"
"    border-bottom: 1.5px solid #303f9f;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    color: #303f9f;\n"
"    background: #ecf0f1;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8px;\n"
"    margin-right: 1px;\n"
"    padding: 7px 15px 10px 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.compare_tabWidget.setObjectName("compare_tabWidget")
        self.compareb1 = QtWidgets.QWidget()
        self.compareb1.setObjectName("compareb1")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.compareb1)
        self.horizontalLayout_52.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_52.setSpacing(10)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.layout_polar_compare1 = QtWidgets.QVBoxLayout()
        self.layout_polar_compare1.setObjectName("layout_polar_compare1")
        self.horizontalLayout_52.addLayout(self.layout_polar_compare1)
        self.bund1_compare_side_3 = QtWidgets.QFrame(self.compareb1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bund1_compare_side_3.sizePolicy().hasHeightForWidth())
        self.bund1_compare_side_3.setSizePolicy(sizePolicy)
        self.bund1_compare_side_3.setMinimumSize(QtCore.QSize(0, 0))
        self.bund1_compare_side_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.bund1_compare_side_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bund1_compare_side_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bund1_compare_side_3.setObjectName("bund1_compare_side_3")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.bund1_compare_side_3)
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.label_66 = QtWidgets.QLabel(self.bund1_compare_side_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy)
        self.label_66.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.label_66.setFont(font)
        self.label_66.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_66.setWordWrap(True)
        self.label_66.setObjectName("label_66")
        self.verticalLayout_57.addWidget(self.label_66)
        self.frame_65 = QtWidgets.QFrame(self.bund1_compare_side_3)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.frame_65.setFont(font)
        self.frame_65.setStyleSheet("QPushButton{\n"
"    color: rgb(77, 77, 77);\n"
"    border: 0.5px solid rgb(191, 191, 191);\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"}")
        self.frame_65.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.frame_65)
        self.verticalLayout_58.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_58.setSpacing(20)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.compareb1s1 = QtWidgets.QPushButton(self.frame_65)
        self.compareb1s1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb1s1.setObjectName("compareb1s1")
        self.verticalLayout_58.addWidget(self.compareb1s1)
        self.compareb1s2 = QtWidgets.QPushButton(self.frame_65)
        self.compareb1s2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb1s2.setObjectName("compareb1s2")
        self.verticalLayout_58.addWidget(self.compareb1s2)
        self.compareb1s3 = QtWidgets.QPushButton(self.frame_65)
        self.compareb1s3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb1s3.setObjectName("compareb1s3")
        self.verticalLayout_58.addWidget(self.compareb1s3)
        self.compareb1s4 = QtWidgets.QPushButton(self.frame_65)
        self.compareb1s4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb1s4.setObjectName("compareb1s4")
        self.verticalLayout_58.addWidget(self.compareb1s4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_58.addItem(spacerItem16)
        self.frame_87 = QtWidgets.QFrame(self.frame_65)
        self.frame_87.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_87.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_87.setObjectName("frame_87")
        self.horizontalLayout_69 = QtWidgets.QHBoxLayout(self.frame_87)
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_69.setSpacing(10)
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.ket_arahb1 = QtWidgets.QPushButton(self.frame_87)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ket_arahb1.sizePolicy().hasHeightForWidth())
        self.ket_arahb1.setSizePolicy(sizePolicy)
        self.ket_arahb1.setMinimumSize(QtCore.QSize(50, 0))
        self.ket_arahb1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ket_arahb1.setStyleSheet("QPushButton{\n"
"    border: 0.5px solid rgb(77, 77, 77);\n"
"    border-radius: 7px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"    color: r#4d4d4d;\n"
"}")
        self.ket_arahb1.setObjectName("ket_arahb1")
        self.horizontalLayout_69.addWidget(self.ket_arahb1)
        self.clear_compare1_btn = QtWidgets.QPushButton(self.frame_87)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_compare1_btn.sizePolicy().hasHeightForWidth())
        self.clear_compare1_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.clear_compare1_btn.setFont(font)
        self.clear_compare1_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_compare1_btn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(46, 19, 84);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_compare1_btn.setIcon(icon8)
        self.clear_compare1_btn.setObjectName("clear_compare1_btn")
        self.horizontalLayout_69.addWidget(self.clear_compare1_btn)
        self.verticalLayout_58.addWidget(self.frame_87)
        self.verticalLayout_57.addWidget(self.frame_65)
        self.horizontalLayout_52.addWidget(self.bund1_compare_side_3)
        self.compare_tabWidget.addTab(self.compareb1, "")
        self.compareb2 = QtWidgets.QWidget()
        self.compareb2.setObjectName("compareb2")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.compareb2)
        self.horizontalLayout_57.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_57.setSpacing(10)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.layout_polar_compare2 = QtWidgets.QVBoxLayout()
        self.layout_polar_compare2.setObjectName("layout_polar_compare2")
        self.horizontalLayout_57.addLayout(self.layout_polar_compare2)
        self.bund2_compare_side = QtWidgets.QFrame(self.compareb2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bund2_compare_side.sizePolicy().hasHeightForWidth())
        self.bund2_compare_side.setSizePolicy(sizePolicy)
        self.bund2_compare_side.setMinimumSize(QtCore.QSize(0, 0))
        self.bund2_compare_side.setMaximumSize(QtCore.QSize(250, 16777215))
        self.bund2_compare_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bund2_compare_side.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bund2_compare_side.setObjectName("bund2_compare_side")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout(self.bund2_compare_side)
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.label_72 = QtWidgets.QLabel(self.bund2_compare_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_72.sizePolicy().hasHeightForWidth())
        self.label_72.setSizePolicy(sizePolicy)
        self.label_72.setMinimumSize(QtCore.QSize(0, 125))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.label_72.setFont(font)
        self.label_72.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_72.setWordWrap(True)
        self.label_72.setObjectName("label_72")
        self.verticalLayout_62.addWidget(self.label_72)
        self.frame_71 = QtWidgets.QFrame(self.bund2_compare_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.frame_71.setFont(font)
        self.frame_71.setStyleSheet("QPushButton{\n"
"    color: rgb(77, 77, 77);\n"
"    border: 0.5px solid rgb(191, 191, 191);\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"}")
        self.frame_71.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.verticalLayout_81 = QtWidgets.QVBoxLayout(self.frame_71)
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_81.setSpacing(10)
        self.verticalLayout_81.setObjectName("verticalLayout_81")
        self.compareb2s1 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s1.setObjectName("compareb2s1")
        self.verticalLayout_81.addWidget(self.compareb2s1)
        self.compareb2s2 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s2.setObjectName("compareb2s2")
        self.verticalLayout_81.addWidget(self.compareb2s2)
        self.compareb2s3 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s3.setObjectName("compareb2s3")
        self.verticalLayout_81.addWidget(self.compareb2s3)
        self.compareb2s4 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s4.setObjectName("compareb2s4")
        self.verticalLayout_81.addWidget(self.compareb2s4)
        self.compareb2s5 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s5.setObjectName("compareb2s5")
        self.verticalLayout_81.addWidget(self.compareb2s5)
        self.compareb2s6 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s6.setObjectName("compareb2s6")
        self.verticalLayout_81.addWidget(self.compareb2s6)
        self.compareb2s7 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s7.setObjectName("compareb2s7")
        self.verticalLayout_81.addWidget(self.compareb2s7)
        self.compareb2s8 = QtWidgets.QPushButton(self.frame_71)
        self.compareb2s8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.compareb2s8.setObjectName("compareb2s8")
        self.verticalLayout_81.addWidget(self.compareb2s8)
        self.verticalLayout_62.addWidget(self.frame_71)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_62.addItem(spacerItem17)
        self.frame_88 = QtWidgets.QFrame(self.bund2_compare_side)
        self.frame_88.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_88.setObjectName("frame_88")
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout(self.frame_88)
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_70.setSpacing(10)
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.ket_arahb2 = QtWidgets.QPushButton(self.frame_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ket_arahb2.sizePolicy().hasHeightForWidth())
        self.ket_arahb2.setSizePolicy(sizePolicy)
        self.ket_arahb2.setMinimumSize(QtCore.QSize(50, 30))
        self.ket_arahb2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ket_arahb2.setStyleSheet("QPushButton{\n"
"    border: 0.5px solid rgb(77, 77, 77);\n"
"    border-radius: 7px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"    color: r#4d4d4d;\n"
"}")
        self.ket_arahb2.setObjectName("ket_arahb2")
        self.horizontalLayout_70.addWidget(self.ket_arahb2)
        self.clear_compare2_btn = QtWidgets.QPushButton(self.frame_88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_compare2_btn.sizePolicy().hasHeightForWidth())
        self.clear_compare2_btn.setSizePolicy(sizePolicy)
        self.clear_compare2_btn.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        self.clear_compare2_btn.setFont(font)
        self.clear_compare2_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_compare2_btn.setStyleSheet("QPushButton{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(46, 19, 84);\n"
"}")
        self.clear_compare2_btn.setIcon(icon8)
        self.clear_compare2_btn.setObjectName("clear_compare2_btn")
        self.horizontalLayout_70.addWidget(self.clear_compare2_btn)
        self.verticalLayout_62.addWidget(self.frame_88)
        self.horizontalLayout_57.addWidget(self.bund2_compare_side)
        self.compare_tabWidget.addTab(self.compareb2, "")
        self.compareb12 = QtWidgets.QWidget()
        self.compareb12.setObjectName("compareb12")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.compareb12)
        self.horizontalLayout_58.setContentsMargins(0, 10, 0, 0)
        self.horizontalLayout_58.setSpacing(10)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.layout_polar_compare12 = QtWidgets.QVBoxLayout()
        self.layout_polar_compare12.setObjectName("layout_polar_compare12")
        self.horizontalLayout_58.addLayout(self.layout_polar_compare12)
        self.bund1_compare_side_15 = QtWidgets.QFrame(self.compareb12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bund1_compare_side_15.sizePolicy().hasHeightForWidth())
        self.bund1_compare_side_15.setSizePolicy(sizePolicy)
        self.bund1_compare_side_15.setMinimumSize(QtCore.QSize(0, 0))
        self.bund1_compare_side_15.setMaximumSize(QtCore.QSize(300, 16777215))
        self.bund1_compare_side_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bund1_compare_side_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.bund1_compare_side_15.setObjectName("bund1_compare_side_15")
        self.verticalLayout_61 = QtWidgets.QVBoxLayout(self.bund1_compare_side_15)
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.label_73 = QtWidgets.QLabel(self.bund1_compare_side_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_73.sizePolicy().hasHeightForWidth())
        self.label_73.setSizePolicy(sizePolicy)
        self.label_73.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.label_73.setFont(font)
        self.label_73.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_73.setWordWrap(True)
        self.label_73.setObjectName("label_73")
        self.verticalLayout_61.addWidget(self.label_73)
        self.frame_73 = QtWidgets.QFrame(self.bund1_compare_side_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_73.sizePolicy().hasHeightForWidth())
        self.frame_73.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.frame_73.setFont(font)
        self.frame_73.setStyleSheet("QPushButton{\n"
"    color: rgb(77, 77, 77);\n"
"    border: 0.5px solid rgb(191, 191, 191);\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"}")
        self.frame_73.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.verticalLayout_84 = QtWidgets.QVBoxLayout(self.frame_73)
        self.verticalLayout_84.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_84.setSpacing(20)
        self.verticalLayout_84.setObjectName("verticalLayout_84")
        self.b1compare_btn = QtWidgets.QPushButton(self.frame_73)
        self.b1compare_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.b1compare_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1compare_btn.setObjectName("b1compare_btn")
        self.verticalLayout_84.addWidget(self.b1compare_btn)
        self.b2compare_btn = QtWidgets.QPushButton(self.frame_73)
        self.b2compare_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.b2compare_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2compare_btn.setObjectName("b2compare_btn")
        self.verticalLayout_84.addWidget(self.b2compare_btn)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_84.addItem(spacerItem18)
        self.frame_89 = QtWidgets.QFrame(self.frame_73)
        self.frame_89.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89.setObjectName("frame_89")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout(self.frame_89)
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_71.setSpacing(10)
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.ket_arahb12 = QtWidgets.QPushButton(self.frame_89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ket_arahb12.sizePolicy().hasHeightForWidth())
        self.ket_arahb12.setSizePolicy(sizePolicy)
        self.ket_arahb12.setMinimumSize(QtCore.QSize(50, 0))
        self.ket_arahb12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ket_arahb12.setStyleSheet("QPushButton{\n"
"    border: 0.5px solid rgb(77, 77, 77);\n"
"    border-radius: 7px;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #ecf0f1;\n"
"    color: r#4d4d4d;\n"
"}")
        self.ket_arahb12.setObjectName("ket_arahb12")
        self.horizontalLayout_71.addWidget(self.ket_arahb12)
        self.clear_compare12 = QtWidgets.QPushButton(self.frame_89)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_compare12.sizePolicy().hasHeightForWidth())
        self.clear_compare12.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.clear_compare12.setFont(font)
        self.clear_compare12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_compare12.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: #303f9f;\n"
"    border: 0px;\n"
"    color: #ffffff;\n"
"    border-radius: 4px;\n"
"    padding-top:7px;\n"
"    padding-bottom:7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(46, 19, 84);\n"
"}")
        self.clear_compare12.setIcon(icon8)
        self.clear_compare12.setObjectName("clear_compare12")
        self.horizontalLayout_71.addWidget(self.clear_compare12)
        self.verticalLayout_84.addWidget(self.frame_89)
        self.verticalLayout_61.addWidget(self.frame_73)
        self.horizontalLayout_58.addWidget(self.bund1_compare_side_15)
        self.compare_tabWidget.addTab(self.compareb12, "")
        self.verticalLayout_60.addWidget(self.compare_tabWidget)
        self.pages_widget.addWidget(self.compare_page)
        self.help_page = QtWidgets.QWidget()
        self.help_page.setObjectName("help_page")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.help_page)
        self.verticalLayout_63.setContentsMargins(0, 15, 0, 0)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.label_5 = QtWidgets.QLabel(self.help_page)
        self.label_5.setMinimumSize(QtCore.QSize(0, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"    padding-left: 20px;\n"
"    padding-right:20px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_63.addWidget(self.label_5)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.help_page)
        self.scrollArea_3.setStyleSheet("QScrollBar:vertical {\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"    width: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    border: 0px solid #ffffff;\n"
"    border-radius:15px;\n"
"    background-color: rgb(153, 153, 153);\n"
"}")
        self.scrollArea_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1078, 5488))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_68.setSpacing(20)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.frame_78 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_78.setMinimumSize(QtCore.QSize(0, 500))
        self.frame_78.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.horizontalLayout_62 = QtWidgets.QHBoxLayout(self.frame_78)
        self.horizontalLayout_62.setObjectName("horizontalLayout_62")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem19)
        self.frame_86 = QtWidgets.QFrame(self.frame_78)
        self.frame_86.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_86.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_86.setObjectName("frame_86")
        self.verticalLayout_69 = QtWidgets.QVBoxLayout(self.frame_86)
        self.verticalLayout_69.setSpacing(20)
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_69.addItem(spacerItem20)
        self.bund_pakMunir = QtWidgets.QLabel(self.frame_86)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bund_pakMunir.sizePolicy().hasHeightForWidth())
        self.bund_pakMunir.setSizePolicy(sizePolicy)
        self.bund_pakMunir.setMaximumSize(QtCore.QSize(426, 240))
        self.bund_pakMunir.setStyleSheet("")
        self.bund_pakMunir.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bund_pakMunir.setText("")
        self.bund_pakMunir.setPixmap(QtGui.QPixmap("images/bund_pakmunir.png"))
        self.bund_pakMunir.setScaledContents(False)
        self.bund_pakMunir.setObjectName("bund_pakMunir")
        self.verticalLayout_69.addWidget(self.bund_pakMunir)
        self.label_79 = QtWidgets.QLabel(self.frame_86)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setMinimumSize(QtCore.QSize(0, 150))
        self.label_79.setMaximumSize(QtCore.QSize(426, 16777215))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_79.setFont(font)
        self.label_79.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_79.setWordWrap(True)
        self.label_79.setObjectName("label_79")
        self.verticalLayout_69.addWidget(self.label_79)
        self.horizontalLayout_62.addWidget(self.frame_86)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem21)
        self.frame_85 = QtWidgets.QFrame(self.frame_78)
        self.frame_85.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_85.setObjectName("frame_85")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.frame_85)
        self.verticalLayout_70.setSpacing(20)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_70.addItem(spacerItem22)
        self.gif_said = QtWidgets.QLabel(self.frame_85)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gif_said.sizePolicy().hasHeightForWidth())
        self.gif_said.setSizePolicy(sizePolicy)
        self.gif_said.setMaximumSize(QtCore.QSize(426, 240))
        self.gif_said.setText("")
        self.gif_said.setPixmap(QtGui.QPixmap("images/bund_said.png"))
        self.gif_said.setObjectName("gif_said")
        self.verticalLayout_70.addWidget(self.gif_said)
        self.gif_said_2 = QtWidgets.QLabel(self.frame_85)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gif_said_2.sizePolicy().hasHeightForWidth())
        self.gif_said_2.setSizePolicy(sizePolicy)
        self.gif_said_2.setMinimumSize(QtCore.QSize(0, 150))
        self.gif_said_2.setMaximumSize(QtCore.QSize(426, 240))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(16)
        self.gif_said_2.setFont(font)
        self.gif_said_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gif_said_2.setWordWrap(True)
        self.gif_said_2.setObjectName("gif_said_2")
        self.verticalLayout_70.addWidget(self.gif_said_2)
        self.horizontalLayout_62.addWidget(self.frame_85)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_62.addItem(spacerItem23)
        self.verticalLayout_68.addWidget(self.frame_78)
        self.frame_81 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_81.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_81.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.horizontalLayout_63 = QtWidgets.QHBoxLayout(self.frame_81)
        self.horizontalLayout_63.setObjectName("horizontalLayout_63")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem24)
        self.label_80 = QtWidgets.QLabel(self.frame_81)
        self.label_80.setMinimumSize(QtCore.QSize(320, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setWordWrap(True)
        self.label_80.setObjectName("label_80")
        self.horizontalLayout_63.addWidget(self.label_80)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem25)
        self.label_81 = QtWidgets.QLabel(self.frame_81)
        self.label_81.setMinimumSize(QtCore.QSize(640, 0))
        self.label_81.setText("")
        self.label_81.setPixmap(QtGui.QPixmap("images/ket_arah.png"))
        self.label_81.setObjectName("label_81")
        self.horizontalLayout_63.addWidget(self.label_81)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_63.addItem(spacerItem26)
        self.verticalLayout_68.addWidget(self.frame_81)
        self.frame_79 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_79.setMinimumSize(QtCore.QSize(0, 850))
        self.frame_79.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_79.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout(self.frame_79)
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem27)
        self.gif_help_nada = QtWidgets.QLabel(self.frame_79)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gif_help_nada.sizePolicy().hasHeightForWidth())
        self.gif_help_nada.setSizePolicy(sizePolicy)
        self.gif_help_nada.setMinimumSize(QtCore.QSize(500, 500))
        self.gif_help_nada.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gif_help_nada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gif_help_nada.setText("")
        self.gif_help_nada.setObjectName("gif_help_nada")
        self.horizontalLayout_64.addWidget(self.gif_help_nada)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem28)
        self.label_82 = QtWidgets.QLabel(self.frame_79)
        self.label_82.setMinimumSize(QtCore.QSize(440, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_82.setFont(font)
        self.label_82.setWordWrap(True)
        self.label_82.setObjectName("label_82")
        self.horizontalLayout_64.addWidget(self.label_82)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_64.addItem(spacerItem29)
        self.verticalLayout_68.addWidget(self.frame_79)
        self.frame_80 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_80.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_80.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_80.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout(self.frame_80)
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem30)
        self.label_83 = QtWidgets.QLabel(self.frame_80)
        self.label_83.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_83.setFont(font)
        self.label_83.setWordWrap(True)
        self.label_83.setObjectName("label_83")
        self.horizontalLayout_65.addWidget(self.label_83)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem31)
        self.label_84 = QtWidgets.QLabel(self.frame_80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy)
        self.label_84.setMinimumSize(QtCore.QSize(500, 462))
        self.label_84.setText("")
        self.label_84.setPixmap(QtGui.QPixmap("images/help_bund_polar.png"))
        self.label_84.setObjectName("label_84")
        self.horizontalLayout_65.addWidget(self.label_84)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem32)
        self.verticalLayout_68.addWidget(self.frame_80)
        self.frame_82 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_82.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_82.setStyleSheet("background-color: rgb(48, 63, 159);")
        self.frame_82.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_82.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_82.setObjectName("frame_82")
        self.horizontalLayout_66 = QtWidgets.QHBoxLayout(self.frame_82)
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem33)
        self.gif_helpkontur = QtWidgets.QLabel(self.frame_82)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gif_helpkontur.sizePolicy().hasHeightForWidth())
        self.gif_helpkontur.setSizePolicy(sizePolicy)
        self.gif_helpkontur.setMinimumSize(QtCore.QSize(600, 556))
        self.gif_helpkontur.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gif_helpkontur.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gif_helpkontur.setText("")
        self.gif_helpkontur.setObjectName("gif_helpkontur")
        self.horizontalLayout_66.addWidget(self.gif_helpkontur)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem34)
        self.label_85 = QtWidgets.QLabel(self.frame_82)
        self.label_85.setMinimumSize(QtCore.QSize(371, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_85.setWordWrap(True)
        self.label_85.setObjectName("label_85")
        self.horizontalLayout_66.addWidget(self.label_85)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem35)
        self.verticalLayout_68.addWidget(self.frame_82)
        self.frame_83 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_83.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_83.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_83.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.horizontalLayout_67 = QtWidgets.QHBoxLayout(self.frame_83)
        self.horizontalLayout_67.setObjectName("horizontalLayout_67")
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem36)
        self.label_86 = QtWidgets.QLabel(self.frame_83)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy)
        self.label_86.setMinimumSize(QtCore.QSize(236, 592))
        self.label_86.setText("")
        self.label_86.setPixmap(QtGui.QPixmap("images/colorbar_help.png"))
        self.label_86.setObjectName("label_86")
        self.horizontalLayout_67.addWidget(self.label_86)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem37)
        self.label_87 = QtWidgets.QLabel(self.frame_83)
        self.label_87.setMinimumSize(QtCore.QSize(0, 0))
        self.label_87.setMaximumSize(QtCore.QSize(541, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_87.setFont(font)
        self.label_87.setWordWrap(True)
        self.label_87.setObjectName("label_87")
        self.horizontalLayout_67.addWidget(self.label_87)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_67.addItem(spacerItem38)
        self.verticalLayout_68.addWidget(self.frame_83)
        self.frame_84 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_84.setMinimumSize(QtCore.QSize(0, 800))
        self.frame_84.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_84.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_84.setObjectName("frame_84")
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout(self.frame_84)
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem39)
        self.label_89 = QtWidgets.QLabel(self.frame_84)
        self.label_89.setMinimumSize(QtCore.QSize(521, 0))
        self.label_89.setMaximumSize(QtCore.QSize(521, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_89.setFont(font)
        self.label_89.setWordWrap(True)
        self.label_89.setObjectName("label_89")
        self.horizontalLayout_68.addWidget(self.label_89)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem40)
        self.label_88 = QtWidgets.QLabel(self.frame_84)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_88.sizePolicy().hasHeightForWidth())
        self.label_88.setSizePolicy(sizePolicy)
        self.label_88.setMinimumSize(QtCore.QSize(450, 450))
        self.label_88.setText("")
        self.label_88.setPixmap(QtGui.QPixmap("images/nada_where.png"))
        self.label_88.setObjectName("label_88")
        self.horizontalLayout_68.addWidget(self.label_88)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_68.addItem(spacerItem41)
        self.verticalLayout_68.addWidget(self.frame_84)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_63.addWidget(self.scrollArea_3)
        self.pages_widget.addWidget(self.help_page)
        self.verticalLayout_2.addWidget(self.pages_widget)
        self.horizontalLayout.addWidget(self.main_view)
        mainWindow.setCentralWidget(self.mainLayout)

        self.retranslateUi(mainWindow)
        self.pages_widget.setCurrentIndex(0)
        self.stackedWidget_bund1.setCurrentIndex(0)
        self.b1senar1_tabWidget.setCurrentIndex(0)
        self.b1senar2_tabWidget.setCurrentIndex(0)
        self.b1senar3_tabWidget.setCurrentIndex(0)
        self.b1senar4_tabWidget.setCurrentIndex(0)
        self.stackedWidget_bund2.setCurrentIndex(0)
        self.b2senar1_tabWidget.setCurrentIndex(0)
        self.b2senar2_tabWidget.setCurrentIndex(0)
        self.b2senar3_tabWidget.setCurrentIndex(0)
        self.b2senar4_tabWidget.setCurrentIndex(0)
        self.b2senar5_tabWidget.setCurrentIndex(0)
        self.b2senar6_tabWidget.setCurrentIndex(0)
        self.b2senar7_tabWidget.setCurrentIndex(0)
        self.b2senar8_tabWidget.setCurrentIndex(0)
        self.compare_tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Bundengan Directivity Visualizer"))
        self.beranda_button.setText(_translate("mainWindow", "Beranda"))
        self.bund1_button.setText(_translate("mainWindow", "Bundengan #1"))
        self.bund2_button.setText(_translate("mainWindow", "Bundengan #2"))
        self.compare_button.setText(_translate("mainWindow", "Bandingkan"))
        self.help_button.setText(_translate("mainWindow", "Bantuan"))
        self.about_button.setText(_translate("mainWindow", "Tentang"))
        self.label_4.setText(_translate("mainWindow", "<h1>Halo Penggemar Bundengan!</h1>\n"
"<p>Saat ini bundengan semakin terancam punah. Apa yang bisa kita lakukan ya?<p>"))
        self.label_67.setText(_translate("mainWindow", "<h2>Bundengan perlu dipentaskan!</h2><br>\n"
"\n"
"Meski begitu, pementasan bundengan belum maksimal karena penonton tidak mendapatkan bunyi musik yang memuaskan ketika bundengan dipentaskan di tempat umum seperti di atas panggung.<br><br>\n"
"\n"
"Tim Akustika Musik UGM hendak merancang solusi pementasan bundengan yang lebih baik. Sebelum solusi dibuat, para insinyur dan para musisi bundengan perlu tahu bagaimana sebaran bunyi bundengan. Apakah betul bahwa kualitas bunyi pada posisi penonton kurang baik?<br><br>\n"
"\n"
"Temukan jawabannya melalui program ini!\n"
""))
        self.label_2.setText(_translate("mainWindow", "<h1>Bundengan Pertama</h1>\n"
"<p>Bundengan ini memiliki empat buah senar. Lihat kualitas masing-masing nada tiap senar melalui tombol berikut!<p>"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://youtu.be/CXSUhsh_W4c\"><span style=\" font-size:15pt; text-decoration: underline; color:#303f9f;\">Klik di sini untuk menyaksikan penampilan Pak Munir dan Pak Bohori!</span></a></p></body></html>"))
        self.label_71.setText(_translate("mainWindow", "Pak Munir dan Pak Bohori saat melakukan perekaman untuk mendeteksi kualitas bunyi bundengan di Fakultas Teknik UGM"))
        self.b1s1_button.setText(_translate("mainWindow", "Senar 1"))
        self.b1s2_button.setText(_translate("mainWindow", "Senar 2"))
        self.b1s3_button.setText(_translate("mainWindow", "Senar 3"))
        self.b1s4_button.setText(_translate("mainWindow", "Senar 4"))
        self.title_b1s.setText(_translate("mainWindow", "<h2>Bundengan Pak Munir dan Pak Bohori</h2>"))
        self.label_7.setText(_translate("mainWindow", "SENAR 1"))
        self.label_6.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 1</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b1senar1_tabWidget.setTabText(self.b1senar1_tabWidget.indexOf(self.b1senar1_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_9.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b1s1n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (235 Hz)"))
        self.b1s1n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (469 Hz)"))
        self.b1s1n3_cekbox.setText(_translate("mainWindow", "Nada Ketiga (609 Hz)"))
        self.b1s1n4_cekbox.setText(_translate("mainWindow", "Nada Keempat (1207 Hz)"))
        self.b1s1_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b1s1_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b1senar1_tabWidget.setTabText(self.b1senar1_tabWidget.indexOf(self.b1senar1_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_2.setText(_translate("mainWindow", "<h2>Bundengan Pak Munir dan Pak Bohori</h2>"))
        self.label_11.setText(_translate("mainWindow", "SENAR 2"))
        self.label_12.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 2</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b1senar2_tabWidget.setTabText(self.b1senar2_tabWidget.indexOf(self.b1senar2_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_14.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b1s2n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (181,6 Hz)"))
        self.b1s2n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (375 Hz)"))
        self.b1s2_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b1s2_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b1senar2_tabWidget.setTabText(self.b1senar2_tabWidget.indexOf(self.b1senar1_polar_2), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_3.setText(_translate("mainWindow", "<h2>Bundengan Pak Munir dan Pak Bohori</h2>"))
        self.label_20.setText(_translate("mainWindow", "SENAR 3"))
        self.label_16.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 3</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b1senar3_tabWidget.setTabText(self.b1senar3_tabWidget.indexOf(self.b1senar3_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_18.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b1s3n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (99,6 Hz)"))
        self.b1s3n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (199,2 Hz)"))
        self.b1s3_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b1s3_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b1senar3_tabWidget.setTabText(self.b1senar3_tabWidget.indexOf(self.b1senar1_polar_3), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_4.setText(_translate("mainWindow", "<h2>Bundengan Pak Munir dan Pak Bohori</h2>"))
        self.label_25.setText(_translate("mainWindow", "SENAR 4"))
        self.label_21.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 4</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b1senar4_tabWidget.setTabText(self.b1senar4_tabWidget.indexOf(self.b1senar4_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_23.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b1s4n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (70,3 Hz)"))
        self.b1s4n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (146,4 Hz)"))
        self.b1s4_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b1s4_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b1senar4_tabWidget.setTabText(self.b1senar4_tabWidget.indexOf(self.b1senar1_polar_4), _translate("mainWindow", "Nada Bundengan"))
        self.label.setText(_translate("mainWindow", "<h1>Bundengan Kedua</h1>\n"
"\n"
"<p>Bundengan ini memiliki delapan buah senar. Lihat kualitas masing-masing nada dari tiap senar melalui tombol berikut!<p>"))
        self.textBrowser_2.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://youtu.be/opn-5tgOb_c\"><span style=\" font-size:15pt; text-decoration: underline; color:#303f9f;\">Klik di sini untuk menyaksikan penampilan Mas Sa\'id! </span></a></p></body></html>"))
        self.label_76.setText(_translate("mainWindow", "Mas Sa\'id saat melakukan perekaman untuk mendeteksi kualitas bunyi bundengan di Fakultas Teknik UGM"))
        self.b2s1_button.setText(_translate("mainWindow", "Senar 1"))
        self.b2s2_button.setText(_translate("mainWindow", "Senar 2"))
        self.b2s3_button.setText(_translate("mainWindow", "Senar 3"))
        self.b2s4_button.setText(_translate("mainWindow", "Senar 4"))
        self.b2s5_button.setText(_translate("mainWindow", "Senar 5"))
        self.b2s6_button.setText(_translate("mainWindow", "Senar 6"))
        self.b2s7_button.setText(_translate("mainWindow", "Senar 7"))
        self.b2s8_button.setText(_translate("mainWindow", "Senar 8"))
        self.title_b1s_5.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_26.setText(_translate("mainWindow", "SENAR 1"))
        self.label_27.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 1</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar1_tabWidget.setTabText(self.b2senar1_tabWidget.indexOf(self.b2senar1_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_29.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s1n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (339,8 Hz)"))
        self.b2s1n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (644,5 Hz)"))
        self.b2s1_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s1_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar1_tabWidget.setTabText(self.b2senar1_tabWidget.indexOf(self.b2senar1_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_6.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_31.setText(_translate("mainWindow", "SENAR 2"))
        self.label_32.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 2</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar2_tabWidget.setTabText(self.b2senar2_tabWidget.indexOf(self.b2senar2_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_34.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s2n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (304,6 Hz)"))
        self.b2s2n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (603,5 Hz)"))
        self.b2s2_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s2_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar2_tabWidget.setTabText(self.b2senar2_tabWidget.indexOf(self.b2senar2_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_7.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_36.setText(_translate("mainWindow", "SENAR 3"))
        self.label_37.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 3</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar3_tabWidget.setTabText(self.b2senar3_tabWidget.indexOf(self.b2senar3_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_39.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s3n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (287,1 Hz)"))
        self.b2s3n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (603,5 Hz)"))
        self.b2s3n3_cekbox.setText(_translate("mainWindow", "Nada Ketiga (1078,1 Hz)"))
        self.b2s3n4_cekbox.setText(_translate("mainWindow", "Nada Keempat (1212,9 Hz)"))
        self.b2s3_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s3_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar3_tabWidget.setTabText(self.b2senar3_tabWidget.indexOf(self.b2senar3_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_8.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_41.setText(_translate("mainWindow", "SENAR 4"))
        self.label_42.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 4</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar4_tabWidget.setTabText(self.b2senar4_tabWidget.indexOf(self.b2senar4_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_44.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s4n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (228,5 Hz)"))
        self.b2s4n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (451,2 Hz)"))
        self.b2s4n3_cekbox.setText(_translate("mainWindow", "Nada Kedua (1306,4 Hz)"))
        self.b2s4_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s4_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar4_tabWidget.setTabText(self.b2senar4_tabWidget.indexOf(self.b2senar4_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_10.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_55.setText(_translate("mainWindow", "SENAR 5"))
        self.label_51.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 5</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar5_tabWidget.setTabText(self.b2senar5_tabWidget.indexOf(self.b2senar5_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_53.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s5n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (210,9 Hz)"))
        self.b2s5n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (568,3 Hz)"))
        self.b2s5_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s5_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar5_tabWidget.setTabText(self.b2senar5_tabWidget.indexOf(self.b2senar5_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_9.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_50.setText(_translate("mainWindow", "SENAR 6"))
        self.label_46.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 6</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar6_tabWidget.setTabText(self.b2senar6_tabWidget.indexOf(self.b2senar6_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_48.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s6n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (170 Hz)"))
        self.b2s6n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (334 Hz)"))
        self.b2s6n3_cekbox.setText(_translate("mainWindow", "Nada Ketiga (527,3 Hz)"))
        self.b2s6n4_cekbox.setText(_translate("mainWindow", "Nada Keempat (1702,2 Hz)"))
        self.b2s6_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s6_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar6_tabWidget.setTabText(self.b2senar6_tabWidget.indexOf(self.b2senar6_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_11.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_60.setText(_translate("mainWindow", "SENAR 7"))
        self.label_56.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 7</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar7_tabWidget.setTabText(self.b2senar7_tabWidget.indexOf(self.b2senar7_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_58.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s7n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (117,2 Hz)"))
        self.b2s7n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (240,2 Hz)"))
        self.b2s7_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s7_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar7_tabWidget.setTabText(self.b2senar7_tabWidget.indexOf(self.b2senar7_polar), _translate("mainWindow", "Nada Bundengan"))
        self.title_b1s_12.setText(_translate("mainWindow", "<h2>Bundengan Mas Sa\'id</h2>"))
        self.label_65.setText(_translate("mainWindow", "SENAR 8"))
        self.label_61.setText(_translate("mainWindow", "<h2>Hasil rekaman senar 8</h2><br>\n"
"Silakan arahkan kursor lalu lihat nilai x dan y pada pojok kanan bawah grafik. <br><br>\n"
"Nilai x berarti frekuensi bunyi dan y adalah arah bunyi. Semakin terang warna artinya bunyinya semakin keras/kuat."))
        self.b2senar8_tabWidget.setTabText(self.b2senar8_tabWidget.indexOf(self.b2senar8_measure), _translate("mainWindow", "Hasil Pengukuran"))
        self.label_63.setText(_translate("mainWindow", "<h2>Lihat kualitas nada.</h2>\n"
"PILIH FREKUENSI NADA"))
        self.b2s8n1_cekbox.setText(_translate("mainWindow", "Nada Pertama (99,6 Hz)"))
        self.b2s8n2_cekbox.setText(_translate("mainWindow", "Nada Kedua (205 Hz)"))
        self.b2s8_applyBtn.setText(_translate("mainWindow", "Lihat"))
        self.b2s8_peakBtn.setText(_translate("mainWindow", "Dari mana nada ini?"))
        self.b2senar8_tabWidget.setTabText(self.b2senar8_tabWidget.indexOf(self.b2senar8_polar), _translate("mainWindow", "Nada Bundengan"))
        self.label_3.setText(_translate("mainWindow", "<h1>Mari bandingkan kualitas nada antar senar bundengan!</h1>\n"
"Pada menu ini anda dapat membandingkan sebaran bunyi dari nada antar senar serta bahkan antar bundengan."))
        self.label_66.setText(_translate("mainWindow", "<h3>Lihat kualitas nada dari senar yang berbeda.</h3>\n"
"PILIH SENAR"))
        self.compareb1s1.setText(_translate("mainWindow", "Senar 1"))
        self.compareb1s2.setText(_translate("mainWindow", "Senar 2"))
        self.compareb1s3.setText(_translate("mainWindow", "Senar 3"))
        self.compareb1s4.setText(_translate("mainWindow", "Senar 4"))
        self.ket_arahb1.setToolTip(_translate("mainWindow", "Di mana posisi bundengan?"))
        self.ket_arahb1.setText(_translate("mainWindow", "i"))
        self.clear_compare1_btn.setText(_translate("mainWindow", "Bersihkan"))
        self.compare_tabWidget.setTabText(self.compare_tabWidget.indexOf(self.compareb1), _translate("mainWindow", "Bundengan 1"))
        self.label_72.setText(_translate("mainWindow", "<h3>Lihat kualitas nada dari senar yang berbeda.</h3>\n"
"PILIH SENAR"))
        self.compareb2s1.setText(_translate("mainWindow", "Senar 1"))
        self.compareb2s2.setText(_translate("mainWindow", "Senar 2"))
        self.compareb2s3.setText(_translate("mainWindow", "Senar 3"))
        self.compareb2s4.setText(_translate("mainWindow", "Senar 4"))
        self.compareb2s5.setText(_translate("mainWindow", "Senar 5"))
        self.compareb2s6.setText(_translate("mainWindow", "Senar 6"))
        self.compareb2s7.setText(_translate("mainWindow", "Senar 7"))
        self.compareb2s8.setText(_translate("mainWindow", "Senar 8"))
        self.ket_arahb2.setToolTip(_translate("mainWindow", "Di mana posisi bundengan?"))
        self.ket_arahb2.setText(_translate("mainWindow", "i"))
        self.clear_compare2_btn.setText(_translate("mainWindow", "Bersihkan"))
        self.compare_tabWidget.setTabText(self.compare_tabWidget.indexOf(self.compareb2), _translate("mainWindow", "Bundengan 2"))
        self.label_73.setText(_translate("mainWindow", "<h3>Lihat perbedaan kualitas nada antar bundengan.</h3>\n"
"PILIH BUNDENGAN"))
        self.b1compare_btn.setText(_translate("mainWindow", "Bundengan #1 (Pak Munir)"))
        self.b2compare_btn.setText(_translate("mainWindow", "Bundengan #2 (Mas Said)"))
        self.ket_arahb12.setToolTip(_translate("mainWindow", "Di mana posisi bundengan?"))
        self.ket_arahb12.setText(_translate("mainWindow", "i"))
        self.clear_compare12.setText(_translate("mainWindow", "Bersihkan"))
        self.compare_tabWidget.setTabText(self.compare_tabWidget.indexOf(self.compareb12), _translate("mainWindow", "Bandingkan Keduanya"))
        self.label_5.setText(_translate("mainWindow", "<h2>Apakah anda kesulitan memahami cara kerja program ini?</h2>\n"
"Penjelasan berikut akan menjawab semua kesulitan anda."))
        self.label_79.setText(_translate("mainWindow", "Bundengan #1 dimainkan oleh <b><span style=\"color: #303f9f\">Pak Munir</span></b>. Bundengan ini terdiri dari <b><span style=\"color: #303f9f\">empat buah senar</span></b> dengan gaya musik tradisional."))
        self.gif_said_2.setText(_translate("mainWindow", "Bundengan #2 dimainkan oleh <b><span style=\"color: #303f9f\">Mas Sa\'id</span></b>. Bundengan ini terdiri dari <b><span style=\"color: #303f9f\">delapan buah senar</span></b> dengan gaya musik lebih modern."))
        self.label_80.setText(_translate("mainWindow", "<p style=\"line-height:4em;\">Bunyi bundengan direkam dengan mikrofon yang disusun seperti pada gambar di samping.</p>"))
        self.label_82.setText(_translate("mainWindow", "<h1>Program ini telah otomatis mendeteksi nada bundengan.</h1><br>\n"
"Cukup pilih nada yang tersedia lalu lihat bagaimana sebaran bunyinya."))
        self.label_83.setText(_translate("mainWindow", "<h2><b><span style=\"color: #303f9f\">Semakin luas</span></b> polanya maka <br><b><span style=\"color: #303f9f\">semakin keras dan merata</span></b> bunyinya!</h2><br>\n"
"Dari gambar di samping dapat dilihat bahwa pola biru lebih luas dibanding pola oranye. Ini berarti Nada 1 cenderung lebih merata dan kuat bunyinya.<br><br>\n"
"Nada 4 selain lebih lemah bunyinya (pola lebih sempit), pola yang terbentuk juga tidak simetris yang berarti bunyinya tidak begitu merata."))
        self.label_85.setText(_translate("mainWindow", "<h2>Seluruh data terekam (termasuk dengan derau/<i>noise</i>) ditampilkan dalam bentuk peta warna.</h2><br>\n"
"Gambar di samping adalah data bunyi yang terekam. Pada grafik tersebut terdapat nada bundengan di antara bunyi lingkungan sekitar yang ikut terekam.<br><br>\n"
"Arahkan kursor ke tempat yang diinginkan. Apabila x = 5 dan y = 180º artinya posisi kursor berada pada bunyi frekuensi 5 Hz yang mengarah pada 180º."))
        self.label_87.setText(_translate("mainWindow", " <h2><b><span style=\"color: #303f9f\">Semakin terang</span></b> warnanya, artinya bunyi tersebut  <b><span style=\"color: #303f9f\">semakin keras</span></b>.</h1><br><br><br>\n"
"<h3>Cara membayangkan seberapa keras bunyi:</h2><br>\n"
"\n"
"Pilih satu warna dari gambar disamping, kemudian bayangkan keras bunyi pada warna tersebut seperti <b><span style=\"color: #303f9f\">satu buah lonceng</span></b> yang berbunyi. Dengan demikian, satu tingkat warna lebih terang (di atasnya) keras bunyinya seperti <b><span style=\"color: #303f9f\">dua lonceng</span></b> yang berbunyi.\n"
"\n"
""))
        self.label_89.setText(_translate("mainWindow", "<h2>Lantas, yang mana nada bundengan?</h2><br><br>\n"
"\n"
"Warna pada grafik yang terlihat seperti \'ombak\' dan semakin ke kanan semakin gelap adalah <i>noise</i> atau bunyi dari lingkungan yang ikut terekam.<br><br>\n"
"<b><span style=\"color: #303f9f\">Garis terang</span></b> yang tegak dan berada di tengah-tengah pola \'ombak\' adalah <b><span style=\"color: #303f9f\">nada bundengan</span></b>.<br><br><br>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

