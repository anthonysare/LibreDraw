from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys
from printGCODE import *
from printSVG import *
from convert import *
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("LibreDraw")
        self.setWindowIcon(QIcon("icon.jpg"))

        printSVGBtn = QPushButton("Print SVG", self)
        printSVGBtn.clicked.connect(printSVGfile)
        printSVGBtn.move(100, 300)

        printGCODEbtn = QPushButton("Print GCODE", self)
        printGCODEbtn.clicked.connect(printGCODEfile)
        printGCODEbtn.move(500,300)

        convertSVGBtn = QPushButton("Convert SVG", self)
        convertSVGBtn.clicked.connect(convertSVG)
        convertSVGBtn.move(100, 100)

        homeSVGBtn = QPushButton("Home", self)
        homeSVGBtn.clicked.connect(home)
        homeSVGBtn.move(500, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)



def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    main()