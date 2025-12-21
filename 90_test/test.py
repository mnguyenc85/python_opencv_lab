import sys
from PySide6.QtWidgets import (
    QApplication, QTreeView, QWidget, QVBoxLayout
)
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt6 TreeView with Image")

        layout = QVBoxLayout(self)

        self.tree = QTreeView()
        self.tree.setHeaderHidden(False)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Name", "Info"])

        # Root item
        root = QStandardItem(QIcon("icons/folder.png"), "Root")
        root.setEditable(False)

        # Child item 1
        child1 = QStandardItem(QIcon("icons/image.png"), "Image File")
        child1_info = QStandardItem("PNG")

        # Child item 2
        child2 = QStandardItem(QIcon("icons/file.png"), "Text File")
        child2_info = QStandardItem("TXT")

        root.appendRow([child1, child1_info])
        root.appendRow([child2, child2_info])

        model.appendRow([root, QStandardItem("Folder")])

        self.tree.setModel(model)
        self.tree.expandAll()

        layout.addWidget(self.tree)


app = QApplication(sys.argv)
w = MainWindow()
w.resize(400, 300)
w.show()
sys.exit(app.exec())
