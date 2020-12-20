import sys
from PyQt5.QtCore import pyqtSignal, QObject


class Ruble(QObject):
    setRuble = pyqtSignal(int)

    def __init__(self, ruble):
        super().__init__()
        self.ruble = ruble

    def update(self, value):
        self.ruble = value

    def getRuble(self):
        return str(self.ruble)