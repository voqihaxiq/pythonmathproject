from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QGroupBox
import math

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project")
        self.resize(600, 400)

        # --- Главный выбор ---
        self.main_choice_box = QGroupBox()
        self.button1 = QPushButton("Калькулятор")
        self.button2 = QPushButton("Определение площади")
        main_choice_layout = QHBoxLayout()
        main_choice_layout.addWidget(self.button1)
        main_choice_layout.addWidget(self.button2)
        self.main_choice_box.setLayout(main_choice_layout)

        # --- Бокс выбора фигур ---
        self.figure_choice_box = QGroupBox("Выберите фигуру")
        self.button7 = QPushButton("Прямоугольник", self)
        self.button8 = QPushButton("Круг", self)
        self.button9 = QPushButton("Квадрат", self)
        self.button10 = QPushButton("Трапецея", self)
        self.button_back_from_figures = QPushButton("Назад")

        figure_choice_layout = QVBoxLayout()
        figure_choice_layout1 = QHBoxLayout()
        figure_choice_layout2 = QHBoxLayout()

        figure_choice_layout1.addWidget(self.button7)
        figure_choice_layout1.addWidget(self.button8)
        figure_choice_layout2.addWidget(self.button9)
        figure_choice_layout2.addWidget(self.button10)
        figure_choice_layout.addLayout(figure_choice_layout1)
        figure_choice_layout.addLayout(figure_choice_layout2)
        figure_choice_layout.addWidget(self.button_back_from_figures)
        self.figure_choice_box.setLayout(figure_choice_layout)
        self.figure_choice_box.hide()

        # --- Калькулятор ---
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

        # --- Прямоугольник ---
        self.rect_box = QGroupBox("Прямоугольник")
        self.text1 = QLabel("Прямоугольник")
        self.text2 = QLabel("S = a*b")
        self.text3 = QLabel("Результат:")
        self.lineedit1 = QLineEdit()
        self.lineedit1.setPlaceholderText("Введите сторону a")
        self.lineedit2 = QLineEdit()
        self.lineedit2.setPlaceholderText("Введите сторону b")
        self.button_answer = QPushButton("Ответ")
        self.button_back_from_rect = QPushButton("Назад")

        rect_layout = QVBoxLayout()
        rect_layout.addWidget(self.text1, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.text2, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.lineedit1, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.lineedit2, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.text3, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.button_answer, alignment=Qt.AlignCenter)
        rect_layout.addWidget(self.button_back_from_rect)
        self.rect_box.setLayout(rect_layout)
        self.rect_box.hide()

        # --- Круг ---
        self.circle_box = QGroupBox("Круг")
        self.circle_box.hide()
        self.circle_info_label = QLabel("S = π * r²")
        self.circle_input = QLineEdit()
        self.circle_input.setPlaceholderText("Радиус:")
        self.circle_result = QLabel("Результат:")
        self.circle_button = QPushButton("Ответ")
        self.circle_back_button = QPushButton("Назад")

        circle_layout = QVBoxLayout()
        circle_layout.addWidget(self.circle_info_label, alignment=Qt.AlignCenter)
        circle_layout.addWidget(self.circle_input, alignment=Qt.AlignCenter)
        circle_layout.addWidget(self.circle_result, alignment=Qt.AlignCenter)
        circle_layout.addWidget(self.circle_button, alignment=Qt.AlignCenter)
        circle_layout.addWidget(self.circle_back_button, alignment=Qt.AlignCenter)
        self.circle_box.setLayout(circle_layout)

        # --- Квадрат ---
        self.square_box = QGroupBox("Квадрат")
        self.square_box.hide()
        self.square_info_label = QLabel("S = a²")
        self.square_input = QLineEdit()
        self.square_input.setPlaceholderText("Сторона квадрата:")
        self.square_result = QLabel("Результат:")
        self.square_button = QPushButton("Ответ")
        self.square_back_button = QPushButton("Назад")

        square_layout = QVBoxLayout()
        square_layout.addWidget(self.square_info_label, alignment=Qt.AlignCenter)
        square_layout.addWidget(self.square_input, alignment=Qt.AlignCenter)
        square_layout.addWidget(self.square_result, alignment=Qt.AlignCenter)
        square_layout.addWidget(self.square_button, alignment=Qt.AlignCenter)
        square_layout.addWidget(self.square_back_button, alignment=Qt.AlignCenter)
        self.square_box.setLayout(square_layout)

        # --- Трапеция ---
        self.tr_box = QGroupBox("Трапеция")
        self.tr_box.hide()
        self.tr_info_label = QLabel("S = (a + b) / 2 * h")
        self.tr_lineedit_a = QLineEdit()
        self.tr_lineedit_a.setPlaceholderText("Сторона a:")
        self.tr_lineedit_b = QLineEdit()
        self.tr_lineedit_b.setPlaceholderText("Сторона b:")
        self.tr_lineedit_h = QLineEdit()
        self.tr_lineedit_h.setPlaceholderText("Высота h:")
        self.tr_result_label = QLabel("Результат:")
        self.tr_button = QPushButton("Ответ")
        self.tr_back_button = QPushButton("Назад")

        layout_t = QVBoxLayout()
        layout_t.addWidget(self.tr_info_label, alignment=Qt.AlignCenter)
        layout_t.addWidget(self.tr_lineedit_a, alignment=Qt.AlignCenter)
        layout_t.addWidget(self.tr_lineedit_b, alignment=Qt.AlignCenter)
        layout_t.addWidget(self.tr_lineedit_h, alignment=Qt.AlignCenter)
        layout_t.addWidget(self.tr_result_label, alignment=Qt.AlignCenter)
        layout_t.addWidget(self.tr_button, alignment=Qt.AlignCenter)
        layout_t.addWidget(self.tr_back_button, alignment=Qt.AlignCenter)
        self.tr_box.setLayout(layout_t)

        # --- Основной layout ---
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.main_choice_box)
        main_layout.addWidget(self.figure_choice_box)
        main_layout.addWidget(self.calc_box)
        main_layout.addWidget(self.rect_box)
        main_layout.addWidget(self.circle_box)
        main_layout.addWidget(self.square_box)
        main_layout.addWidget(self.tr_box)
        self.setLayout(main_layout)

        # --- Подключения ---
        self.button1.clicked.connect(self.show_calc)
        self.button2.clicked.connect(self.show_figure_choice)
        self.button7.clicked.connect(self.show_rectangle)
        self.button8.clicked.connect(self.show_circle)
        self.button9.clicked.connect(self.show_square)
        self.button10.clicked.connect(self.show_trapezoid)

        self.button_back_from_figures.clicked.connect(self.show_main_choice)
        self.button_back_from_calc.clicked.connect(self.show_main_choice)
        self.button_back_from_rect.clicked.connect(self.show_figure_choice)
        self.circle_back_button.clicked.connect(self.show_figure_choice)
        self.square_back_button.clicked.connect(self.show_figure_choice)
        self.tr_back_button.clicked.connect(self.show_figure_choice)

        self.button3.clicked.connect(self.count1)
        self.button4.clicked.connect(self.count2)
        self.button5.clicked.connect(self.count3)
        self.button6.clicked.connect(self.count4)

        self.button_answer.clicked.connect(self.calc_rectangle_area)
        self.circle_button.clicked.connect(self.calc_circle_area)
        self.square_button.clicked.connect(self.calc_square_area)
        self.tr_button.clicked.connect(self.calc_trapezoid_area)

    # --- Переключения ---
    def show_main_choice(self):
        self.main_choice_box.show()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.hide()
        self.circle_box.hide()
        self.square_box.hide()
        self.tr_box.hide()

    def show_figure_choice(self):
        self.main_choice_box.hide()
        self.figure_choice_box.show()
        self.calc_box.hide()
        self.rect_box.hide()
        self.circle_box.hide()
        self.square_box.hide()
        self.tr_box.hide()

    def show_calc(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.show()
        self.rect_box.hide()
        self.circle_box.hide()
        self.square_box.hide()
        self.tr_box.hide()

    def show_rectangle(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.show()
        self.circle_box.hide()
        self.square_box.hide()
        self.tr_box.hide()

    def show_circle(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.hide()
        self.circle_box.show()
        self.square_box.hide()
        self.tr_box.hide()

    def show_square(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.hide()
        self.circle_box.hide()
        self.square_box.show()
        self.tr_box.hide()

    def show_trapezoid(self):
        self.main_choice_box.hide()
        self.figure_choice_box.hide()
        self.calc_box.hide()
        self.rect_box.hide()
        self.circle_box.hide()
        self.square_box.hide()
        self.tr_box.show()

    # --- Калькулятор ---
    def count1(self):
        try:
            a = float(self.answer1.text())
            b = float(self.answer2.text())
            self.text.setText(f"Ответ: {a + b}")
        except:
            self.text.setText("Ошибка ввода")

    def count2(self):
        try:
            a = float(self.answer1.text())
            b = float(self.answer2.text())
            self.text.setText(f"Ответ: {a - b}")
        except:
            self.text.setText("Ошибка ввода")

    def count3(self):
        try:
            a = float(self.answer1.text())
            b = float(self.answer2.text())
            self.text.setText(f"Ответ: {a * b}")
        except:
            self.text.setText("Ошибка ввода")

    def count4(self):
        try:
            a = float(self.answer1.text())
            b = float(self.answer2.text())
            if b == 0:
                self.text.setText("На 0 делить нельзя")
            else:
                self.text.setText(f"Ответ: {a / b}")
        except:
            self.text.setText("Ошибка ввода")

    # --- Площади ---
    def calc_rectangle_area(self):
        try:
            a = float(self.lineedit1.text())
            b = float(self.lineedit2.text())
            self.text3.setText(f"Ответ: {a * b}")
        except:
            self.text3.setText("Ошибка ввода")

    def calc_circle_area(self):
        try:
            r = float(self.circle_input.text())
            area = math.pi * r ** 2
            self.circle_result.setText(f"Ответ: {area}")
        except:
            self.circle_result.setText("Ошибка ввода")

    def calc_square_area(self):
        try:
            a = float(self.square_input.text())
            self.square_result.setText(f"Ответ: {a ** 2}")
        except:
            self.square_result.setText("Ошибка ввода")

    def calc_trapezoid_area(self):
        try:
            a = float(self.tr_lineedit_a.text())
            b = float(self.tr_lineedit_b.text())
            h = float(self.tr_lineedit_h.text())
            area = (a + b) / 2 * h
            self.tr_result_label.setText(f"Ответ: {area}")
        except:
            self.tr_result_label.setText("Ошибка ввода")

if __name__ == "__main__":
    app = QApplication([])
    main_win = main()
    main_win.show()
    app.exec_()
