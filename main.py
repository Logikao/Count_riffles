import sys
import random as rd
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
)

#   cria a janela
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabela de Sorteios")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.populate_table()

    #   função do sorteio
    def riffle(self, j):
        count = 0

        for i in range(j):
            x = [rd.choice(self.fist_lether), rd.choice(self.second_lether),
                 rd.choice(self.third_lether), rd.choice(self.fourth_lether)]
            if x == self.word:
                count += 1
        return count

    #   função para porcentagem de acerto
    def guess(self):
        porcent_1 = (self.count_1 / 72) * 100
        porcent_2 = (self.count_2 / 216) * 100
        porcent_3 = (self.count_3 / 720) * 100
        porcent_4 = (self.count_4 / 2160) * 100
        porcent_5 = (self.count_5 / 7200) * 100
        porcent_6 = (self.count_6 / 72000) * 100

        porcent = (porcent_1 + porcent_2 + porcent_3 + porcent_4 + porcent_5 + porcent_6) / 6
        porcent = round(porcent, 2)

        return porcent

    #   função da tabela
    def populate_table(self):
        #   define as variáveis das letras
        self.fist_lether = ["Q", "W", "X", "Z"]
        self.second_lether = ["A", "I", "U"]
        self.third_lether = ["C", "F", "P"]
        self.fourth_lether = ["E", "O"]

        #   define as colunas
        self.table.setColumnCount(8)
        #   define o cabeçalho
        self.table.setHorizontalHeaderLabels(["Palavras", "72 sorteios", "216 sorteios", "720 sorteios",
                                              "2.160 sorteios", "7.200 sorteios", "72.000 sorteios",
                                              "Esperado (%) [Média]"])
        self.table.verticalHeader().setVisible(False)   #   seta a tabela vertical como falsa
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #   main go
        for i in range(6):
            self.word = [rd.choice(self.fist_lether), rd.choice(self.second_lether),
                         rd.choice(self.third_lether), rd.choice(self.fourth_lether)]

            #   puxa/faz as informações
            self.count_1 = self.riffle(72)
            self.count_2 = self.riffle(216)
            self.count_3 = self.riffle(720)
            self.count_4 = self.riffle(2160)
            self.count_5 = self.riffle(7200)
            self.count_6 = self.riffle(72000)

            porcent = self.guess()

            #   insere as informações na tabela
            self.table.insertRow(self.table.rowCount())
            self.table.setItem(i, 0, QTableWidgetItem("".join(self.word)))
            self.table.setItem(i, 1, QTableWidgetItem(str(self.count_1)))
            self.table.setItem(i, 2, QTableWidgetItem(str(self.count_2)))
            self.table.setItem(i, 3, QTableWidgetItem(str(self.count_3)))
            self.table.setItem(i, 4, QTableWidgetItem(str(self.count_4)))
            self.table.setItem(i, 5, QTableWidgetItem(str(self.count_5)))
            self.table.setItem(i, 6, QTableWidgetItem(str(self.count_6)))
            self.table.setItem(i, 7, QTableWidgetItem(str(porcent)))

#   start
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
