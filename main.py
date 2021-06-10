import sys
from PyQt5.QtWidgets import QApplication
from pyui import RequestUI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RequestUI()
    sys.exit(app.exec_())