import sys

from PyQt5 import QtGui
import openweather
import others
from PyQt5.QtGui import QBrush, QImage, QPainter, QPainterPath, QPalette, QPen, QPixmap, QColor
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMenu,QWidget,QLabel,QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

#Programer: Craciun Mihai
#Purpose: Experimentare PyQt5

#TO DO : Set Up Menu button and try too add more others.py faetures

class WeatherWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(1000,500))
        self.setWindowTitle("OpenWeather App")

        openweather.getWeatherInfo(city)

        #Have no goddam idea how this works but it does soo we no change
        font = self.font()
        font.setPointSize(20)

        # Bruh i have depresion i cant i am dying i think after this i need a phycologist
        oImage = QImage("zackground.png")
        sImage = oImage.scaled(QSize(1000,500))
        pallete = QPalette()
        pallete.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(pallete)


        self.cityLabel = QLabel(self)
        self.cityLabel.setText(city)
        self.cityLabel.setFont(font)
        self.cityLabel.adjustSize()
        self.cityLabel.move(340,180)

        font.setPointSize(20)
        self.temperatureLabel = QLabel(self)
        self.temperatureLabel.setText(str(openweather.current_temperature_celsius) + "°C")
        self.temperatureLabel.setFont(font)
        self.temperatureLabel.adjustSize()
        self.temperatureLabel.move(540,180)

        font.setPointSize(16)
        self.descLabel = QLabel(self)
        self.descLabel.setText(str(openweather.weather_description).capitalize())
        self.descLabel.setFont(font)
        self.descLabel.adjustSize()
        self.descLabel.move(380,220)

        font.setPointSize(72)
        self.TimeLabel = QLabel(self)
        self.TimeLabel.setFont(font)
        others.wTime()
        self.TimeLabel.setText(str(others.h) + ":" + str(others.m1))
        self.TimeLabel.adjustSize()
        self.TimeLabel.move(350,85)
        self.TimeLabel.setMaximumSize(QSize(241,90))

        font.setPointSize(12)
        self.HumLabel = QLabel(self)
        self.HumLabel.setFont(font)
        self.HumLabel.setText("Current humidity is: " + str(openweather.current_humidiy) + "%")
        self.HumLabel.adjustSize()
        self.HumLabel.move(10,440)

        self.AthmLabel = QLabel(self)
        self.AthmLabel.setFont(font)
        self.AthmLabel.setText("Current athmoseferic pressure is: " + str(openweather.current_pressure) + "hPa")
        self.AthmLabel.adjustSize()
        self.AthmLabel.move(10,470)

        self.PixMap = QLabel(self)
        if (openweather.weather_description == "clear sky"):
            self.PixMap.setPixmap(QPixmap("clear_sky.png"))
        elif (openweather.weather_description == "few clouds"):
            self.PixMap.setPixmap(QPixmap("few_clouds.png"))
        elif (openweather.weather_description == "scattered clouds"):
            self.PixMap.setPixmap(QPixmap("scattered_clouds.png"))
        elif (openweather.weather_description == "broken clouds"):
            self.PixMap.setPixmap(QPixmap("broken_clouds.png"))
        elif (openweather.weather_description == "shower rain"):
            self.PixMap.setPixmap(QPixmap("shower_rain.png"))
        elif (openweather.weather_description == "rain"):
            self.PixMap.setPixmap(QPixmap("rain.png"))
        elif (openweather.weather_description == "thunderstorm"):
            self.PixMap.setPixmap(QPixmap("thunderstorm.png"))
        elif (openweather.weather_description == "snow"):
            self.PixMap.setPixmap(QPixmap("snow.png"))
        elif (openweather.weather_description == "mist"):
            self.PixMap.setPixmap(QPixmap("mist.png"))
        
        self.PixMap.hasScaledContents()
        self.PixMap.move(600,170)

        MainMenu = QMenu(self)

        MainMenu.addAction("Arduino", self.MenuArduino)
        MainMenu.addAction("Refresh", self.MenuRefresh)

        self.MenuButt = QPushButton("Menu",self)
        self.MenuButt.move(0,0)
        self.MenuButt.setMenu(MainMenu)
        
    def MenuArduino(self):
        others.connectArduino('COM3')
        others.AnalogRead(0)
        print(others.analogval)
    def MenuRefresh(self):
        print("sugi sa mor io")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.w = None #Verificare pt ferestre externe chestie

        self.setMinimumSize(QSize(1000,500))
        self.setWindowTitle("WeatherApp v0")

        self.intLabel = QLabel(self)
        self.intLabel.setText("Welcome to OpenWether GUI v0")
        self.intLabel.adjustSize()
        self.intLabel.move(380,0)

        self.lineLabel = QLabel(self)
        self.lineLabel.setText("Please insert city:")
        self.lineLabel.adjustSize()
        self.lineLabel.move(315,58)

        self.cityLine = QLineEdit(self)
        self.cityLine.setMaxLength(85)
        self.cityLine.move(440,50)
        self.cityLine.resize(250,35)

        cityBut = QPushButton("Submit",self)
        cityBut.clicked.connect(self.clickAction)
        cityBut.move(450,100)

    def clickAction(self):
        # Submit Button functie de activare
        global city
        city = self.cityLine.text()
        if self.w is None:
            self.w = WeatherWindow()
        self.w.show()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
        