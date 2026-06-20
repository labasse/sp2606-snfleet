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
        DetailView.resize(284, 206)
        self.formLayout = QFormLayout(DetailView)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DetailView)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.robotIDLabel = QLabel(DetailView)
        self.robotIDLabel.setObjectName(u"robotIDLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.robotIDLabel)

        self.label_3 = QLabel(DetailView)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.displayNameLabel = QLabel(DetailView)
        self.displayNameLabel.setObjectName(u"displayNameLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.displayNameLabel)

        self.label_5 = QLabel(DetailView)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.modelLabel = QLabel(DetailView)
        self.modelLabel.setObjectName(u"modelLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.modelLabel)

        self.label_6 = QLabel(DetailView)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.siteIDLabel = QLabel(DetailView)
        self.siteIDLabel.setObjectName(u"siteIDLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.siteIDLabel)

        self.label_7 = QLabel(DetailView)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.statusLabel = QLabel(DetailView)
        self.statusLabel.setObjectName(u"statusLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.statusLabel)

        self.label_8 = QLabel(DetailView)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.createdAtLabel = QLabel(DetailView)
        self.createdAtLabel.setObjectName(u"createdAtLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.createdAtLabel)

        self.label_9 = QLabel(DetailView)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.lastEventTimeLabel = QLabel(DetailView)
        self.lastEventTimeLabel.setObjectName(u"lastEventTimeLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lastEventTimeLabel)


        self.retranslateUi(DetailView)

        QMetaObject.connectSlotsByName(DetailView)
    # setupUi

    def retranslateUi(self, DetailView):
        DetailView.setWindowTitle(QCoreApplication.translate("DetailView", u"Form", None))
        self.label.setText(QCoreApplication.translate("DetailView", u"ID:", None))
        self.robotIDLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("DetailView", u"Display name:", None))
        self.displayNameLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("DetailView", u"Model:", None))
        self.modelLabel.setText("")
        self.label_6.setText(QCoreApplication.translate("DetailView", u"Site:", None))
        self.siteIDLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("DetailView", u"Status:", None))
        self.statusLabel.setText("")
        self.label_8.setText(QCoreApplication.translate("DetailView", u"Created at:", None))
        self.createdAtLabel.setText("")
        self.label_9.setText(QCoreApplication.translate("DetailView", u"Last event:", None))
        self.lastEventTimeLabel.setText("")
    # retranslateUi

