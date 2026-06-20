# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetailView.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_DetailView(object):
    def setupUi(self, DetailView):
        if not DetailView.objectName():
            DetailView.setObjectName(u"DetailView")
        DetailView.resize(288, 214)
        self.formLayout = QFormLayout(DetailView)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DetailView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(DetailView)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_2)

        self.label_3 = QLabel(DetailView)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(DetailView)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.label_4)

        self.label_5 = QLabel(DetailView)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.label_10 = QLabel(DetailView)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.label_10)

        self.label_6 = QLabel(DetailView)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.label_11 = QLabel(DetailView)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.label_11)

        self.label_7 = QLabel(DetailView)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_12 = QLabel(DetailView)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.label_12)

        self.label_8 = QLabel(DetailView)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_13 = QLabel(DetailView)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.label_13)

        self.label_9 = QLabel(DetailView)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_14 = QLabel(DetailView)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.label_14)


        self.retranslateUi(DetailView)

        QMetaObject.connectSlotsByName(DetailView)
    # setupUi

    def retranslateUi(self, DetailView):
        DetailView.setWindowTitle(QCoreApplication.translate("DetailView", u"Form", None))
        self.label.setText(QCoreApplication.translate("DetailView", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("DetailView", u"Display name:", None))
        self.label_4.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("DetailView", u"Model:", None))
        self.label_10.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("DetailView", u"Site:", None))
        self.label_11.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("DetailView", u"Status:", None))
        self.label_12.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("DetailView", u"Created at:", None))
        self.label_13.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("DetailView", u"Last event:", None))
        self.label_14.setText(QCoreApplication.translate("DetailView", u"TextLabel", None))
    # retranslateUi

