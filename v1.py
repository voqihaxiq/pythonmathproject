from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGroupBox

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = QWidget()
        self.main_window.setWindowTitle("Project")
        self.main_window.resize(1000, 800)
        self.main_line = QHBoxLayout()
        main_poloska = QHBoxLayout()
        main_line2 = QHBoxLayout()
        

        #боксы
        GroupBox1 = QGroupBox()
        GroupBox2 = QGroupBox()
        GroupBox3 = QGroupBox()
        GroupBox4 = QGroupBox()
        GroupBox5 = QGroupBox()
        GroupBox6 = QGroupBox()
        GroupBox7 = QGroupBox()

        # NEW CODE

        def PushButton1():
            GroupBox1.show()
            GroupBox2.hide()

        def PushButton2():
            GroupBox2.hide()
            GroupBox3.show()
        #выбор того что нужно
        self.button1 = QPushButton("Калькулятор", self)
        self.button2 = QPushButton("Определение площади", self)
        self.main_line.addWidget(self.button1, alignment=Qt.AlignCenter)
        self.main_line.addWidget(self.button2, alignment=Qt.AlignCenter)
        GroupBox2.setLayout(self.main_line)
        #проверка на нажатие кнопки
        self.button1.clicked.connect(PushButton1)
        self.button2.clicked.connect(PushButton2)

        #кнопки для калькулятора
        self.answer1 = QLineEdit()
        self.answer1.setPlaceholderText("Введите число:")
        self.answer2 = QLineEdit()
        self.answer2.setPlaceholderText("Введите число:")
        self.button3 = QPushButton("+", self)
        self.button4 = QPushButton("-", self)
        self.button5 = QPushButton("*", self)
        self.button6 = QPushButton("/", self)
        self.text = QLabel("Ответ:")
        #калькулятор
        def count1():
            try:
                num1 = float(self.answer1.text())
                num2 = float(self.answer2.text())
                answer = num1 + num2
                self.text.setText("Ответ:" + str(answer))
            except:
                print("Ошибка")
        def count2():
            try:
                num1 = float(self.answer1.text())
                num2 = float(self.answer2.text())
                answer = num1 - num2
                self.text.setText("Ответ:" + str(answer))
            except:
                print("Ошибка")


        def count3():
            try:
                num1 = float(self.answer1.text())
                num2 = float(self.answer2.text())
                answer = num1 * num2
                self.text.setText("Ответ:" + str(answer))
            except:
                print("Ошибка")


        def count4():
            try:
                num1 = float(self.answer1.text())
                num2 = float(self.answer2.text())
                if num2 == 0:
                    self.text.setText("На 0 делить нельзя")
                else:
                    answer = num1 / num2
                    self.text.setText("Ответ:" + str(answer))
            except:
                self.text.setText("Ошибка")
        #проверка на нажатие кнопок
        self.button3.clicked.connect(count1)
        self.button4.clicked.connect(count2)
        self.button5.clicked.connect(count3)
        self.button6.clicked.connect(count4)
        #прямоугольник
        def cs1():
            try:
                num3 = float(self.answer1.text())
                num4 = float(self.answer2.text())
                answer2 = (num3 * 2) + (num4 *2)
                self.text.setText("Ответ:" + str(answer2))
            except:
                print("Ошибка")
        #круг
        def cs2():
            try:
                num3 = float(self.answer1.text())
                num4 = float(self.answer2.text())
                answer2 = num3 * num4
                self.text.setText("Ответ:" + str(answer2))
            except:
                print("Ошибка")
        #квадрат 
        def cs3():
            try:
                num3 = float(self.answer1.text())
                num4 = float(self.answer2.text())
                answer2 = num3 * num4
                self.text.setText("Ответ:" + str(answer2))
            except:
                print("Ошибка")
        #тарпеция
        def cs4():
            try:
                num3 = float(self.answer1.text())
                num4 = float(self.answer2.text())
                answer2 = num3 * num4
                self.text.setText("Ответ:" + str(answer2))
            except:
                print("Ошибка")

        #кнопки выбора фигура
        self.button7 = QPushButton("Прямоугольник", self)
        self.button8 = QPushButton("Круг", self)
        self.button9 = QPushButton("Квадрат", self)
        self.button10 = QPushButton("Трапецея", self)
        #кнопки для фигур
        #прверка на нажатие кнопок
        self.button7.clicked.connect(cs1)
        self.button8.clicked.connect(cs2)
        self.button9.clicked.connect(cs3)
        self.button10.clicked.connect(cs4)
        #создание линий
        self.line1 = QHBoxLayout()
        self.line2 = QHBoxLayout()
        self.line3 = QVBoxLayout()
        #приклепление линий
        self.line1.addWidget(self.button3, alignment=Qt.AlignCenter)
        self.line1.addWidget(self.button4, alignment=Qt.AlignCenter)
        self.line2.addWidget(self.button5, alignment=Qt.AlignCenter)
        self.line2.addWidget(self.button6, alignment=Qt.AlignCenter)
        #закрепление всё к основной линии
        self.line3.addWidget(self.answer1)
        self.line3.addWidget(self.answer2)
        self.line3.addLayout(self.line1)
        self.line3.addLayout(self.line2)
        self.line3.addWidget(self.text)

        #создание линий
        self.line4 = QHBoxLayout()
        self.line5 = QHBoxLayout()
        self.line6 = QVBoxLayout()
        
        #закрепление кнопок выбора фигуры
        self.line4.addWidget(self.button7, alignment=Qt.AlignCenter)
        self.line4.addWidget(self.button8, alignment=Qt.AlignCenter)
        self.line5.addWidget(self.button9, alignment=Qt.AlignCenter)
        self.line5.addWidget(self.button10, alignment=Qt.AlignCenter)

        self.line6.addLayout(self.line4)
        self.line6.addLayout(self.line5)

        self.line7 = QHBoxLayout()
        self.line8 = QHBoxLayout()
        self.line9 = QHBoxLayout()
        self.line10 = QHBoxLayout()
        self.line11 = QHBoxLayout()
        self.line12 = QHBoxLayout()
        self.line13 = QHBoxLayout()
        self.line14 = QHBoxLayout()
        self.line15 = QHBoxLayout()
        self.line16 = QHBoxLayout()
        self.line17 = QHBoxLayout()


        GroupBox3.setLayout(self.line6)
        GroupBox1.setLayout(self.line3)
        GroupBox1.hide()
        GroupBox3.hide()
        GroupBox4.hide()
        GroupBox5.hide()
        GroupBox6.hide()
        GroupBox7.hide()
        #прикрепление боксов к окну
        main_poloska.addWidget(GroupBox1, alignment=Qt.AlignCenter)
        main_poloska.addWidget(GroupBox2, alignment=Qt.AlignCenter)
        main_poloska.addWidget(GroupBox3, alignment=Qt.AlignCenter)
        main_poloska.addWidget(GroupBox4, alignment=Qt.AlignCenter)
        main_poloska.addWidget(GroupBox5, alignment=Qt.AlignCenter)
        main_poloska.addWidget(GroupBox6, alignment=Qt.AlignCenter)
        main_poloska.addWidget(GroupBox7, alignment=Qt.AlignCenter)
        
        self.main_window.setLayout(main_poloska)
        self.main_window.show()

app = QApplication([])
main_win = main()
app.exec_()
