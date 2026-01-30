# pyqt5 introduction
# pip install PyQt5

import sys    #sys- meaning SYstem Specific paramters and function--this module provides access to some varaiblea used or maintained by the interpreter and to functions that inter act strongly with the interpreter. it is always available
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300,300,300)    #(x,y,width,height)
        self.setWindowIcon(QIcon("nanditha.jpg"))



def main():
    app=QApplication(sys.argv)                    #sys.argv is a list in Python that contains the command-line arguments passed to your script when you run it from the terminal/command prompt.
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

