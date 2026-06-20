# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QSplitter, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from modules.robots.views import (DetailView, FilterView, RobotListView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filterView = FilterView(self.centralwidget)
        self.filterView.setObjectName(u"filterView")
        self.filterView.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout.addWidget(self.filterView)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.robotListView = RobotListView(self.splitter)
        self.robotListView.setObjectName(u"robotListView")
        self.splitter.addWidget(self.robotListView)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.robotDetailTab = QWidget()
        self.robotDetailTab.setObjectName(u"robotDetailTab")
        self.horizontalLayout = QHBoxLayout(self.robotDetailTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = DetailView(self.robotDetailTab)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout.addWidget(self.widget)

        self.frame = QFrame(self.robotDetailTab)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: SteelBlue")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)

        self.horizontalLayout.addWidget(self.frame)

        self.tabWidget.addTab(self.robotDetailTab, "")
        self.eventsTab = QWidget()
        self.eventsTab.setObjectName(u"eventsTab")
        self.tabWidget.addTab(self.eventsTab, "")
        self.alertsTab = QWidget()
        self.alertsTab.setObjectName(u"alertsTab")
        self.tabWidget.addTab(self.alertsTab, "")
        self.splitter.addWidget(self.tabWidget)

        self.verticalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 857, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        MainWindow.setWindowFilePath("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.robotDetailTab), QCoreApplication.translate("MainWindow", u"General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eventsTab), QCoreApplication.translate("MainWindow", u"Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.alertsTab), QCoreApplication.translate("MainWindow", u"Alerts", None))
    # retranslateUi

