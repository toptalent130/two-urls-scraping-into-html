import sys
from PyQt5.QtWidgets import QApplication, QCalendarWidget, QMainWindow, QLabel, QComboBox, QPushButton, QWidget
from PyQt5.QtCore import QDate
from datetime import datetime
import calendar
from engine import GetDataFrom
from pytz import timezone
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import threading

class RequestUI(QMainWindow):

    def __init__(self):
        super().__init__()

        armenia = timezone('Asia/Yerevan')
        month = datetime.now(tz=armenia).month
        day = datetime.now(tz=armenia).day
        if month < 10:
            month = "0" + str(month)
        else:
            month = str(month)
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)
        date = month +  day

        # default values
        self.horse = "horse"
        self.track = "BEL"
        self.date = date

        # combo box
        combo = QComboBox(self)
        
        combo.move(70, 50)
        combo.addItem("horse")
        combo.addItem("dam")
        # combo.addItem("sire")
        by = QLabel(self)
        by.setText("By Name: ")
        by.move(20, 50)
        combo.activated[str].connect(self.onChangedByHorse)

        # calendar
        calendar = QCalendarWidget(self)
        calendar.setGeometry(200, 50, 450, 300)
        calendar.setGridVisible(True)
        calendar.clicked.connect(self.onChangedDate)

        # tracks
        combo1 = QComboBox(self)
        combo1.addItem("BEL")
        combo1.addItem("SAR")
        combo1.addItem("AQU")
        combo1.addItem("CD")
        combo1.addItem("KEE")
        combo1.addItem("GP")
        combo1.addItem("OP")
        combo1.addItem("AP")
        combo1.addItem("SA")
        combo1.addItem("PIM")
        combo1.addItem("PRX")
        combo1.move(730, 50)
        by1 = QLabel(self)
        by1.setText("By Track: ")
        by1.move(680, 50)
        combo1.activated[str].connect(self.onChangedByTrack)

        # submit
        button = QPushButton('Send Request', self)
        button.setToolTip('send request to web browser')
        button.move(100, 70)
        button.setGeometry(350, 400, 150, 40)
        button.clicked.connect(self.clickedOnSubmit)

        # show ui
        self.setGeometry(50, 50, 900, 500)
        self.setWindowTitle("Five Pedigrees")
        self.show()

    def onChangedDate(self, qDate):
        month_to_num = [("Jan", "01"), ("Feb", "02"), ("Mar", "03"), ("Apr", "04"), ("May", "05"), ("Jun", "06"),
                        ("Jul", "07"), ("Aug", "08"), ("Sep", "09"), ("Oct", "10"), ("Nov", "11"), ("Dec", "12")]
        month = ""
        day = qDate.toString().split(" ")[2]
        for each in month_to_num:
            if each[0] == qDate.toString().split(" ")[1]:
                month = each[1]
        if int(qDate.toString().split(" ")[2]) < 10:
            day = "0" + qDate.toString().split(" ")[2]
        self.date = month + day

    def onChangedByHorse(self, text):
        self.horse = text
        print(self.horse)

    def onChangedByTrack(self, text):
        self.track = text

    def clickedOnSubmit(self):
        print(self.horse)
        driver1 = webdriver.Chrome(ChromeDriverManager().install())
        driver2 = webdriver.Chrome(ChromeDriverManager().install())
        self.t1 = threading.Thread(target=GetDataFrom,args=[driver1, driver2, self.date, self.horse, self.track],daemon=True)
        self.t1.start()
