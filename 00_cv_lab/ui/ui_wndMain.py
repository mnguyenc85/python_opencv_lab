# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wndMainTObgei.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTreeView, QVBoxLayout, QWidget)

class Ui_wndMain(object):
    def setupUi(self, wndMain):
        if not wndMain.objectName():
            wndMain.setObjectName(u"wndMain")
        wndMain.resize(1366, 768)
        self.mniFileOpen = QAction(wndMain)
        self.mniFileOpen.setObjectName(u"mniFileOpen")
        self.centralwidget = QWidget(wndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.layout000 = QHBoxLayout()
        self.layout000.setObjectName(u"layout000")
        self.layout000.setContentsMargins(3, 3, 3, 3)
        self.tvPipelines = QTreeView(self.centralwidget)
        self.tvPipelines.setObjectName(u"tvPipelines")

        self.layout000.addWidget(self.tvPipelines)

        self.layoutImage = QVBoxLayout()
        self.layoutImage.setObjectName(u"layoutImage")
        self.layoutImage.setContentsMargins(3, 3, 3, 3)

        self.layout000.addLayout(self.layoutImage)

        self.layout000.setStretch(1, 1)

        self.verticalLayout.addLayout(self.layout000)

        wndMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wndMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        wndMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wndMain)
        self.statusbar.setObjectName(u"statusbar")
        wndMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.mniFileOpen)

        self.retranslateUi(wndMain)

        QMetaObject.connectSlotsByName(wndMain)
    # setupUi

    def retranslateUi(self, wndMain):
        wndMain.setWindowTitle(QCoreApplication.translate("wndMain", u"OpenCV GUI Lab", None))
        self.mniFileOpen.setText(QCoreApplication.translate("wndMain", u"Open", None))
        self.menuFile.setTitle(QCoreApplication.translate("wndMain", u"File", None))
    # retranslateUi

