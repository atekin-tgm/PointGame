"""
@author: TEKIN Abdurrahim Burak
@date: 2016-12-15
-- Points! --
"""

from View import View
from multiprocessing import *
from random import randint
import time

class Controller(Process):
    """
    Controller class using multiprocessing
    """
    def __init__(self):
        """
        Konstruktor
        """
        super().__init__()

        self.view = View()
        self.view.show()

        self.view.buttonNew.clicked.connect(self.newPoint)
        self.view.buttonNew.clicked.connect(self.view.update)
        self.view.buttonDel.clicked.connect(self.delPoint)
        self.view.buttonDel.clicked.connect(self.view.update)

    def newPoint(self):
        """
        Method for new Point
        :return: None
        """
        x = randint(1, 499)
        y = randint(1, 299)

        point = Point(x, y)
        point.start()

        self.view.pointlist.append(point)

    def delPoint(self):
        """
        Method for deleting a Point -> Deletes the last entry (last Point)
        :return: None
        """
        if len(self.view.pointlist) > 0:
            self.view.pointlist[len(self.view.pointlist) - 1].join()
            self.view.pointlist.pop()

    def update(self):
        """
        Method for repainting -> repaints constantly
        :return: None
        """
        self.view.repaint()

class Point(Process):
    """
    Point class using multiprocessing
    """
    def __init__(self, x, y):
        """
        Konstruktor of Point class
        :param x: x Value of Point
        :param y: y Value of Point
        """
        super().__init__()
        self.x = Value("i", x)
        self.y = Value("i", y)

        self.directionx = randint(0, 1)
        self.directiony = randint(0, 1)

        self.speed = randint(5, 10)

        self.closing = Value("b", False)

    def join(self, timeout=None):
        self.closing.value = True

    #Got help from Wellner... I was absent while the class discussed how this could work,
    #so he showed me how it could work
    def run(self):
        """
        Run method -> Makes the Balls bounce against the Walls and change their directions
        :return: None
        """
        while not self.closing.value:

            if self.directionx == 0:
                self.x.value += 1 * self.speed
            else:
                self.x.value += -1 * self.speed

            if self.directiony == 0:
                self.y.value += 1 * self.speed
            else:
                self.y.value += -1 * self.speed

            if self.x.value >= View.width - (5 + View.radius):
                self.directionx = 1

            if self.x.value <= 0 + (View.radius):
                self.directionx = 0

            if self.y.value >= View.heigth - (5 + View.radius):
                self.directiony = 1

            if self.y.value <= 0 + (View.radius):
                self.directiony = 0

            time.sleep(0.05)

