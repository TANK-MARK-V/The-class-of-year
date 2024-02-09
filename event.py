from PyQt5 import uic
import io
from PyQt5.QtWidgets import QMainWindow
import sqlite3

SPISOK = (
    '5 А', '5 Б', '6 А', '6 Б', '6 В', '7 А', '7 Б', '7 В', '7 Г', '8 А', '8 Б', '9 А', '9 Б', '10 А', '11 А', '11 Б')

with open("adding_event.txt", "r", encoding="utf-8") as lines:
    event_design = ''.join(lines.readlines())


class Adding(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(event_design), self)
        self.auto()
        self.initUI()

    def initUI(self):
        self.adding.clicked.connect(self.checking)
        self.pushButton.clicked.connect(self.auto)

    def checking(self):
        if self.checkBox.isChecked():
            self.get_results()

    def get_results(self):
        marks = dict()
        marks['Дата'] = self.date.text()
        marks['Название'] = self.named.text()
        marks['Максимум'] = self.igor.text()
        leest = self.auto(1)
        for i in range(len(SPISOK)):
            marks[SPISOK[i]] = leest[i]
        castle = '", "'.join(marks.keys())
        items = '", "'.join(marks.values())
        con = sqlite3.connect('Klass.sqlite')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO events("{castle}") VALUES("{items}")""").fetchall()
        con.commit()
        self.close()

    def auto(self, flag=0):
        dct = {
            'Не принял участия': '0', '1-ое место': '40', '2-ое место': '20', '3-ее место': '10', 'Остальные места': '5'
        }
        if not flag:
            self.balls_5a.setText(str(dct[self.choise_5a.currentText()]))
            self.balls_5b.setText(str(dct[self.choise_5b.currentText()]))
            self.balls_6a.setText(str(dct[self.choise_6a.currentText()]))
            self.balls_6b.setText(str(dct[self.choise_6b.currentText()]))
            self.balls_6v.setText(str(dct[self.choise_6v.currentText()]))
            self.balls_7a.setText(str(dct[self.choise_7a.currentText()]))
            self.balls_7b.setText(str(dct[self.choise_7b.currentText()]))
            self.balls_7v.setText(str(dct[self.choise_7v.currentText()]))
            self.balls_7g.setText(str(dct[self.choise_7g.currentText()]))
            self.balls_8a.setText(str(dct[self.choise_8a.currentText()]))
            self.balls_8b.setText(str(dct[self.choise_8b.currentText()]))
            self.balls_9a.setText(str(dct[self.choise_9a.currentText()]))
            self.balls_9b.setText(str(dct[self.choise_9b.currentText()]))
            self.balls_10a.setText(str(dct[self.choise_10a.currentText()]))
            self.balls_11a.setText(str(dct[self.choise_11a.currentText()]))
            self.balls_11b.setText(str(dct[self.choise_11b.currentText()]))
        if flag:
            least = []
            least.append(self.balls_5a.text())
            least.append(self.balls_5b.text())
            least.append(self.balls_6a.text())
            least.append(self.balls_6b.text())
            least.append(self.balls_6v.text())
            least.append(self.balls_7a.text())
            least.append(self.balls_7b.text())
            least.append(self.balls_7v.text())
            least.append(self.balls_7g.text())
            least.append(self.balls_8a.text())
            least.append(self.balls_8b.text())
            least.append(self.balls_9a.text())
            least.append(self.balls_9b.text())
            least.append(self.balls_10a.text())
            least.append(self.balls_11a.text())
            least.append(self.balls_11b.text())
            return least
