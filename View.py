"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-15
-- Points! --
"""

from PySide.QtGui import *
from PySide.QtCore import *
from random import randint


class View(QWidget):
    """
    The View Class of the Game
    """
    heigth = 500
    width = 500
    radius = randint(0, 10)


    def __init__(self):
        """
        Konstruktor
        """
        super(View, self).__init__()

        self.pointUI()

        self.pointlist = []

    def pointUI(self):
        """
        Ui Method for painting the Points
        :return: None
        """
        self.heigth = View.heigth
        self.width = View.width

        self.setWindowTitle("PointGame")
        self.setObjectName("Widget")

        self.setStyleSheet("QWidget#Widget {background-color: white}")

        self.painter = QPainter()

        self.buttonNew = QPushButton("New Point", self)
        self.buttonDel = QPushButton("Delete Point", self)

        #self.setStyleSheet("")

        self.buttonNew.resize(200, 50)
        self.buttonDel.resize(200, 50)

        self.buttonNew.move(self.width/100 * 5, self.heigth/100 * 85)
        self.buttonDel.move(self.width/100 * 55, self.heigth/100 * 85)

        self.buttonNew.show()
        self.buttonDel.show()

        self.setFixedSize(500, 500)

        self.show()

    def paintEvent(self, event):
        """
        paintEvent for painting the Points
        :param event:
        :return:
        """
        #painter.drawEllipse(100, 100, 300, 300)

        self.painter.begin(self)

        pen = QPen()

        pen.setWidth(5)

        self.painter.setPen(pen)

        for p in self.pointlist:
            self.painter.setPen(QColor(p.c[0], p.c[1], p.c[2]))
            self.painter.drawEllipse(p.x.value, p.y.value, p.radius.value, p.radius.value)

        self.update()
        self.painter.end()

    def closeEvent(self, event):
        """
        closeEvent for closing the event
        :param event:
        :return:
        """
        for p in self.pointlist:
            p.join()

        event.accept()







