import sys
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QTimer, QThread, QEvent, QEventLoop, Signal)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QMainWindow, QPushButton, QSizePolicy,
                               QSpacerItem, QToolButton, QVBoxLayout, QWidget, QDialog, QFileDialog,
                               QMessageBox, QTableWidgetItem, QProgressDialog, QProgressBar, QStyleOptionProgressBar,
                               QMenuBar, QMenu, QToolBar)

import velocity as vel

from src.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.cid = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_load6.clicked.connect(self.btn_load6_pressed)
        self.ui.btn_set_time.clicked.connect(self.btn_set_time_pressed)
        self.ui.btn_settings.setDisabled(True)


        self.ui.btn_in_1.setDisabled(True)
        self.ui.btn_in_2.setDisabled(True)
        self.ui.btn_in_3.setDisabled(True)
        self.ui.btn_in_4.setDisabled(True)
        self.ui.btn_spring_prc.setDisabled(True)

        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def btn_set_time_pressed(self):
        print('mpl_connecting callback')
        self.cid = plt.connect('button_press_event', self.onclick)

    def btn_load6_pressed(self):
        file_name, filter = QFileDialog.getOpenFileName(parent=self.sender(),
                                                        caption='Открыть XOB файл...',
                                                        dir='..',
                                                        filter='*.xob', )
        vel.load_cog(file_name)

    def onclick(self, event):
        if event.button is MouseButton.LEFT:
            self.ix, iy = event.xdata, event.ydata
            print(f'x = {self.ix}, y = {iy}')
            self.get_data()
        if event.button is MouseButton.RIGHT:
            print('disconnecting callback')
            plt.disconnect(self.cid)

    def get_data(self):
        res_data = vel.update_res_data(self.ix)
        time_file = res_data[0]
        str_time = str(f"{time_file:.4f}")
        vy = str(f"{abs(res_data[1]):.2f}")
        vz = str(f"{abs(res_data[2]):.2f}")
        rx = str(f"{abs(res_data[3]):.2f}")
        self.ui.lineEdit_set_time.setText(str_time)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(vz))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(vy))
        self.ui.tableWidget.setItem(1, 2, QTableWidgetItem(rx))

    def closeEvent(self, event):
        for i in plt.get_fignums():
            plt.close(i)

        super(MainWindow, self).closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
