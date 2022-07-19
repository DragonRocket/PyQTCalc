from cmath import inf
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        self.operating = False
        self.result = 0
        super(MainWindow, self).__init__()
        uic.loadUi('calc.ui', self)

        self.btneq.clicked.connect(self.onbtneq)
        self.btnac.clicked.connect(self.onbtnac)
        self.btnbck.clicked.connect(self.onbtnbck)
        self.btnpnt.clicked.connect(self.onbtnpnt)
        self.btnplus.clicked.connect(self.onbtnplus)
        self.btnminus.clicked.connect(self.onbtnminus)
        self.btnmul.clicked.connect(self.onbtnmul)
        self.btndiv.clicked.connect(self.onbtndiv)
        self.btn0.clicked.connect(self.onbtn0)
        self.btn1.clicked.connect(self.onbtn1)
        self.btn2.clicked.connect(self.onbtn2)
        self.btn3.clicked.connect(self.onbtn3)
        self.btn4.clicked.connect(self.onbtn4)
        self.btn5.clicked.connect(self.onbtn5)
        self.btn6.clicked.connect(self.onbtn6)
        self.btn7.clicked.connect(self.onbtn7)
        self.btn8.clicked.connect(self.onbtn8)
        self.btn9.clicked.connect(self.onbtn9)
		
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_0:
            self.onbtn0()
        elif event.key() == Qt.Key_1:
            self.onbtn1()
        elif event.key() == Qt.Key_2:
            self.onbtn2()
        elif event.key() == Qt.Key_3:
            self.onbtn3()
        elif event.key() == Qt.Key_4:
            self.onbtn4()
        elif event.key() == Qt.Key_5:
            self.onbtn5()
        elif event.key() == Qt.Key_6:
            self.onbtn6()
        elif event.key() == Qt.Key_7:
            self.onbtn7()
        elif event.key() == Qt.Key_8:
            self.onbtn8()
        elif event.key() == Qt.Key_9:
            self.onbtn9()
        elif event.key() == Qt.Key_Period:
            self.onbtnpnt()
        elif event.key() == Qt.Key_Plus:
            self.onOpBtn('+')
        elif event.key() == Qt.Key_Minus:
            self.onOpBtn('-')
        elif event.key() == Qt.Key_Asterisk:
            self.onOpBtn('*')
        elif event.key() == Qt.Key_Slash:
            self.onOpBtn('/')
        elif event.key() == Qt.Key_Enter:
            self.onbtneq()
        elif event.key() == Qt.Key_Escape:
            self.onbtnac()
        elif event.key() == Qt.Key_Backspace:
            self.onbtnbck()

    def update_disp(self):
        if self.result == inf:
            self.disp.setText(str(inf))
        else:
            if abs(self.result) - abs(int(self.result)) <= 0:
                self.disp.setText(str(int(self.result)))
            else:
                self.disp.setText(str(self.result))

    def onbtnac(self):
        self.disp.setText('0')
        self.scnddisp.setText('')
        self.result = 0
        self.operating = False

    def onbtnbck(self):
        if not self.operating:

            noback = True
            if len(self.scnddisp.text()) > 0:
                if (self.scnddisp.text()[-1] == '='):
                    noback = False

            if noback:
                if len(self.disp.text()) == 1:
                    self.disp.setText('0')
                elif len(self.disp.text()) > 0:
                    self.disp.setText(self.disp.text()[:-1])

    def onbtneq(self):
        if not self.operating:
            prevop = ''
            if len(self.scnddisp.text()):
                prevop = self.scnddisp.text()[-1]

            if len(self.scnddisp.text()) == 0:
                self.result = float(self.disp.text())
            if prevop == '+':
                self.result = self.result + float(self.disp.text())
            elif prevop == '-':
                self.result = self.result - float(self.disp.text())
            elif prevop == '*':
                self.result = self.result * float(self.disp.text())
            elif prevop == '/':
                try:
                    self.result = self.result / float(self.disp.text())
                except ZeroDivisionError:
                    self.result = inf
            
            self.scnddisp.setText(self.scnddisp.text() + ' ' + self.disp.text() + ' =')
            self.update_disp()
    
    def onOpBtn(self, op):
        if self.operating:
            self.scnddisp.setText(self.scnddisp.text()[:-2] + ' ' + op)
        else:
            prevop = op
            if len(self.scnddisp.text()):
                prevop = self.scnddisp.text()[-1]
            self.operating = True

            if len(self.scnddisp.text()) == 0:
                self.result = float(self.disp.text())
            else:
                if prevop == '+':
                    self.result = self.result + float(self.disp.text())
                elif prevop == '-':
                    self.result = self.result - float(self.disp.text())
                elif prevop == '*':
                    self.result = self.result * float(self.disp.text())
                elif prevop == '/':
                    self.result = self.result / float(self.disp.text())

            if self.result == inf:
                self.scnddisp.setText(str(inf))
            else:
                if abs(self.result) - abs(int(self.result)) == 0:
                    self.scnddisp.setText(str(int(self.result)) + ' ' + op)
                else:
                    self.scnddisp.setText(str(self.result) + ' ' + op)
                
            self.update_disp()

    def onbtnplus(self):
        self.onOpBtn('+')

    def onbtnminus(self):
        self.onOpBtn('-')
        
    def onbtnmul(self):
        self.onOpBtn('*')
        
    def onbtndiv(self):
        self.onOpBtn('/')

    def onbtnpnt(self):
        if len(self.scnddisp.text()) and self.scnddisp.text()[-1] == '=':
            self.disp.setText('0.')
            self.scnddisp.setText('')
            self.operating = False
        else:
            if self.disp.text().find('.') == -1:
                self.disp.setText(self.disp.text() + '.')

    def onbtn0(self):
        if self.operating:
            self.disp.setText('')
            self.operating = False
        
        if self.disp.text() != '0':
            self.disp.setText(self.disp.text() + '0')
    
    def onNonZeroBtn(self, digit):
        if (len(self.scnddisp.text()) and self.scnddisp.text()[-1] == '='):
            self.scnddisp.setText('')
        if self.operating:
            self.disp.setText('')
            self.operating = False

        if self.disp.text() == '0':
            self.disp.setText(digit)
        else:
            self.disp.setText(self.disp.text() + digit)

    def onbtn1(self):
        self.onNonZeroBtn('1')
    
    def onbtn2(self):
        self.onNonZeroBtn('2')
    
    def onbtn3(self):
        self.onNonZeroBtn('3')
        
    def onbtn4(self):
        self.onNonZeroBtn('4')
        
    def onbtn5(self):
        self.onNonZeroBtn('5')
        
    def onbtn6(self):
        self.onNonZeroBtn('6')
        
    def onbtn7(self):
        self.onNonZeroBtn('7')
        
    def onbtn8(self):
        self.onNonZeroBtn('8')
        
    def onbtn9(self):
        self.onNonZeroBtn('9')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
