from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView


class Show(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.size = 1600
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
        view.move(8, 8)
        view.resize(self.size - 8 * 2, 800)
        self.setGeometry((1920 - self.size) // 2, 100, self.size, 900)
        self.setWindowTitle('Таблица')
