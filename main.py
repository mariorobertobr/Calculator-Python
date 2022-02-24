import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('calculadora.ui', self)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        ##self.setStyleSheet("opacity: 70; background-color: rgba(0, 0, 0, 0.5); border: 10px; border-radius: 500px;")
        ##frameless

        self.setWindowOpacity(0.95)
        self.setAttribute(Qt.WA_TranslucentBackground)
        radius = 150
        self.setStyleSheet(
            """
            background:rgb(255, 255, 255);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
        #make a clic for the button pushButton4

        #create a funtion to handle the display
        global value_1, value_2, operator, simbol, formatted_value, formatted_value_2
        formatted_value = 0
        formatted_value_2 = 0
        simbol = "+"
        value_1 = []
        value_2 = []
        operator = 1
        self.display = self.lineEdit
        self.display.setText("0")
        self.display.setAlignment(Qt.AlignRight)
        #set the display to be blocked
        self.display.setReadOnly(True)

        self.btn_0.clicked.connect(lambda: self.handle_button(0))
        self.btn_1.clicked.connect(lambda: self.handle_button(1))
        self.btn_2.clicked.connect(lambda: self.handle_button(2))
        self.btn_3.clicked.connect(lambda: self.handle_button(3))
        self.btn_4.clicked.connect(lambda: self.handle_button(4))
        self.btn_5.clicked.connect(lambda: self.handle_button(5))
        self.btn_6.clicked.connect(lambda: self.handle_button(6))
        self.btn_7.clicked.connect(lambda: self.handle_button(7))
        self.btn_8.clicked.connect(lambda: self.handle_button(8))
        self.btn_9.clicked.connect(lambda: self.handle_button(9))
        self.btn_dot.clicked.connect(lambda: self.handle_button("."))
        self.btn_plus.clicked.connect(lambda: self.handle_button("+"))
        self.btn_minus.clicked.connect(lambda: self.handle_button("-"))
        self.btn_multiply.clicked.connect(lambda: self.handle_button("*"))
        self.btn_divide.clicked.connect(lambda: self.handle_button("/"))
        self.btn_equal.clicked.connect(lambda: self.handle_button("="))
        self.btn_clear.clicked.connect(lambda: self.handle_button("C"))

        self.show()

    #handle the basic operations
    #aqui ele pega os valores do botão e passa pra função que se chama display text, ela serve pra joga os numeros na tela e verificar as coisas
    #o operador serve pra eu saber se to mexendo com o primeiro numero ou o segundo numero então sempre que alguém clica no + ou _ ou divisão ou multiplicaç
    #ele aumenta o operador e com isso eu sei se eu incremento o value_1 ou o value_2
    #primeira entrada de valor
    def handle_button(self, text):
        if text == "C":
            self.display.setText("0")
            value_1.clear()
            value_2.clear()
            operator = 1
        else:
            self.display_text(text)

    #handles the display displayin the list in line edit
    #recebe o valor do handle button e joga na tela se for numero se for operador ele incrementa e se for = ele faz a operação

    def display_text(self, text):

        if text == "/" or text == "*" or text == "+" or text == "-":
            global operator
            operator = operator + 1
            global simbol
            global formatted_value, formatted_value_2
            simbol = str(text)

        if text == "=":
            if simbol == "+":
                result = formatted_value + formatted_value_2
                self.display.setText(str(result))
            elif simbol == "-":
                result = formatted_value - formatted_value_2
                self.display.setText(str(result))
            elif simbol == "*":
                result = formatted_value * formatted_value_2
                self.display.setText(str(result))
            elif simbol == "/":
                result = formatted_value / formatted_value_2
                self.display.setText(str(result))
            else:
                self.display.setText("0")

        elif operator % 2 and type(text) == int:
            value_1.append(text)

            #trnasform the display value in an int
            formatted_value = int("".join(str(x) for x in value_1))
            self.display.setText(str(formatted_value))

        elif type(text) == int:
            value_2.append(text)
            # formatted_value_2 = int(value_2.join(int(x) for x in value_2))
            formatted_value_2 = int("".join(str(x) for x in value_2))
            self.display.setText(str(formatted_value_2))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
