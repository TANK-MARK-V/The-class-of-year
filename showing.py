from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView


class Show(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Klass.sqlite')
        db.open()
        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable(self.name)
        model.select()
        view.setModel(model)
        if self.name == 'weeks':
            view.move(10, 10)
            view.resize(1802, 800)
            self.setGeometry(49, 100, 1822, 900)
        else:
            view.move(8, 8)
            view.resize(1904, 800)
            self.setGeometry(5, 100, 1920, 900)
        self.setWindowTitle('Таблица')
