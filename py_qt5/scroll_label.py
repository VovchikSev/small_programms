'''
скроллирование метки
http://opython.blogspot.com/2017/07/python-pyqt5-pyqt5-example.html
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
'''
QWidget - это базовый класс для всех объектов интерфейса пользователя в PyQt5
QApplication - каждое приложение написанное на PyQt5 должно создать объект приложения.
QLabel - текстовая метка.
QPushButton - позволяет создавать кнопки.
QTimer - таймер.
'''

'''
Само приложение содержит всего один класс.
Для начала рассмотрим ту часть в которой происходит инициализация интерфейса.
В приведенном ниже коде я постарался дать подробные коментарии:
'''
LEFT = 'влево'
RIGHT = 'вправо'
STOP = 'STOP'

class myApp(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.init_iu()  # вызов метода в котором задается интерфейс и начальные параметры
    
    def init_iu(self):
        self.speed = 10  # каждые 10 мс будет обновляться таймер
        self.timer = QTimer(self)  # создаем таймер
        # объявление кнопок
        btn_left = QPushButton(LEFT, self)  # создаем кнопку "влево"
        btn_right = QPushButton(RIGHT, self)  # создаем кнопку "вправо"
        btn_stop =QPushButton(STOP, self)  # создаем кнопку "стоп"
        # абсолютное позиционирование кнопок
        btn_left.move(10, 10)
        btn_right.move(350, 10)
        btn_stop.move(180, 10)

        # создание и настройка окна приложения
        self.setWindowTitle('бегущая строка')
        self.setGeometry(300, 300, 450, 300)

        # начальные координаты надписи (бегущей строки) путем указания координат x и y
        self.x = 200
        self.y = 150
        
        # создание метки содержащей текст для прокрутки.
        self.label = QLabel("Бегущфа строка", self)
        self.label.move(self.x, self.y)

        # подключить сигнал кнопок clicked к методу buttonClicked
        btn_left.clicked.connect(self.buttonClicked)
        btn_right.clicked.connect(self.buttonClicked)
        btn_stop.clicked.connect(self.buttonClicked)

        self.show()


    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == RIGHT:
            if self.timer.isActive():
                self.timer.stop()
                self.timer.timeout.disconnect()
                # перенести в общую часть и убрать else                
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_right)
            else:
                self.timer.start(self.speed)
                self.timer.timeout.connect(self.move_label_right)
                

        elif sender.text() == LEFT:
            if self.timer.isActive():
                self.timer.stop()
                self.timer.timeout.disconnect()
                # перенести в общую часть и убрать else                
            
            self.timer.start(self.speed)
            self.timer.timeout.connect(self.move_label_left)
            
        elif sender.text() ==  STOP:
            self.stop_move()

    def move_label_left(self):
        if self.x == -100:
            self.x = 500
        
        self.x -= 0.5
        self.label.move(self.x, self.y)


    def move_label_right(self):
        if self.x == 500:
            self.x = -100
        
        self.x += 0.5
        self.label.move(self.x, self.y)


    def stop_move(self):
        if self.timer.isActive:
            self.timer.stop()
            self.timer.timeout.disconect()


app = QApplication(sys.argv)
ex = myApp()
sys.exit(app.exec_())