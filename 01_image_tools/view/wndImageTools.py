import asyncio, datetime
from ctypes import POINTER, cast, c_ubyte
from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QMessageBox, QLabel
from PySide6.QtGui import QCloseEvent, QPixmap
from PySide6.QtCore import Qt


from ui.ui_wndImageTools import Ui_wndImageTools

class CWndImageTools(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_wndImageTools()
        self.ui.setupUi(self)

        self._lblPos = QLabel("0, 0")
        self.statusBar().addPermanentWidget(self._lblPos)
        self._lblZoom = QLabel("1x")
        self.statusBar().addPermanentWidget(self._lblZoom)

        self._img_scene = QGraphicsScene(self)
        self.ui.grvMain.setScene(self._img_scene)
        self.ui.grvMain.mousePosChanged.connect(self.on_grv_mouse_pos)
        self.ui.grvMain.zoomChanged.connect(self._on_grm_zoom_changed)
        
        self.ui.mniFileOpen.triggered.connect(self._on_mniFileOpen_triggered)

        self.ui.actionToolbarMask.toggled.connect(self._on_toolbar_mark_toggle)

        self._pixitem = None

    # region Events
    # region Main Canvas
    def on_grv_mouse_pos(self, x, y):
        self._lblPos.setText(f"{x}, {y}")
    
    def _on_grm_zoom_changed(self, z):
        self._lblZoom.setText(f"{round(z, 1)}x")
    # endregion

    # region Toolbar
    def _on_toolbar_mark_toggle(self):
        ison = self.ui.actionToolbarMask.isChecked()
        if ison:
            mode = self.ui.grvMain.setMode(1)
            if mode != 1:
                self.ui.actionToolbarMask.setChecked(False)
        else:
            self.ui.grvMain.setMode(0)
        

    # endregion
    # endregion

    # region Menu
    def _on_mniFileOpen_triggered(self):
        file_path, _ = QFileDialog.getOpenFileName(
          self,
          "Open image file",
          "",
          "Images (*.png *.jpg *.bmp);;All files (*.*)"
        )

        if file_path:
          self.load_image(file_path)
    # endregion

    # region Utils

    def load_image(self, img_path: str):
        pix = QPixmap(img_path)
        if pix.isNull():
            print("Load image failed")
            return

        if self._pixitem:
            self._img_scene.removeItem(self._pixitem)
        if not hasattr(self, "pix_item"):
            self._pix_item = QGraphicsPixmapItem()
            self._pix_item.setPixmap(pix)
            self._img_scene.addItem(self._pix_item)

        rect = pix.rect()
        # resize scene theo ảnh
        self._img_scene.setSceneRect(rect)

        self.ui.grvMain.initMark(rect)

    # endregion