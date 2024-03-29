import sys
import io
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3

import event
import showing
import week

SPISOK = (
    '1 А', '1 Б', '1 В', '1 Г', '1 Д', '2 А', '2 Б', '2 В', '2 Г', '2 Д', '3 А', '3 Б', '3 В', '3 Г', '4 А', '4 Б',
    '4 В',
    '5 А', '5 Б', '6 А', '6 Б', '6 В', '7 А', '7 Б', '7 В', '7 Г', '8 А', '8 Б', '9 А', '9 Б', '10 А', '11 А', '11 Б')

LITTLE = (
    '1 А', '1 Б', '1 В', '1 Г', '1 Д', '2 А', '2 Б', '2 В', '2 Г', '2 Д', '3 А', '3 Б', '3 В', '3 Г', '4 А', '4 Б',
    '4 В')
BIG = (
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
        self.show_balls.clicked.connect(self.showing)
        self.final_button.clicked.connect(self.final)

    def add_events(self):
        self.eventing = event.Adding()
        self.eventing.show()

    def add_weeks(self):
        self.weekend = week.Adding()
        self.weekend.show()

    def showing(self):
        dct_school = {'Начальная школа': 'primary', 'Средняя школа': 'secondary'}
        school = dct_school[self.school.currentText()]
        dct_type = {'Мероприятия': 'events_', 'Недели': 'weeks_'}
        type = dct_type[self.type.currentText()]
        self.checking = showing.Show(type + school)
        self.checking.show()

    def final(self):
        con = sqlite3.connect("Klass.sqlite")
        cur = con.cursor()

        eventing = dict()
        weeking = dict()
        for clas in SPISOK:
            eventing[clas] = 0
            weeking[clas] = 0

        events_primary = cur.execute("SELECT * FROM events_primary").fetchall()
        events_secondary = cur.execute("SELECT * FROM events_secondary").fetchall()
        weeks_primary = cur.execute("SELECT * FROM weeks_primary").fetchall()
        weeks_secondary = cur.execute("SELECT * FROM weeks_secondary").fetchall()
        many = len(weeks_primary)
        maksimum = 0

        for ev in events_primary:
            maksimum += int(ev[2])
            for i in range(len(ev[3:])):
                eventing[LITTLE[i]] += int(ev[i + 3])
        for ev in events_secondary:
            for i in range(len(ev[3:])):
                eventing[BIG[i]] += int(ev[i + 3])
        for we in weeks_primary:
            for i in range(len(we[2:])):
                weeking[LITTLE[i]] += int(we[i + 2])
        for we in weeks_secondary:
            for i in range(len(we[2:])):
                weeking[BIG[i]] += int(we[i + 2])

        classes = dict()
        for clas in SPISOK:
            classes[clas] = eventing[clas] + int((weeking[clas] / many / 100) * maksimum)

        ready = ''
        maks = 0
        file = open('Баллы классов.txt', 'w', encoding='utf-8')
        for klass in SPISOK:
            if klass == '5 А':
                file.write('\n')
            score = classes[klass]
            if score > maks:
                ready = klass
                maks = score
            elif score == maks:
                ready += f', {klass}'
            file.write(f'{klass}: {eventing[klass]} + {classes[klass] - eventing[klass]} = {classes[klass]}\n')
        file.write(f'\nКласс года: {ready}')
        file.close()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Project()
    ex.show()
    sys.exit(app.exec())
