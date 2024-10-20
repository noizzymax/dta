# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tol_dialoggSnffj.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDialog,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import src.res

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(388, 264)
        Dialog.setMinimumSize(QSize(388, 264))
        Dialog.setMaximumSize(QSize(388, 264))
        Dialog.setStyleSheet(u"QDialog\n"
"{\n"
"background-image: url(:/images/images/bg_2.jpg);\n"
"}\n"
"QFrame#frame_btns {\n"
"	background-color: rgba(0, 0, 0, 50);\n"
"	border-radius: 10px;\n"
"}\n"
"QWidget \n"
"{\n"
"color: white;\n"
"font: 11pt \"Roboto\";\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_btns = QFrame(Dialog)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(370, 250))
        self.verticalLayout_3 = QVBoxLayout(self.frame_btns)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_btns)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 40))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 6, 0)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(250, 0))
        self.label_4.setMaximumSize(QSize(250, 16777215))

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_btns)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 205))
        self.frame_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tableWidget_2 = QTableWidget(self.frame_7)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(320, 120))
        self.tableWidget_2.setMaximumSize(QSize(335, 120))
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section {\n"
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
        self.tableWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_2.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget_2.setLineWidth(0)
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setCornerButtonEnabled(False)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(124)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(22)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(29)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_7.addWidget(self.tableWidget_2)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame = QFrame(self.frame_btns)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, 9, -1)
        self.btn_in_1 = QPushButton(self.frame)
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

        self.horizontalLayout.addWidget(self.btn_in_1)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_in_2 = QPushButton(self.frame)
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

        self.horizontalLayout.addWidget(self.btn_in_2)


        self.verticalLayout_3.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.frame_btns)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u043f\u0443\u0441\u043a\u0438", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Upper", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Lower", None));
        ___qtablewidgetitem2 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Vz, m/s", None));
        ___qtablewidgetitem3 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Vy, m/s", None));
        ___qtablewidgetitem4 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Rx, deg", None));
        self.btn_in_1.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.btn_in_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

