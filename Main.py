"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-15
-- Points! --
"""

import sys
from PySide import QtGui, QtCore
from View import View
from Controller import Controller


class Main(QtGui.QApplication):
    """
    The App for starting the Program
    """
    def __init__(self):
        """
        Konstruktor
        """
        super().__init__(sys.argv)
        self.Controller = Controller()

        while self.Controller.view.isVisible():
            self.Controller.update()
            self.processEvents()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())


