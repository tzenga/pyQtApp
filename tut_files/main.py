import sys
from window import Window
from PyQt4 import QtGui, QtCore

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
