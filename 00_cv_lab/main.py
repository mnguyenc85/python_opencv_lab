import sys
from PySide6.QtWidgets import QApplication
from view.wndMain import CWndMain

def main():
  app = QApplication(sys.argv)
  win = CWndMain()
  win.show()
  sys.exit(app.exec())

if __name__ == "__main__":
    main()