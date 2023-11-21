from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle


class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2  = wrong2
        self.wrong3 = wrong3


questions = []
questions.append(Question('Перевод слова "Table"','Стол','Табурет','Шкаф','Стул'))
questions.append(Question('Перевод слова "Ant"','Муравей','Комар','Жук','Паук'))
questions.append(Question('Перевод слова "Apple"','Яблоко','Черника','Мандарин','Виноград'))
questions.append(Question('Перевод слова "Wall"','Стена','Потолок','Пол','Ковёр'))

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,200)
main_win.counter = 0
main_win.q_counter = 0
main_win.res_counter = 0

question_label = QLabel('Текст вопроса')
answer_button = QPushButton('Ответить')
a1 = QRadioButton('вар1')
a2 = QRadioButton('вар2')
a3 = QRadioButton('вар3')
a4 = QRadioButton('вар4')
rg = QButtonGroup()
rg.addButton(a1)
rg.addButton(a2)
rg.addButton(a3)
rg.addButton(a4)

gb1 = QGroupBox('Варианты ответов')

layout_quest1 = QVBoxLayout()
layout_quest2 = QVBoxLayout()

layout_quest1.addWidget(a1)
layout_quest1.addWidget(a2)
layout_quest2.addWidget(a3)
layout_quest2.addWidget(a4)

layout_gb1 = QHBoxLayout()

layout_gb1.addLayout(layout_quest1)
layout_gb1.addLayout(layout_quest2)

gb1.setLayout(layout_gb1)

layout_support1 = QHBoxLayout()
layout_support2 = QHBoxLayout()
layout_support3 = QHBoxLayout()

layout_support1.addWidget(question_label, alignment = Qt.AlignCenter)

layout_support2.addWidget(gb1)

layout_support3.addWidget(answer_button)

layout_main = QVBoxLayout()

layout_main.addLayout(layout_support1)
layout_main.addLayout(layout_support2)
layout_main.addLayout(layout_support3)

hint_label = QLabel('Самый сложный вопрос в мире!')
correctness_label = QLabel('Правильно/Неправильно')
right_label = QLabel('Правильный ответ')
next_button = QPushButton('Следующий вопрос')

gb2 = QGroupBox('Результат теста')

layout_gb2 = QVBoxLayout()

layout_gb2.addWidget(correctness_label)
layout_gb2.addWidget(right_label, alignment = Qt.AlignCenter)

gb2.setLayout(layout_gb2)

layout_support1.addWidget(hint_label, alignment = Qt.AlignCenter)
layout_support2.addWidget(gb2)
layout_support3.addWidget(next_button)

answers = [a1, a2, a3, a4]


# Чтобы комментить несколько строк:
# 1. Выделить несколько строк
# 2. Нажать ctrl + /(?)


def ask(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_label.setText(q.question)
    right_label.setText(q.right)

def show_result():
    question_label.hide()
    gb1.hide()
    answer_button.hide()
    hint_label.show()
    next_button.show()
    gb2.show()
    print('-Всего вопросов:', main_win.q_counter)
    print('-Правильных ответов:', main_win.res_counter)

def check_answer():
    # Какая-то проверка
    # Что нажатая кнопка имеет такой же текст как и текущий вопрос (с номером counter)
    if a1.isChecked() :
        if a1.text() == questions[main_win.counter - 1].right:
            correctness_label.setText('Правильно')
            main_win.res_counter += 1
        else :
            correctness_label.setText('Неправильно')
        main_win.q_counter += 1
    elif a2.isChecked() :
        if a2.text() == questions[main_win.counter - 1].right:
            correctness_label.setText('Правильно')
            main_win.res_counter += 1
        else :
            correctness_label.setText('Неправильно')
        main_win.q_counter += 1
    elif a3.isChecked() :
        if a3.text() == questions[main_win.counter - 1].right:
            correctness_label.setText('Правильно')
            main_win.res_counter += 1
        else :
            correctness_label.setText('Неправильно')
        main_win.q_counter += 1
    elif a4.isChecked() :
        if a4.text() == questions[main_win.counter - 1].right:
            correctness_label.setText('Правильно')
            main_win.res_counter += 1
        else :
            correctness_label.setText('Неправильно')
        main_win.q_counter += 1
    show_result()

def show_question():
    hint_label.hide()
    gb2.hide()
    next_button.hide()
    question_label.show()
    gb1.show()
    answer_button.show()
    rg.setExclusive(False)
    a1.setChecked(False)
    a2.setChecked(False)
    a3.setChecked(False)
    a4.setChecked(False)
    rg.setExclusive(True)

    # автоматизация следующего вопроса
    ask(questions[main_win.counter])
    main_win.counter += 1

    if main_win.counter == len(questions):
        shuffle(questions)
        main_win.counter = 0


    # сколько-то строчек кода


answer_button.clicked.connect(check_answer)
next_button.clicked.connect(show_question)



hint_label.hide()
gb2.hide()
next_button.hide()

main_win.setLayout(layout_main)
main_win.show()
show_question()

app.exec_()
