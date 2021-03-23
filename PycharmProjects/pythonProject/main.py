# This is a sample Python script.
import Enclave
from PyQt5 import QtWidgets , QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class window(QMainWindow):

    def __init__(self):
        super(window,self).__init__()
        self.setGeometry(200,200,700,700)
        self.setWindowTitle("AutoEnclave")
        #Objeto Enclave
        self.EnclaveBog = Enclave.Enclave(16, 0, 1, 0.74, 0.46)

        # CreacionBoton1
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Abrir")
        self.b1.clicked.connect(self.abrirEnc)
        self.b1.move(40,85)

        #Creacion ImagenAutoClave
        self.l2 = QtWidgets.QLabel(self)
        self.pixmap1 = QtGui.QPixmap("AutoClaveCerrado.png")
        self.pixmap2 = QtGui.QPixmap("AutoClaveAbierto.png")
        self.l2.setGeometry(180, 150, 500, 400)
        self.l2.setPixmap(self.pixmap1)
        self.l2.setAlignment(Qt.AlignCenter)

        # CreacionBoton2
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Cerrar")
        self.b2.clicked.connect(self.cerrarEnc)
        self.b2.move(40, 125)

        # CreacionLabel
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText("Puerta:")
        self.l1.setAlignment(Qt.AlignLeft)
        self.l1.setFont(QtGui.QFont('SansSerif',12))
        self.l1.move(20,50)

        # CreacionLabel
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText("Temperatura:")
        self.l3.setAlignment(Qt.AlignLeft)
        self.l3.setFont(QtGui.QFont('SansSerif', 12))
        self.l3.setGeometry(20,180,110,100)

        #CreacionTextBoxTemp
        self.tb1 = QtWidgets.QLineEdit(self)
        self.tb1.setGeometry(90,208,50,20)

        # CreacionBoton2
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Ok.")
        self.b3.clicked.connect(self.cambioTemp)
        self.b3.setGeometry(60,230,60,20)

        # CreacionLabel
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText("SetTemp:")
        self.l3.setAlignment(Qt.AlignLeft)
        self.l3.setFont(QtGui.QFont('SansSerif', 8))
        self.l3.setGeometry(35,210,100,20)

        #Progress Bar
        self.pb = QtWidgets.QProgressBar(self)
        self.pb.setGeometry(65,280,50,200)
        self.pb.setValue((self.EnclaveBog.temperature/150)*100)
        self.pb.setOrientation(Qt.Vertical)

        # CreacionLabel
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText("150°C")
        self.l4.setAlignment(Qt.AlignLeft)
        self.l4.setFont(QtGui.QFont('SansSerif', 6))
        self.l4.setGeometry(75, 270, 50, 20)

        #CreacionBCD
        self.BCD = QtWidgets.QLCDNumber(self)
        self.BCD.setGeometry(50,490,50,60)
        self.BCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.BCD.display(self.EnclaveBog.temperature)
        self.BCD.setDigitCount(5)

        # CreacionLabel
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText("°C")
        self.l5.setAlignment(Qt.AlignLeft)
        self.l5.setFont(QtGui.QFont('SansSerif', 16))
        self.l5.setGeometry(100, 508, 100, 100)

        # CreacionLabel
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText("Presion:")
        self.l6.setAlignment(Qt.AlignLeft)
        self.l6.setFont(QtGui.QFont('SansSerif', 12))
        self.l6.setGeometry(20, 560, 100, 50)

        self.BCD1 = QtWidgets.QLCDNumber(self)
        self.BCD1.setGeometry(50, 590, 50, 60)
        self.BCD1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.BCD1.display(self.EnclaveBog.pressure)
        self.BCD1.setDigitCount(5)

        # CreacionLabel
        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText("atm")
        self.l7.setAlignment(Qt.AlignLeft)
        self.l7.setFont(QtGui.QFont('SansSerif', 16))
        self.l7.setGeometry(105, 610, 100, 100)

        # CreacionLabel
        self.l8 = QtWidgets.QLabel(self)
        self.l8.setText("SetPress:")
        self.l8.setAlignment(Qt.AlignLeft)
        self.l8.setFont(QtGui.QFont('SansSerif', 8))
        self.l8.setGeometry(170,610, 100, 20)

        self.tb2 = QtWidgets.QLineEdit(self)
        self.tb2.setGeometry(225,608, 50, 20)

        # CreacionBoton2
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Ok.")
        self.b4.clicked.connect(self.cambioPress)
        self.b4.setGeometry(200,630, 60, 20)

        # CreacionLabel
        self.l9 = QtWidgets.QLabel(self)
        self.l9.setText("Humedad:")
        self.l9.setAlignment(Qt.AlignLeft)
        self.l9.setFont(QtGui.QFont('SansSerif', 12))
        self.l9.setGeometry(320, 560, 100, 50)

        self.BCD2 = QtWidgets.QLCDNumber(self)
        self.BCD2.setGeometry(350, 590, 50, 60)
        self.BCD2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.BCD2.display(self.EnclaveBog.humidity*100)
        self.BCD2.setDigitCount(5)

        # CreacionLabel
        self.l10 = QtWidgets.QLabel(self)
        self.l10.setText("%")
        self.l10.setAlignment(Qt.AlignLeft)
        self.l10.setFont(QtGui.QFont('SansSerif', 16))
        self.l10.setGeometry(405, 610, 100, 100)

        # CreacionLabel
        self.l11 = QtWidgets.QLabel(self)
        self.l11.setText("SetHum:")
        self.l11.setAlignment(Qt.AlignLeft)
        self.l11.setFont(QtGui.QFont('SansSerif', 8))
        self.l11.setGeometry(470,610, 100, 20)

        self.tb3 = QtWidgets.QLineEdit(self)
        self.tb3.setGeometry(525,608, 50, 20)

        # CreacionBoton2
        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setText("Ok.")
        self.b5.clicked.connect(self.cambioHum)
        self.b5.setGeometry(500,630, 60, 20)

        self.l12 = QtWidgets.QLabel(self)
        self.l12.setText("¡Alarma Temp!")
        self.l12.setAlignment(Qt.AlignLeft)
        self.l12.setFont(QtGui.QFont('SansSerif', 12))
        self.l12.setGeometry(200,20, 150, 20)

        self.l13 = QtWidgets.QLabel(self)
        self.l13.setAlignment(Qt.AlignCenter)
        self.l13.setGeometry(205, 30, 100,100)
        self.pixmap3 = QtGui.QPixmap("Alarma.png")

        self.timer = QTimer()
        self.timer.timeout.connect(self.alarmTemp)
        self.timer.timeout.connect(self.alarmPress)
        self.timer.start(100)

        self.l14 = QtWidgets.QLabel(self)
        self.l14.setText("¡Alarma Press!")
        self.l14.setAlignment(Qt.AlignLeft)
        self.l14.setFont(QtGui.QFont('SansSerif', 12))
        self.l14.setGeometry(400, 20, 150, 20)

        self.l15 = QtWidgets.QLabel(self)
        self.l15.setAlignment(Qt.AlignCenter)
        self.l15.setGeometry(405, 30, 100, 100)



    def alarmPress(self):
        if (self.EnclaveBog.temperature >= 100):
            self.l13.setPixmap(self.pixmap3)
        else:
            self.l13.clear()
        self.update()

    def alarmTemp(self):
        if (self.EnclaveBog.pressure >= 5):
            self.l15.setPixmap(self.pixmap3)
        else:
            self.l15.clear()
        self.update()


    def cambioHum(self):
        input = self.tb3.text()
        input2 = float(input)
        self.BCD2.display(input2*100)
        self.EnclaveBog.sethumidity(input2)
        self.update()

    def cambioPress(self):
        input = self.tb2.text()
        input2 = float(input)
        self.BCD1.display(input2)
        self.EnclaveBog.setPressure(input2)
        self.update()

    def cambioTemp(self):
        input = self.tb1.text()
        input2 = float(input)
        self.BCD.display(input2)
        self.EnclaveBog.setTemp(input2)
        self.pb.setValue((input2/150)*100)
        self.update()

    def cerrarEnc(self):
        if self.EnclaveBog.close == 0:
            self.l2.setPixmap(self.pixmap1)
        self.EnclaveBog.cerrar()
        self.update()

    def abrirEnc(self):
        if self.EnclaveBog.open == 0:
            self.l2.setPixmap(self.pixmap2)
        self.EnclaveBog.abrir()
        self.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    wind = window()
    wind.show()
    sys.exit(app.exec())