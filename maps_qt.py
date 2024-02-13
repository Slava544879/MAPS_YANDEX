from PyQt5 import QtWidgets, QtGui
import os
import sqlite3
import base64
import shutil
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton,
                             QVBoxLayout, QComboBox, QTableWidget, QTableWidgetItem)
import sys
import random
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import requests
import sqlite3
import pyautogui
connect = sqlite3.connect('maps.sqlite')
cursor = connect.cursor()


class MAPS(QMainWindow):
    def __init__(self, ):
        super().__init__()
        self.resize(820, 800)

        self.lbl = QLabel(self)
        self.lbl.resize(650, 450)
        self.pix = QtGui.QPixmap('map.png')
        self.lbl.setPixmap(self.pix)
        self.lbl.move(75, 350)

        self.map_look = 'map'
        self.mashtab_sp = [90, 40, 10, 5, 3, 1]

        layout = QVBoxLayout()

        self.parameterSelection = QComboBox(self)
        self.parameterSelection.resize(100, 30)
        self.parameterSelection.addItem("схема")
        self.parameterSelection.addItem("спутник")
        self.parameterSelection.addItem("гибрид")
        self.parameterSelection.move(10, 10)
        self.parameterSelection.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")

        self.name_label = QLabel('Название:', self)
        self.name_label.resize(100, 30)
        self.name_label.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.name_label.move(120, 10)

        self.name_object = QLineEdit(self)
        self.name_object.resize(565, 30)
        self.name_object.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.name_object.move(225, 10)

        self.coords_label = QLabel('Координаты:', self)
        self.coords_label.resize(120, 30)
        self.coords_label.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.coords_label.move(120, 65)

        self.coords_1 = QLineEdit(self)
        self.coords_1.resize(270, 30)
        self.coords_1.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.coords_1.move(245, 65)

        self.coords_2 = QLineEdit(self)
        self.coords_2.resize(270, 30)
        self.coords_2.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.coords_2.move(520, 65)

        self.left = QPushButton("LEFT", self)
        self.left.resize(140, 30)
        self.left.move(75, 300)
        self.left.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.left.clicked.connect(self.smeshenie)

        self.up = QPushButton("UP", self)
        self.up.resize(140, 30)
        self.up.move(245, 300)
        self.up.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.up.clicked.connect(self.smeshenie)

        self.down = QPushButton("DOWN", self)
        self.down.resize(140, 30)
        self.down.move(415, 300)
        self.down.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.down.clicked.connect(self.smeshenie)

        self.right = QPushButton("RIGHT", self)
        self.right.resize(140, 30)
        self.right.move(585, 300)
        self.right.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.right.clicked.connect(self.smeshenie)

        self.plus = QPushButton("+", self)
        self.plus.resize(50, 50)
        self.plus.move(750, 500)
        self.plus.setStyleSheet("color: rgb(0, 0, 0); font: bold 35px;")
        self.plus.clicked.connect(self.plus_minus)

        self.minus = QPushButton("-", self)
        self.minus.resize(50, 50)
        self.minus.move(750, 575)
        self.minus.setStyleSheet("color: rgb(0, 0, 0); font: bold 35px;")
        self.minus.clicked.connect(self.plus_minus)

        self.poisk_object = QPushButton("Поиск", self)
        self.poisk_object.resize(100, 30)
        self.poisk_object.move(700, 250)
        self.poisk_object.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.poisk_object.clicked.connect(self.poisk)

        self.poisk_delete = QPushButton("Сброс поискового результата", self)
        self.poisk_delete.resize(300, 30)
        self.poisk_delete.move(10, 250)
        self.poisk_delete.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.poisk_delete.clicked.connect(self.poisk_del)

        self.metka_del_all = QPushButton("удалить все метки", self)
        self.metka_del_all.resize(300, 30)
        self.metka_del_all.move(10, 210)
        self.metka_del_all.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.metka_del_all.clicked.connect(self.poisk_del)

        self.metka_set = QPushButton("поставить метку", self)
        self.metka_set.resize(200, 30)
        self.metka_set.move(350, 210)
        self.metka_set.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.metka_set.clicked.connect(self.poisk_del)

        self.metka_del = QPushButton("удалить метку", self)
        self.metka_del.resize(200, 30)
        self.metka_del.move(350, 250)
        self.metka_del.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.metka_del.clicked.connect(self.poisk_del)

        self.mashtab_label = QLabel('Масштаб:', self)
        self.mashtab_label.resize(120, 30)
        self.mashtab_label.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.mashtab_label.move(120, 110)

        self.mashtab = QLineEdit('10', self)
        self.mashtab.resize(270, 30)
        self.mashtab.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.mashtab.move(245, 110)

        self.adres_label = QLabel('Адрес:', self)
        self.adres_label.resize(120, 30)
        self.adres_label.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.adres_label.move(120, 150)

        self.adres = QLineEdit(self)
        self.adres.resize(535, 30)
        self.adres.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.adres.move(245, 150)

        self.checkbox = QCheckBox('Почтовый индекс', self)
        self.checkbox.resize(270, 20)
        self.checkbox.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.checkbox.move(530, 100)
        self.checkbox.setChecked(False)

        self.checkbox_m = QCheckBox('Ставить метки автоматически', self)
        self.checkbox_m.resize(270, 20)
        self.checkbox_m.setStyleSheet("color: rgb(0, 0, 0); font: bold 15px;")
        self.checkbox_m.move(530, 125)
        self.checkbox_m.setChecked(False)

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_PageUp:
                if float(self.mashtab.text()) > 1:
                    for i in self.mashtab_sp:
                        if float(self.mashtab.text()) > i:
                            self.mashtab.setText(str(i))
                            break
                else:
                    self.mashtab.setText(str(float(self.mashtab.text()) / 2))
                self.poisk()
            elif event.key() == Qt.Key_PageDown:
                if float(self.mashtab.text()) < 90:
                    if float(self.mashtab.text()) >= 1:
                        for i in self.mashtab_sp[::-1]:
                            if float(self.mashtab.text()) < i:
                                self.mashtab.setText(str(i))
                                break
                    else:
                        self.mashtab.setText(str(float(self.mashtab.text()) * 2))
                else:
                    self.mashtab.setText(str(90))
                self.poisk()
        except:
            pass

    def smeshenie(self):
        smeshenie = self.sender().text()
        try:
            if str(smeshenie) == 'LEFT':
                if float(self.coords_1.text()) - float(self.mashtab.text()) >= -180:
                    self.coords_1.setText(str(float(self.coords_1.text()) - float(self.mashtab.text())))
            elif str(smeshenie) == 'RIGHT':
                if float(self.coords_1.text()) + float(self.mashtab.text()) <= 179:
                    self.coords_1.setText(str(float(self.coords_1.text()) + float(self.mashtab.text())))
            elif str(smeshenie) == 'UP':
                if float(self.coords_2.text()) + float(self.mashtab.text()) <= 85:
                    self.coords_2.setText(str(float(self.coords_2.text()) + float(self.mashtab.text())))
            elif str(smeshenie) == 'DOWN':
                if float(self.coords_2.text()) + float(self.mashtab.text()) >= -84:
                    self.coords_2.setText(str(float(self.coords_2.text()) - float(self.mashtab.text())))
            self.name_object.setText('')
            self.poisk()
        except:
            pass

    def plus_minus(self):
        smeshenie = self.sender().text()
        try:
            if str(smeshenie) == '+':
                if float(self.mashtab.text()) > 1:
                    for i in self.mashtab_sp:
                        if float(self.mashtab.text()) > i:
                            self.mashtab.setText(str(i))
                            break
                else:
                    self.mashtab.setText(str(float(self.mashtab.text()) / 2))
            elif str(smeshenie) == '-':
                if float(self.mashtab.text()) < 90:
                    if float(self.mashtab.text()) >= 1:
                        for i in self.mashtab_sp[::-1]:
                            if float(self.mashtab.text()) < i:
                                self.mashtab.setText(str(i))
                                break
                    else:
                        self.mashtab.setText(str(float(self.mashtab.text()) * 2))
                else:
                    self.mashtab.setText(str(90))
            self.poisk()
        except:
            pass

    def poisk_del(self):
        smeshenie = self.sender().text()
        try:
            if str(smeshenie) == 'удалить метку':
                cursor.execute("DELETE FROM near WHERE name=?", (str(self.name_object.text()),))
                connect.commit()
            elif str(smeshenie) == 'удалить все метки':
                for i in cursor.execute("SELECT coords FROM near").fetchall():
                    cursor.execute("DELETE FROM near WHERE coords=?", (str(i[0]),))
                    connect.commit()
            elif str(smeshenie) == 'поставить метку':
                if len(self.coords_1.text()) != 0 and len(self.coords_2.text()) != 0 and len(self.mashtab.text()) != 0:
                    flag = True
                    for i in cursor.execute("SELECT name, coords FROM near").fetchall():
                        if str(i[0]) == str(self.object) and \
                                str(i[1]) == str(f'{self.coords1} {self.coords2}'):
                            flag = False
                    if flag:
                        cursor.execute(
                            """INSERT OR IGNORE INTO near (name, coords) VALUES (?, ?)""", (
                                str(self.object), str(f'{self.coords1} {self.coords2}')))
                        connect.commit()
            elif str(smeshenie) == 'Сброс поискового результата':
                self.adres.setText('')
                self.name_object.setText('')
                self.coords_1.setText('')
                self.mashtab.setText('')
                self.coords_2.setText('')
            self.poisk()
        except:
            pass

    def poisk(self):
        parameter = self.parameterSelection.currentText()
        if parameter == 'схема':
            self.map_look = 'map'
        elif parameter == 'спутник':
            self.map_look = 'sat'
        elif parameter == 'гибрид':
            self.map_look = 'sat,skl'
        try:
            if len(self.name_object.text()) != 0:
                geo = f"http://geocode-maps.yandex.ru/" \
                      f"1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b" \
                      f"&geocode={self.name_object.text()}&format=json"
                response = requests.get(geo)
                if response:
                    json_response = response.json()
                    toponym = \
                        json_response["response"]["GeoObjectCollection"][
                            "featureMember"][0]["GeoObject"]
                    toponym_coodrinates = toponym["Point"]["pos"]
                    self.coords_1.setText(toponym_coodrinates.split()[0])
                    self.coords_2.setText(toponym_coodrinates.split()[1])
                    if len(self.mashtab.text()) == 0:
                        self.mashtab.setText(str(10))
                    if self.checkbox_m.isChecked():
                        try:
                            flag = True
                            for i in cursor.execute("SELECT name, coords FROM near").fetchall():
                                if str(i[0]) == str(self.name_object.text()) and \
                                        str(i[1]) == str(f'{self.coords_1.text()} {self.coords_2.text()}'):
                                    flag = False
                            if flag:
                                cursor.execute(
                                    """INSERT OR IGNORE INTO near (name, coords) VALUES (?, ?)""", (
                                        str(self.name_object.text()), str(f'{self.coords_1.text()}'
                                                                          f' {self.coords_2.text()}')))
                                connect.commit()
                        except:
                            pass
                    if self.checkbox.isChecked():
                        try:
                            index_postal = json_response["response"]["GeoObjectCollection"]["featureMember"][0][
                                "GeoObject"]["metaDataProperty"]["GeocoderMetaData"]['Address']['postal_code']
                            self.adres.setText(f"{toponym['metaDataProperty']['GeocoderMetaData']['text']};"
                                               f" почтовый индекс: {index_postal}")
                        except:
                            self.adres.setText(f"{toponym['metaDataProperty']['GeocoderMetaData']['text']}")
                    else:
                        self.adres.setText(f"{toponym['metaDataProperty']['GeocoderMetaData']['text']}")
            if len(self.coords_1.text()) != 0 and len(self.coords_2.text()) != 0:
                text = '&pt='
                for i in cursor.execute("SELECT coords FROM near").fetchall():
                    text += f'{str(i[0]).split()[0]},{str(i[0]).split()[1]},pm2rdm~'
                if len(text) == 4:
                    text = ''
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={float(self.coords_1.text())}," \
                              f"{float(self.coords_2.text())}&scale=1&z=9&size=650,450{text[:-1]}" \
                              f"&spn=0.00000000000000001,{self.mashtab.text()}&l={self.map_look}"
                response = requests.get(map_request)
                if not response:
                    pass
                else:
                    map_file = "map.png"
                    with open(map_file, "wb") as file:
                        file.write(response.content)
                    file.close()
                    self.pix = QtGui.QPixmap('map.png')
                    self.lbl.setPixmap(self.pix)
        except:
            pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MAPS()
    window.show()
    sys.exit(app.exec_())