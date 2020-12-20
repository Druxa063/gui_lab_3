from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

from Dollar import Dollar
from Oil import Oil
from Ruble import Ruble

top = 400
left = 400
width = 400
height = 250

# 1 баррель нефти рублях
OIL_RUB = 3796

# 1 баррель нефти в долларах
OIL_DOLLAR = 52

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Генератор курса валют на торговом рынке"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setFixedSize(width, height)
        
        validator = QDoubleValidator(self)
        locale = QLocale("en")
        validator.setLocale(locale)

        self.oilLabel = QLabel(self)
        self.rubleLabel = QLabel(self)
        self.dollarLabel = QLabel(self)
        
        # Конфигурация для нефти
        self.oil = Oil(1)
        self.oilLabel.setText("Нефть:")
        self.oilLabel.move(30,20)
        self.oilLabel.resize(200, 30)
        self.oilLabel.setFont(QFont('Arial', 20))

        self.oilEdit = QLineEdit(self)
        self.oilEdit.move(150, 20)
        self.oilEdit.resize(200, 30)
        self.oilEdit.setText(self.oil.getOil())
        self.oilEdit.setFont(QFont('Arial', 10))
        self.oilEdit.setValidator(validator)

        # Конфигурация для рубля
        self.ruble = Ruble(OIL_RUB)
        self.ruble.setRuble.connect(self.ruble.update)
        self.rubleLabel.setText("Рубль:")
        self.rubleLabel.move(30,80)
        self.rubleLabel.setFont(QFont('Arial', 20))

        self.rubleInput = QLineEdit(self)
        self.rubleInput.move(150,80)
        self.rubleInput.resize(200, 30)
        self.rubleInput.setFont(QFont('Arial', 10))
        self.rubleInput.setText(self.ruble.getRuble())
        self.rubleInput.setReadOnly(True)

        # Конфигурация для доллара
        self.dollar = Dollar(OIL_DOLLAR)
        self.dollar.setDollar.connect(self.dollar.update)
        
        self.dollarLabel.setText("Доллар:")
        self.dollarLabel.move(30,140)
        self.dollarLabel.setFont(QFont('Arial', 20))

        self.dollarInput = QLineEdit(self)
        self.dollarInput.move(150, 140)
        self.dollarInput.resize(200, 30)
        self.dollarInput.setText(self.dollar.getDollar())
        self.dollarInput.setFont(QFont('Arial', 10))
        self.dollarInput.setReadOnly(True)

        self.btn1 = QPushButton("Анализ", self)
        self.btn1.move(150,200)
        self.btn1.setFont(QFont('Arial', 10))
        self.btn1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        newOil = float(self.oilEdit.text())
        self.oil.setOil(self.oilEdit.text())
        
        self.dollar.setDollar.emit(newOil * OIL_DOLLAR)
        self.dollarInput.setText(self.dollar.getDollar())

        self.ruble.setRuble.emit(newOil * OIL_RUB)
        self.rubleInput.setText(self.ruble.getRuble())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()