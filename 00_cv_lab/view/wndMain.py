from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide6.QtGui import QCloseEvent, QStandardItemModel, QStandardItem
from PySide6.QtCore import QSize, Qt

from ui.ui_wndMain import Ui_wndMain
from utils.pipeline_factory import create_loadimage_node
from utils.utils_qt6 import thumbnail_from_numpy

class CWndMain(QMainWindow):
  def __init__(self):
    super().__init__()

    self.ui = Ui_wndMain()
    self.ui.setupUi(self)    

    self._tv_model = QStandardItemModel()
    self._init_values()

    self.ui.mniFileOpen.triggered.connect(self._on_mniFileOpen)
    self.ui.tvPipelines.clicked.connect(self._on_tv_clicked)

  def _init_values(self):
    tv = self.ui.tvPipelines
    tv.setIconSize(QSize(64, 64))
    tv.setHeaderHidden(True)
    tv.setModel(self._tv_model)

  # region Events
  def closeEvent(self, event: QCloseEvent):
    pass

  def _on_tv_clicked(self, index):
    item = self._tv_model.itemFromIndex(index)
    print(item.data(Qt.ItemDataRole.UserRole))
  # endregion

  # region Menu
  def _on_mniFileOpen(self):
    file_path, _ = QFileDialog.getOpenFileName(
      self,
      "Open image file",
      "",
      "Images (*.png *.jpg *.bmp);;All files (*.*)"
    )

    if file_path:
      self._add_load_image_node(file_path)
  # endregion

  # region Button handlers
  # endregion

  def _add_load_image_node(self, file_path):
    ndata = create_loadimage_node(file_path)
    if ndata:
      icon = thumbnail_from_numpy(ndata.output)

      root = self._tv_model.invisibleRootItem()

      node = QStandardItem("Origin")
      node.setEditable(False)
      node.setIcon(icon)
      node.setData(ndata.id, Qt.ItemDataRole.UserRole)

      root.appendRow(node)

    