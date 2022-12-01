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
        self.btn_c.clicked.connect(self.clear)
        self.btn_ce.clicked.connect(self.recentClr)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_plusMinus.clicked.connect(self.plusMinus)
        self.btn_frac.clicked.connect(self.fraction)
        self.btn_sq.clicked.connect(self.square)                
        self.btn_root.clicked.connect(self.root)
        self.btn_rem.clicked.connect(self.remainder)
        self.btn_multi.clicked.connect(self.multi)
        self.btn_div.clicked.connect(self.divide)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_ans.clicked.connect(self.equal)
        self.btn_minus.clicked.connect(self.minus)
        
        
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
        
    def root(self):
        exist_text = self.lineEdit.text()
        ans = math.sqrt(float(exist_text))
        self.lineEdit.setText(str(ans))

    def square(self):
        exist_text = self.lineEdit.text()
        ans = float(exist_text) * float(exist_text)
        self.lineEdit.setText(str(ans))

    def fraction(self):
        exist_text = self.lineEdit.text()
        ans = 1 / float(exist_text)
        self.lineEdit.setText(str(ans))
        
    def plusMinus(self):
        exist_text = self.lineEdit.text()
        ans = -1 * float(exist_text)
        self.lineEdit.setText(str(ans))
        
    def dot(self):
        exist_text = self.lineEdit.text()
        if "." in self.lineEdit.text()[:]:
            pass
        else:
            self.lineEdit.setText(exist_text + ".")
            
    def remainder(self):
        global math
        math = "%"
        global temp1
        #temp1 = 0
        exist_text = self.lineEdit.text()
        if((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1]) # 연산자 중복 방지   
        temp1 = exist_text[:] # temp1에 처음 입력한 숫자 담기
        self.lineEdit.setText("") # 연산자 입력 시 입력한 숫자 삭제
            
    def divide(self):
        global math
        math = "/"
        global temp1
        #temp1 = 0
        exist_text = self.lineEdit.text()
        if((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1]) # 연산자 중복 방지   
        temp1 = exist_text[:] # temp1에 처음 입력한 숫자 담기
        self.lineEdit.setText("") # 연산자 입력 시 입력한 숫자 삭제

    def minus(self):
        global math
        math = "-"
        global temp1
        #temp1 = 0
        exist_text = self.lineEdit.text()
        if((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1]) # 연산자 중복 방지   
        temp1 = exist_text[:] # temp1에 처음 입력한 숫자 담기
        self.lineEdit.setText("") # 연산자 입력 시 입력한 숫자 삭제

    def multi(self):
        global math
        math = "*"
        global temp1
        #temp1 = 0
        exist_text = self.lineEdit.text()
        if((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1]) # 연산자 중복 방지   
        temp1 = exist_text[:] # temp1에 처음 입력한 숫자 담기
        self.lineEdit.setText("") # 연산자 입력 시 입력한 숫자 삭제

    def plus(self):
        global math
        math = "+"
        global temp1
        #temp1 = 0
        exist_text = self.lineEdit.text()
        if((exist_text[-1] == "+") | (exist_text[-1] == "-") | (exist_text[-1] == "*") | (exist_text[-1] == "/") | (exist_text[-1] == "%")):
            self.lineEdit.setText(exist_text[:-1]) # 연산자 중복 방지
        temp1 = exist_text[:] # temp1에 처음 입력한 숫자 담기
        self.lineEdit.setText("") # 연산자 입력 시 입력한 숫자 삭제
                
    def equal(self):   
        exist_text = self.lineEdit.text()
        global temp2
        temp2 = exist_text[:]

        if math == "+":
            #global temp2
            #temp2 = 0
            ans = float(temp1) + float(temp2)
            self.lineEdit.setText(str(ans))
    
        if math == "-":
            ans = float(temp1) - float(temp2)
            self.lineEdit.setText(str(ans))
        
        if math == "*":
            ans = float(temp1) * float(temp2)
            self.lineEdit.setText(str(ans))
            
        if math == "/":
            ans = float(temp1) / float(temp2)
            self.lineEdit.setText(str(ans))

        if math == "%":
            ans = float(temp1) % float(temp2)
            self.lineEdit.setText(str(ans))
  
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())