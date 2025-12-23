import sys
from PySide6.QtWidgets import QApplication
from view.wndImageTools import CWndImageTools

def main():

  app = QApplication(sys.argv)
  win = CWndImageTools()
  win.show()
  sys.exit(app.exec())

if __name__ == "__main__":
    main()