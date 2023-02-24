import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow
sc_si = (680, 480)


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.x, self.y = 0, 0
        self.color = (255, 255, 0)
        self.size = 0
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
        self.cort = 0
        self.pushButton.clicked.connect(self.draw)
        self.coords = list()

    def draw(self):
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.cort = 1
        self.update()

    def paintEvent(self, event):
        if self.cort:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x = random.randint(0, sc_si[0])
            self.y = random.randint(0, sc_si[1])
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
