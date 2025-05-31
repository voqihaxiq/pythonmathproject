from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGroupBox

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project")
        self.resize(600, 400)

        # --- Главный выбор ---
        self.main_choice_box = QGroupBox()
        self.button1 = QPushButton("Калькулятор")
        self.button2 = QPushButton("Определение площади")
        main_choice_layout = QVBoxLayout()
        main_choice_layout.addWidget(self.button1)
        main_choice_layout.addWidget(self.button2)
        self.main_choice_box.setLayout(main_choice_layout)

        # --- Бокс выбора фигур ---
        self.figure_choice_box = QGroupBox("Выберите фигуру")
        self.button_rect = QPushButton("Прямоугольник")
        self.button_back_from_figures = QPushButton("Назад")
        figure_choice_layout = QVBoxLayout()
        figure_choice_layout.addWidget(self.button_rect)
        figure_choice_layout.addWidget(self.button_back_from_figures)
        self.figure_choice_box.setLayout(figure_choice_layout)
        self.figure_choice_box.hide()

        # --- Калькулятор (твой оригинальный, без изменений) ---
        self.calc_box = QGroupBox("Калькулятор")

        self.answer1 = QLineEdit()
        self.answer1.setPlaceholderText("Введите число:")
        self.answer2 = QLineEdit()
        self.answer2.setPlaceholderText("Введите число:")
        self.button3 = QPushButton("+")
        self.button4 = QPushButton("-")
        self.button5 = QPushButton("*")
        self.button6 = QPushButton("/")
        self.text = QLabel("Ответ:")
        self.button_back_from_calc = QPushButton("Назад")

        self.line1 = QHBoxLayout()
        self.line1.addWidget(self.button3, alignment=Qt.AlignCenter)
        self.line1.addWidget(self.button4, alignment=Qt.AlignCenter)
        self.line2 = QHBoxLayout()
        self.line2.addWidget(self.button5, alignment=Qt.AlignCenter)
        self.line2.addWidget(self.button6, alignment=Qt.AlignCenter)

        self.line3 = QVBoxLayout()
        self.line3.addWidget(self.answer1)
        self.line3.addWidget(self.answer2)
        self.line3.addLayout(self.line1)
        self.line3.addLayout(self.line2)
        self.line3.addWidget(self.text)
        self.line3.addWidget(self.button_back_from_calc)

        self.calc_box.setLayout(self.line3)
        self.calc_box.hide()

        # --- Форма для прямоугольника ---
        self.rect_box = QGroupBox("Прямоугольник")
        self.text1 = QLabel("Прямоугольник")
        self.text2 = QLabel("S = a*b")
        self.text3 = QLabel("Результат:")
        self.lineedit1 = QLineEdit()
        self.lineedit1.setPlaceholderText("Введите:")
        self.lineedit2 = QLineEdit()
        self.lineedit2.setPlaceholderText("Введите:")
        self.button8 = QPushButton("Ответ")
        self.button_back_from_rect = QPushButton("Назад")

        rect_layout = QVBoxLayout()
        rect_layout.addWidget(self.text1, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.text2, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.lineedit1, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.lineedit2, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.text3, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.button8, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.button_back_from_rect)
        self.rect_box.setLayout(rect_layout)
        self.rect_box.hide()

        # --- Основной лэйаут ---
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.main_choice_box)
        main_layout.addWidget(self.figure_choice_box)
        main_layout.addWidget(self.calc_box)
        main_layout.addWidget(self.rect_box)
        self.setLayout(main_layout)

        # --- Подключение кнопок ---
        self.button1.clicked.connect(self.show_calc)
        self.button2.clicked.connect(self.show_figure_choice)

        self.button_rect.clicked.connect(self.show_rectangle)
        self.button_back_from_figures.clicked.connect(self.show_main_choice)
        self.button_back_from_calc.clicked.connect(self.show_main_choice)
        self.button_back_from_rect.clicked.connect(self.show_figure_choice)

        self.button3.clicked.connect(self.count1)
        self.button4.clicked.connect(self.count2)
        self.button5.clicked.connect(self.count3)
        self.button6.clicked.connect(self.count4)
        self.button8.clicked.connect(self.PushButton3)

    # --- Методы переключения ---
    def show_main_choice(self):
        self.main_choice_box.show()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.hide()

    def show_figure_choice(self):
        self.main_choice_box.hide()
        self.figure_choice_box.show()
        self.calc_box.hide()
        self.rect_box.hide()

    def show_calc(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.show()
        self.rect_box.hide()

    def show_rectangle(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.show()

    # --- Твои функции калькулятора ---
    def count1(self):
        try:
            num1 = float(self.answer1.text())
            num2 = float(self.answer2.text())
            answer = num1 + num2
            self.text.setText("Ответ:" + str(answer))
        except:
            print("Ошибка")

    def count2(self):
        try:
            num1 = float(self.answer1.text())
            num2 = float(self.answer2.text())
            answer = num1 - num2
            self.text.setText("Ответ:" + str(answer))
        except:
            print("Ошибка")

    def count3(self):
        try:
            num1 = float(self.answer1.text())
            num2 = float(self.answer2.text())
            answer = num1 * num2
            self.text.setText("Ответ:" + str(answer))
        except:
            print("Ошибка")

    def count4(self):
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

    # --- Функция площади прямоугольника ---
    def PushButton3(self):
        try:
            num3 = float(self.lineedit1.text())
            num4 = float(self.lineedit2.text())
            answer = num3 * num4
            self.text3.setText("Ответ:"+ str(answer))
        except:
            print("Ошибка")

if __name__ == "__main__":
    app = QApplication([])
    main_win = main()
    main_win.show()
    app.exec_()
