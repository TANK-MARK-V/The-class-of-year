from PyQt5 import uic
import io
from PyQt5.QtWidgets import QMainWindow
import sqlite3

SPISOK = (
    '1 А', '1 Б', '1 В', '1 Г', '1 Д', '2 А', '2 Б', '2 В', '2 Г', '2 Д', '3 А', '3 Б', '3 В', '3 Г', '4 А', '4 Б',
    '4 В',
    '5 А', '5 Б', '6 А', '6 Б', '6 В', '7 А', '7 Б', '7 В', '7 Г', '8 А', '8 Б', '9 А', '9 Б', '10 А', '11 А', '11 Б')
NAMES = (
    '1a', '1b', '1v', '1g', '1d', '2a', '2b', '2v', '2g', '2d', '3a', '3b', '3v', '3g', '4a', '4b', '4v',
    '5a', '5b', '6a', '6b', '6v', '7a', '7b', '7v', '7g', '8a', '8b', '9a', '9b', '10a', '11a', '11b')
PRIME = ('1a', '1b', '1v', '1g', '1d', '2a', '2b', '2v', '2g', '2d', '3a', '3b', '3v', '3g', '4a', '4b', '4v')
SECONDARY = ('5a', '5b', '6a', '6b', '6v', '7a', '7b', '7v', '7g', '8a', '8b', '9a', '9b', '10a', '11a', '11b')
balls = []

with open("adding_week.txt", "r", encoding="utf-8") as lines:
    week_design = ''.join(lines.readlines())
with open('Количество человек.txt', 'r', encoding='utf-8') as lines:
    balls = lines.readline().split()


class Adding(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(week_design), self)
        self.initUI()

    def initUI(self):
        self.adding.clicked.connect(self.checking)
        self.automatick.clicked.connect(self.fatting)
        self.nuls.clicked.connect(self.zeros)

    def zeros(self):
        for name in NAMES:
            eval(f'self.mist_{str(name)}.setText("0")')

    def checking(self):
        if self.checkBox.isChecked():
            self.get_results()

    def fatting(self):
        for i in range(len(NAMES)):
            eval(f'self.balls_{NAMES[i]}.setText(str({balls[i]}))')

    def get_results(self):
        mists_small = list()
        mists_huge = list()
        balls_small = list()
        balls_huge = list()
        for name in PRIME:
            mists_small.append(eval(f'self.mist_{name}.text()'))
            balls_small.append(eval(f'self.balls_{name}.text()'))
        for name in SECONDARY:
            mists_huge.append(eval(f'self.mist_{name}.text()'))
            balls_huge.append(eval(f'self.balls_{name}.text()'))
        marks_small = dict()
        marks_small['Дата'] = self.date.text()
        marks_small['Проверяли'] = self.problems.text()
        marks_huge = dict()
        marks_huge['Дата'] = self.date.text()
        marks_huge['Проверяли'] = self.problems.text()
        leng = len(PRIME)
        for i in range(leng):
            marks_small[SPISOK[i]] = str(int(100 - (((int(mists_small[i]) / int(balls_small[i])) * 100) // 1)))
        for i in range(len(SECONDARY)):
            marks_huge[SPISOK[i + leng]] = str(int(100 - (((int(mists_huge[i]) / int(balls_huge[i])) * 100) // 1)))
        castle_small = '", "'.join(marks_small.keys())
        items_small = '", "'.join(marks_small.values())
        castle_huge = '", "'.join(marks_huge.keys())
        items_huge = '", "'.join(marks_huge.values())
        con = sqlite3.connect('Klass.sqlite')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO weeks_primary("{castle_small}") VALUES("{items_small}")""").fetchall()
        cur.execute(f"""INSERT INTO weeks_secondary("{castle_huge}") VALUES("{items_huge}")""").fetchall()
        con.commit()
        self.close()
