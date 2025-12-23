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

        self._img_scene = QGraphicsScene(self)
        self.ui.grvMain.setScene(self._img_scene)
        self.ui.grvMain.mousePosChanged.connect(self.on_grv_mouse_pos)
        
        self.ui.mniFileOpen.triggered.connect(self._on_mniFileOpen_triggered)

        self._pixitem = None

    # region Events
    def on_grv_mouse_pos(self, x, y):
        self._lblPos.setText(f"{x}, {y}")
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

      # resize scene theo ảnh
      self._img_scene.setSceneRect(pix.rect())
    # endregion