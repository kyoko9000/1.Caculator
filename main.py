import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from Calculator import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
#tinh toan
        self.uic.Plus_Button.clicked.connect(self.Plus_Equal)
        self.uic.Minus_Button.clicked.connect(self.Minus_Equal)
        self.uic.Multiply_Button.clicked.connect(self.Multiply_Equal)
        self.uic.Divide_Button.clicked.connect(self.Divide_Equal)
    def Divide_Equal(self):
        Addnumber = self.uic.Screen_1.toPlainText()+"/"+self.uic.Screen_2.toPlainText()
        try:
            result = eval(Addnumber)
            self.uic.Screen_3.setText(str(result))
        except:
            self.uic.Screen_3.setText("Error")
    def Multiply_Equal(self):
        Addnumber = self.uic.Screen_1.toPlainText()+"*"+self.uic.Screen_2.toPlainText()
        try:
            result = eval(Addnumber)
            self.uic.Screen_3.setText(str(result))
        except:
            self.uic.Screen_3.setText("Error")
    def Minus_Equal(self):
        Addnumber = self.uic.Screen_1.toPlainText()+"-"+self.uic.Screen_2.toPlainText()
        try:
            result = eval(Addnumber)
            self.uic.Screen_3.setText(str(result))
        except:
            self.uic.Screen_3.setText("Error")
    def Plus_Equal(self):
        Addnumber = self.uic.Screen_1.toPlainText()+"+"+self.uic.Screen_2.toPlainText()
        try:
            result = eval(Addnumber)
            self.uic.Screen_3.setText(str(result))
        except:
            self.uic.Screen_3.setText("Error")

    # chuoi = self.uic.Screen.text()
    # if chuoi[0] != "-":
    #     chuoi = "+" + chuoi
    # else:
    #     chuoi = chuoi
    # y = ""
    # for x in chuoi:
    #     if x == "-":
    #         x = "+"
    #     elif x == "+":
    #         x = "-"
    #     else:
    #         x = x
    #     y = y + x
    #     self.uic.Screen.setText(str(y))
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
