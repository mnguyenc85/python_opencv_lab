# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wndImageToolsLGmjBI.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)

from controls.ZoomGraphicsView2 import ZoomGraphicsView2

class Ui_wndImageTools(object):
    def setupUi(self, wndImageTools):
        if not wndImageTools.objectName():
            wndImageTools.setObjectName(u"wndImageTools")
        wndImageTools.resize(800, 600)
        self.mniFileOpen = QAction(wndImageTools)
        self.mniFileOpen.setObjectName(u"mniFileOpen")
        self.actionToolbarMask = QAction(wndImageTools)
        self.actionToolbarMask.setObjectName(u"actionToolbarMask")
        self.actionToolbarMask.setCheckable(True)
        self.actionToolbarMask.setChecked(False)
        self.actionToolbarMask.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(wndImageTools)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.grvMain = ZoomGraphicsView2(self.centralwidget)
        self.grvMain.setObjectName(u"grvMain")

        self.horizontalLayout.addWidget(self.grvMain)


        self.verticalLayout.addLayout(self.horizontalLayout)

        wndImageTools.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wndImageTools)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.mnuFile = QMenu(self.menubar)
        self.mnuFile.setObjectName(u"mnuFile")
        wndImageTools.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wndImageTools)
        self.statusbar.setObjectName(u"statusbar")
        wndImageTools.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(wndImageTools)
        self.toolBar.setObjectName(u"toolBar")
        wndImageTools.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.dockWidget = QDockWidget(wndImageTools)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidget.setWidget(self.dockWidgetContents)
        wndImageTools.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.mnuFile.menuAction())
        self.mnuFile.addAction(self.mniFileOpen)
        self.toolBar.addAction(self.actionToolbarMask)

        self.retranslateUi(wndImageTools)

        QMetaObject.connectSlotsByName(wndImageTools)
    # setupUi

    def retranslateUi(self, wndImageTools):
        wndImageTools.setWindowTitle(QCoreApplication.translate("wndImageTools", u"MainWindow", None))
        self.mniFileOpen.setText(QCoreApplication.translate("wndImageTools", u"Open", None))
        self.actionToolbarMask.setText(QCoreApplication.translate("wndImageTools", u"Mask", None))
        self.mnuFile.setTitle(QCoreApplication.translate("wndImageTools", u"File", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("wndImageTools", u"toolBar", None))
    # retranslateUi

