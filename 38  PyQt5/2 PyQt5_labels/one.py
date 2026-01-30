# pyqt5 introduction
# pip install PyQt5

import sys    
from PyQt5.QtWidgets import QApplication ,QMainWindow,QLabel
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700,300,300,300)    #(x,y,width,height)

        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",20))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:blue;")

def main():
    app=QApplication(sys.argv)                    #sys.argv is a list in Python that contains the command-line arguments passed to your script when you run it from the terminal/command prompt.
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()

