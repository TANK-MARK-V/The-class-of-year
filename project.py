import sys
import io
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3

import event
import showing
import week


SPISOK = (
    '5 А', '5 Б', '6 А', '6 Б', '6 В', '7 А', '7 Б', '7 В', '7 Г', '8 А', '8 Б', '9 А', '9 Б', '10 А', '11 А', '11 Б')
with open("main_design.txt", "r", encoding="utf-8") as lines:
    main_design = ''.join(lines.readlines())


class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(io.StringIO(main_design), self)
        self.initUI()

    def initUI(self):
        self.add_event.clicked.connect(self.add_events)
        self.add_week.clicked.connect(self.add_weeks)
        self.show_event.clicked.connect(self.show_events)
        self.show_week.clicked.connect(self.show_weeks)
        self.final_button.clicked.connect(self.final)

    def add_events(self):
        self.eventing = event.Adding()
        self.eventing.show()

    def add_weeks(self):
        self.weekend = week.Adding()
        self.weekend.show()

    def show_events(self):
        self.checking = showing.Show('events')
        self.checking.show()

    def show_weeks(self):
        self.checking = showing.Show('weeks')
        self.checking.show()

    def final(self):
        con = sqlite3.connect("Klass.sqlite")
        cur = con.cursor()
        eventing = dict()
        result = cur.execute("SELECT * FROM events").fetchall()
        krico = 'Дата Название Максимум'.split() + list(SPISOK)
        for estriper in result:
            for i in range(19):
                if krico[i] in eventing.keys():
                    if krico[i] not in 'Дата Название':
                        eventing[krico[i]] += int(estriper[i])
                    else:
                        eventing[krico[i]].append(estriper[i])
                else:
                    if krico[i] not in 'Дата Название':
                        eventing[krico[i]] = int(estriper[i])
                    else:
                        eventing[krico[i]] = [estriper[i]]
        num = int(eventing['Максимум'] / 3)
        weeking = dict()
        result = cur.execute("SELECT * FROM weeks").fetchall()
        kawasaki = 'Дата Проверяли'.split() + list(SPISOK)
        for cago in result:
            for i in range(18):
                if kawasaki[i] in weeking.keys():
                    if kawasaki[i] not in 'Дата Проверяли':
                        weeking[kawasaki[i]] += int(cago[i])
                    else:
                        weeking[kawasaki[i]].append(cago[i])
                else:
                    if kawasaki[i] not in 'Дата Проверяли':
                        weeking[kawasaki[i]] = int(cago[i])
                    else:
                        weeking[kawasaki[i]] = [cago[i]]
        many = len(weeking['Дата'])
        final = list()
        ready = ''
        maks = 0
        file = open('Баллы классов.txt', 'w', encoding='utf-8')
        for klass in SPISOK:
            score = eventing[klass] + int((weeking[klass] / many / 100) * num)
            if score > maks:
                ready = klass
                maks = score
            elif score == maks:
                ready += f', {klass}'
            final.append(score)
            file.write(f'{klass}: {eventing[klass]} + {int((weeking[klass] / many / 100) * num)} = {score}\n')
        file.close()
        self.label.setText(ready)
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
