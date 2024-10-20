# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowAFfvUt.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import src.res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(388, 580)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(388, 580))
        MainWindow.setMaximumSize(QSize(388, 580))
        MainWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget { \n"
"	background-image: url(:/images/images/bg_2.jpg);\n"
"}\n"
"\n"
"QWidget { \n"
"	color: white;\n"
"	font: 11pt \"Roboto\";\n"
"\n"
"}\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #00d2ff, stop:1 #3a47d5)\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy)
        self.frame_main.setMinimumSize(QSize(370, 557))
        self.frame_main.setMaximumSize(QSize(370, 557))
        self.frame_main.setStyleSheet(u"QFrame#frame_main, QFrame#frame_stats, QFrame#frame_6dof, QFrame#frame_springs {\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame_main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setStyleSheet(u"font-size: 12pt;")

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_6dof = QFrame(self.frame_main)
        self.frame_6dof.setObjectName(u"frame_6dof")
        sizePolicy.setHeightForWidth(self.frame_6dof.sizePolicy().hasHeightForWidth())
        self.frame_6dof.setSizePolicy(sizePolicy)
        self.frame_6dof.setMaximumSize(QSize(16777215, 150))
        self.frame_6dof.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.frame_6dof)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.frame_6dof)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_set_time = QLineEdit(self.frame)
        self.lineEdit_set_time.setObjectName(u"lineEdit_set_time")
        self.lineEdit_set_time.setMaximumSize(QSize(140, 30))
        self.lineEdit_set_time.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit_set_time.setStyleSheet(u"QLineEdit\n"
" {\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"	background-color: rgba(255, 255, 255, 80);\n"
"	border: none;\n"
"	border-radius: 5px; \n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_set_time)

        self.btn_set_time = QPushButton(self.frame)
        self.btn_set_time.setObjectName(u"btn_set_time")
        sizePolicy.setHeightForWidth(self.btn_set_time.sizePolicy().hasHeightForWidth())
        self.btn_set_time.setSizePolicy(sizePolicy)
        self.btn_set_time.setMinimumSize(QSize(100, 30))
        self.btn_set_time.setMaximumSize(QSize(130, 30))
        self.btn_set_time.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(4, 170, 109, 255);\n"
"	color: white;\n"
"	font-size: 10pt;\n"
"}\n"
"QPushButton::dasabled {\n"
"	background-color: rgba(4, 170, 109, 180);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(4, 160, 98, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(3, 134, 84, 255)\n"
"}")
        self.btn_set_time.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_set_time)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_6dof)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 0)
        self.btn_load6 = QPushButton(self.frame_2)
        self.btn_load6.setObjectName(u"btn_load6")
        self.btn_load6.setMinimumSize(QSize(200, 30))
        self.btn_load6.setMaximumSize(QSize(200, 30))
        self.btn_load6.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.btn_load6.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_load6)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_6dof, 1, 0, 1, 1)

        self.frame_stats = QFrame(self.frame_main)
        self.frame_stats.setObjectName(u"frame_stats")
        self.frame_stats.setMaximumSize(QSize(16777215, 202))
        self.verticalLayout = QVBoxLayout(self.frame_stats)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_4 = QFrame(self.frame_stats)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, 6, 0)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(250, 0))
        self.label_3.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.btn_settings = QToolButton(self.frame_4)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(30, 30))
        self.btn_settings.setMaximumSize(QSize(30, 30))
        self.btn_settings.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_settings.setStyleSheet(u"QToolButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QToolButton::hover {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"QToolButton::pressed {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/images/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.btn_settings)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_stats)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 300))
        self.frame_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(320, 120))
        self.tableWidget.setMaximumSize(QSize(320, 120))
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: transparent;\n"
"	padding-left: 5px;\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 80);\n"
"    border-right: 1px solid rgba(255, 255, 255, 80);\n"
"\n"
"}\n"
"QTableWidget {	\n"
"	border-style: none;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	gridline-color: rgba(255, 255, 255, 80);\n"
"    border-left: 1px solid rgba(255, 255, 255, 80);\n"
"    border-top: 1px solid rgba(255, 255, 255, 80);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: white;\n"
"	gridline-color: white;\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: transparent;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"	background-color: transparent;\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 80);\n"
"    border-right: 1px solid rgba(255, 255, 255, 80);\n"
"	\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(124)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(22)
        self.tableWidget.verticalHeader().setDefaultSectionSize(29)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_stats, 2, 0, 1, 1)

        self.frame_springs = QFrame(self.frame_main)
        self.frame_springs.setObjectName(u"frame_springs")
        self.frame_springs.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_5 = QVBoxLayout(self.frame_springs)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.frame_springs)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, -1, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_springs)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_in_1 = QPushButton(self.frame_7)
        self.btn_in_1.setObjectName(u"btn_in_1")
        self.btn_in_1.setMinimumSize(QSize(150, 30))
        self.btn_in_1.setMaximumSize(QSize(150, 30))
        self.btn_in_1.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.btn_in_1.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_in_1, 0, 0, 1, 1)

        self.btn_in_3 = QPushButton(self.frame_7)
        self.btn_in_3.setObjectName(u"btn_in_3")
        self.btn_in_3.setMinimumSize(QSize(150, 30))
        self.btn_in_3.setMaximumSize(QSize(150, 30))
        self.btn_in_3.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.btn_in_3.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_in_3, 2, 0, 1, 1)

        self.btn_in_2 = QPushButton(self.frame_7)
        self.btn_in_2.setObjectName(u"btn_in_2")
        self.btn_in_2.setMinimumSize(QSize(150, 30))
        self.btn_in_2.setMaximumSize(QSize(150, 30))
        self.btn_in_2.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.btn_in_2.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_in_2, 0, 1, 1, 1)

        self.btn_spring_prc = QPushButton(self.frame_7)
        self.btn_spring_prc.setObjectName(u"btn_spring_prc")
        self.btn_spring_prc.setMinimumSize(QSize(320, 30))
        self.btn_spring_prc.setMaximumSize(QSize(310, 30))
        self.btn_spring_prc.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(4, 170, 109, 255);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton::dasabled {\n"
"	background-color: rgba(4, 170, 109, 180);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(4, 160, 98, 255);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(3, 134, 84, 255)\n"
"}")
        self.btn_spring_prc.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_spring_prc, 4, 0, 1, 1)

        self.btn_in_4 = QPushButton(self.frame_7)
        self.btn_in_4.setObjectName(u"btn_in_4")
        self.btn_in_4.setMinimumSize(QSize(150, 30))
        self.btn_in_4.setMaximumSize(QSize(150, 30))
        self.btn_in_4.setStyleSheet(u"QPushButton {\n"
"	text-align: center;\n"
"    border-radius: 5px;\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	color: white;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(0, 0, 0, 80);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")
        self.btn_in_4.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_in_4, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 2)


        self.verticalLayout_5.addWidget(self.frame_7)


        self.gridLayout.addWidget(self.frame_springs, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DTA v.0.2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DTA (DROP TEST ANALYSIS) version 0.2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Landing, s:", None))
        self.btn_set_time.setText(QCoreApplication.translate("MainWindow", u"Time click", None))
        self.btn_load6.setText(QCoreApplication.translate("MainWindow", u"Load 6DOF XOB", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.btn_settings.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Actual", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nominal", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Vz, m/s", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Vy, m/s", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Rx, deg", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Springs processing", None))
        self.btn_in_1.setText(QCoreApplication.translate("MainWindow", u"Load spring 1", None))
        self.btn_in_3.setText(QCoreApplication.translate("MainWindow", u"Load spring 3", None))
        self.btn_in_2.setText(QCoreApplication.translate("MainWindow", u"Load spring 2", None))
        self.btn_spring_prc.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.btn_in_4.setText(QCoreApplication.translate("MainWindow", u"Load spring 4", None))
    # retranslateUi

