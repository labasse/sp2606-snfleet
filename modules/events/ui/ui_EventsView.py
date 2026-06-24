# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EventsView.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_EventsView(object):
    def setupUi(self, EventsView):
        if not EventsView.objectName():
            EventsView.setObjectName(u"EventsView")
        EventsView.resize(573, 300)
        self.verticalLayout = QVBoxLayout(EventsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.eventsFilterLayout = QHBoxLayout()
        self.eventsFilterLayout.setObjectName(u"eventsFilterLayout")
        self.startDateLabel = QLabel(EventsView)
        self.startDateLabel.setObjectName(u"startDateLabel")

        self.eventsFilterLayout.addWidget(self.startDateLabel)

        self.start_date_edit = QLineEdit(EventsView)
        self.start_date_edit.setObjectName(u"start_date_edit")

        self.eventsFilterLayout.addWidget(self.start_date_edit)

        self.endDateLabel = QLabel(EventsView)
        self.endDateLabel.setObjectName(u"endDateLabel")

        self.eventsFilterLayout.addWidget(self.endDateLabel)

        self.end_date_edit = QLineEdit(EventsView)
        self.end_date_edit.setObjectName(u"end_date_edit")

        self.eventsFilterLayout.addWidget(self.end_date_edit)

        self.eventTypeLabel = QLabel(EventsView)
        self.eventTypeLabel.setObjectName(u"eventTypeLabel")

        self.eventsFilterLayout.addWidget(self.eventTypeLabel)

        self.event_type_filter = QLineEdit(EventsView)
        self.event_type_filter.setObjectName(u"event_type_filter")

        self.eventsFilterLayout.addWidget(self.event_type_filter)

        self.severityLabel = QLabel(EventsView)
        self.severityLabel.setObjectName(u"severityLabel")

        self.eventsFilterLayout.addWidget(self.severityLabel)

        self.severity_filter = QComboBox(EventsView)
        self.severity_filter.addItem("")
        self.severity_filter.addItem("")
        self.severity_filter.addItem("")
        self.severity_filter.addItem("")
        self.severity_filter.addItem("")
        self.severity_filter.addItem("")
        self.severity_filter.setObjectName(u"severity_filter")

        self.eventsFilterLayout.addWidget(self.severity_filter)

        self.searchEventLabel = QLabel(EventsView)
        self.searchEventLabel.setObjectName(u"searchEventLabel")

        self.eventsFilterLayout.addWidget(self.searchEventLabel)

        self.search_event_edit = QLineEdit(EventsView)
        self.search_event_edit.setObjectName(u"search_event_edit")

        self.eventsFilterLayout.addWidget(self.search_event_edit)

        self.apply_filters_btn = QPushButton(EventsView)
        self.apply_filters_btn.setObjectName(u"apply_filters_btn")

        self.eventsFilterLayout.addWidget(self.apply_filters_btn)


        self.verticalLayout.addLayout(self.eventsFilterLayout)

        self.robotIDLabel = QLabel(EventsView)
        self.robotIDLabel.setObjectName(u"robotIDLabel")

        self.verticalLayout.addWidget(self.robotIDLabel)

        self.eventsTree = QTreeWidget(EventsView)
        self.eventsTree.setObjectName(u"eventsTree")
        self.eventsTree.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.eventsTree)


        self.retranslateUi(EventsView)

        QMetaObject.connectSlotsByName(EventsView)
    # setupUi

    def retranslateUi(self, EventsView):
        EventsView.setWindowTitle(QCoreApplication.translate("EventsView", u"Form", None))
        self.startDateLabel.setText(QCoreApplication.translate("EventsView", u"Start:", None))
        self.start_date_edit.setPlaceholderText(QCoreApplication.translate("EventsView", u"YYYY-MM-DD", None))
        self.endDateLabel.setText(QCoreApplication.translate("EventsView", u"End:", None))
        self.end_date_edit.setPlaceholderText(QCoreApplication.translate("EventsView", u"YYYY-MM-DD", None))
        self.eventTypeLabel.setText(QCoreApplication.translate("EventsView", u"Types:", None))
        self.event_type_filter.setPlaceholderText(QCoreApplication.translate("EventsView", u"Comma separated", None))
        self.severityLabel.setText(QCoreApplication.translate("EventsView", u"Severity>=:", None))
        self.severity_filter.setItemText(0, QCoreApplication.translate("EventsView", u"All", None))
        self.severity_filter.setItemText(1, QCoreApplication.translate("EventsView", u"DEBUG", None))
        self.severity_filter.setItemText(2, QCoreApplication.translate("EventsView", u"INFO", None))
        self.severity_filter.setItemText(3, QCoreApplication.translate("EventsView", u"WARNING", None))
        self.severity_filter.setItemText(4, QCoreApplication.translate("EventsView", u"ERROR", None))
        self.severity_filter.setItemText(5, QCoreApplication.translate("EventsView", u"CRITICAL", None))

        self.searchEventLabel.setText(QCoreApplication.translate("EventsView", u"Search:", None))
        self.search_event_edit.setPlaceholderText(QCoreApplication.translate("EventsView", u"Search in message", None))
        self.apply_filters_btn.setText(QCoreApplication.translate("EventsView", u"Apply Filters", None))
        self.robotIDLabel.setText(QCoreApplication.translate("EventsView", u"TextLabel", None))
        ___qtreewidgetitem = self.eventsTree.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("EventsView", u"Acknowledged", None))
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("EventsView", u"Message", None))
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("EventsView", u"Severity", None))
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("EventsView", u"Type", None))
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("EventsView", u"Timestamp", None))
    # retranslateUi

