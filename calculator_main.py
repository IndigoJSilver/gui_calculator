import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_main = uic.loadUiType("calculator.ui")[0]

class MainWindow(QDialog, form_main):
    def __init__(self):
        super().__init__()
        self.initUI(),
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.btn_1.clicked.connect(self.button_1)
        self.btn_2.clicked.connect(self.button_2)
        self.btn_3.clicked.connect(self.button_3)
        self.btn_4.clicked.connect(self.button_4)
        self.btn_5.clicked.connect(self.button_5)
        self.btn_6.clicked.connect(self.button_6)
        self.btn_7.clicked.connect(self.button_7)
        self.btn_8.clicked.connect(self.button_8)
        self.btn_9.clicked.connect(self.button_9)
        self.btn_0.clicked.connect(self.button_0)
        self.btn_del.clicked.connect(self.del_num)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_c.clicked.connect(self.clear)

        
    def button_1(self):
        self.number("1")
        
    def button_2(self):
        self.number("2")
        
    def button_3(self):
        self.number("3")
        
    def button_4(self):
        self.number("4")
        
    def button_5(self):
        self.number("5")
        
    def button_6(self):
        self.number("6")
        
    def button_7(self):
        self.number("7")
        
    def button_8(self):
        self.number("8")
        
    def button_9(self):
        self.number("9")
        
    def button_0(self):
        self.number("0")
        
    def number(self, num):
        exist_text = self.lineEdit.text()
        self.lineEdit.setText(exist_text + num)
        
    def del_num(self):
        exist_text = self.lineEdit.text()
        self.lineEdit.setText(exist_text[:-1])
      
    def recentClr(self):
        self.lineEdit.setText("") 
            
    def clear(self):
        self.lineEdit.setText("")
  
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())