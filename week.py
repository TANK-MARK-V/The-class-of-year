from PyQt5 import uic
import io
from PyQt5.QtWidgets import QMainWindow
import sqlite3

SPISOK = (
    '5 А', '5 Б', '6 А', '6 Б', '6 В', '7 А', '7 Б', '7 В', '7 Г', '8 А', '8 Б', '9 А', '9 Б', '10 А', '11 А', '11 Б')
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
        self.mist_5a.setText('0')
        self.mist_5b.setText('0')
        self.mist_6a.setText('0')
        self.mist_6b.setText('0')
        self.mist_6v.setText('0')
        self.mist_7a.setText('0')
        self.mist_7b.setText('0')
        self.mist_7v.setText('0')
        self.mist_7g.setText('0')
        self.mist_8a.setText('0')
        self.mist_8b.setText('0')
        self.mist_9a.setText('0')
        self.mist_9b.setText('0')
        self.mist_10a.setText('0')
        self.mist_11a.setText('0')
        self.mist_11b.setText('0')

    def checking(self):
        if self.checkBox.isChecked():
            self.get_results()

    def fatting(self):
        self.balls_5a.setText(balls[0])
        self.balls_5b.setText(balls[1])
        self.balls_6a.setText(balls[2])
        self.balls_6b.setText(balls[3])
        self.balls_6v.setText(balls[4])
        self.balls_7a.setText(balls[5])
        self.balls_7b.setText(balls[6])
        self.balls_7v.setText(balls[7])
        self.balls_7g.setText(balls[8])
        self.balls_8a.setText(balls[9])
        self.balls_8b.setText(balls[10])
        self.balls_9a.setText(balls[11])
        self.balls_9b.setText(balls[12])
        self.balls_10a.setText(balls[13])
        self.balls_11a.setText(balls[14])
        self.balls_11b.setText(balls[15])

    def get_results(self):
        mists = list()
        mists.append(self.mist_5a.text())
        mists.append(self.mist_5b.text())
        mists.append(self.mist_6a.text())
        mists.append(self.mist_6b.text())
        mists.append(self.mist_6v.text())
        mists.append(self.mist_7a.text())
        mists.append(self.mist_7b.text())
        mists.append(self.mist_7v.text())
        mists.append(self.mist_7g.text())
        mists.append(self.mist_8a.text())
        mists.append(self.mist_8b.text())
        mists.append(self.mist_9a.text())
        mists.append(self.mist_9b.text())
        mists.append(self.mist_10a.text())
        mists.append(self.mist_11a.text())
        mists.append(self.mist_11b.text())

        ball = list()
        ball.append(self.balls_5a.text())
        ball.append(self.balls_5b.text())
        ball.append(self.balls_6a.text())
        ball.append(self.balls_6b.text())
        ball.append(self.balls_6v.text())
        ball.append(self.balls_7a.text())
        ball.append(self.balls_7b.text())
        ball.append(self.balls_7v.text())
        ball.append(self.balls_7g.text())
        ball.append(self.balls_8a.text())
        ball.append(self.balls_8b.text())
        ball.append(self.balls_9a.text())
        ball.append(self.balls_9b.text())
        ball.append(self.balls_10a.text())
        ball.append(self.balls_11a.text())
        ball.append(self.balls_11b.text())

        marks = dict()
        marks['Дата'] = self.date.text()
        marks['Проверяли'] = self.problems.text()
        for i in range(16):
            marks[SPISOK[i]] = str(int(100 - (((int(mists[i]) / int(ball[i])) * 100) // 1)))
        castle = '", "'.join(marks.keys())
        items = '", "'.join(marks.values())
        con = sqlite3.connect('Klass.sqlite')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO weeks("{castle}") VALUES("{items}")""").fetchall()
        con.commit()
        self.close()
