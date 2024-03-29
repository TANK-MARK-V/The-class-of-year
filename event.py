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
        marks_small = dict()
        marks_small['Дата'] = self.date.text()
        marks_small['Название'] = self.named.text()
        marks_small['Максимум'] = self.igor.text()
        marks_huge = dict()
        marks_huge['Дата'] = self.date.text()
        marks_huge['Название'] = self.named.text()
        marks_huge['Максимум'] = self.igor.text()
        small, huge = self.auto(1)
        leng = len(PRIME)
        for i in range(leng):
            marks_small[SPISOK[i]] = small[i]
        for i in range(len(SECONDARY)):
            marks_huge[SPISOK[i + leng]] = huge[i]
        castle_small = '", "'.join(marks_small.keys())
        items_small = '", "'.join(marks_small.values())
        castle_huge = '", "'.join(marks_huge.keys())
        items_huge = '", "'.join(marks_huge.values())
        con = sqlite3.connect('Klass.sqlite')
        cur = con.cursor()
        cur.execute(f"""INSERT INTO events_primary("{castle_small}") VALUES("{items_small}")""").fetchall()
        cur.execute(f"""INSERT INTO events_secondary("{castle_huge}") VALUES("{items_huge}")""").fetchall()
        con.commit()
        self.close()

    def auto(self, flag=0):
        dct = {
            'Не принял участия': '0', '1-ое место': '40', '2-ое место': '20', '3-ее место': '10', 'Остальные места': '5'
        }
        if not flag:
            for name in NAMES:
                current_text = str(eval(f'dct[self.choise_{name}.currentText()]'))
                eval(f'self.balls_{name}.setText(str({current_text}))')
        if flag:
            little = []
            big = []
            for name in NAMES:
                if name in PRIME:
                    little.append(eval(f'self.balls_{name}.text()'))
                else:
                    big.append(eval(f'self.balls_{name}.text()'))
            return little, big
