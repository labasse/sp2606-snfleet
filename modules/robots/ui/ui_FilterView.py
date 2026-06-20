# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilterView.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_FilterView(object):
    def setupUi(self, FilterView):
        if not FilterView.objectName():
            FilterView.setObjectName(u"FilterView")
        FilterView.resize(730, 82)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FilterView.sizePolicy().hasHeightForWidth())
        FilterView.setSizePolicy(sizePolicy)
        FilterView.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(FilterView)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(FilterView)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(FilterView)
        self.groupBox1.setObjectName(u"groupBox1")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.groupBox1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.spinBox = QSpinBox(self.groupBox1)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.pushButton = QPushButton(self.groupBox1)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_3.addWidget(self.groupBox1)


        self.retranslateUi(FilterView)

        QMetaObject.connectSlotsByName(FilterView)
    # setupUi

    def retranslateUi(self, FilterView):
        FilterView.setWindowTitle(QCoreApplication.translate("FilterView", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("FilterView", u"Quick filters", None))
        self.label.setText(QCoreApplication.translate("FilterView", u"Site:", None))
        self.label_2.setText(QCoreApplication.translate("FilterView", u"Status:", None))
        self.label_3.setText(QCoreApplication.translate("FilterView", u"Search:", None))
        self.groupBox1.setTitle(QCoreApplication.translate("FilterView", u"Data update", None))
        self.label_4.setText(QCoreApplication.translate("FilterView", u"Refresh every:", None))
        self.pushButton.setText(QCoreApplication.translate("FilterView", u"Refresh", None))
    # retranslateUi

