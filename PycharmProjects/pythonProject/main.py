# This is a sample Python script.
from serial import Serial
import Autoclave
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from datetime import datetime

class window(QMainWindow):
    def __init__(self):
        # Variables de ajuste
        t_printData=1000  #Periodo de recolección de datos en milisegundos
        self.Temp_maxima=100 # Temperatura máxima en grados centígrados
        self.Pressure_maxima=5 # Presión máxima en atm
        self.guardarDatos="memoria.txt" # Nombre del archivo en el que se va a guardar el registro
        # Inicio del código
        # Se configuran las dimensiones de la pantalla principal
        super(window,self).__init__()
        self.setGeometry(200,200,700,700)
        self.setWindowTitle("Autoclave")
        #Objeto Autoclave es instanceado
        self.AutoclaveBog = Autoclave.Autoclave(16, 0, 1, 0.74, 0.46)
        # CreacionBoton1 para abrir
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Abrir")
        self.b1.clicked.connect(self.abrirEnc)
        self.b1.move(40,85)
        #Creacion Imagen AutoClave
        self.l2 = QtWidgets.QLabel(self)
        self.pixmap1 = QtGui.QPixmap("AutoClaveCerrado.png")
        self.pixmap2 = QtGui.QPixmap("AutoClaveAbierto.png")
        self.l2.setGeometry(180, 150, 500, 400)
        self.l2.setPixmap(self.pixmap1)
        self.l2.setAlignment(Qt.AlignCenter)
        # CreacionBoton2 para cerrar el autoclave
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Cerrar")
        self.b2.clicked.connect(self.cerrarEnc)
        self.b2.move(40, 125)
        # CreacionLabel para la puerta
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText("Puerta:")
        self.l1.setAlignment(Qt.AlignLeft)
        self.l1.setFont(QtGui.QFont('SansSerif',12))
        self.l1.move(20,50)
        # CreacionLabel para la temperatura
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText("Temperatura:")
        self.l3.setAlignment(Qt.AlignLeft)
        self.l3.setFont(QtGui.QFont('SansSerif', 12))
        self.l3.setGeometry(20,180,110,100)
            #CreacionTextBoxTemp que permite captar la información deseada.
        self.tb1 = QtWidgets.QLineEdit(self)
        self.tb1.setGeometry(90,208,50,20)
            # CreacionBoton2 Permite capturar la información de la temperatura. 
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("Ok.")
        self.b3.clicked.connect(self.cambioTemp)
        self.b3.setGeometry(60,230,60,20)
        # CreacionBoton4 para reiniciar el registro de información
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Reiniciar registro")
        self.b4.clicked.connect(self.reiniciarRegistro)
        self.b4.setGeometry(300, 120, 150, 30)
        
        

        # CreacionLabel para configurar la tempertatura
        self.l3 = QtWidgets.QLabel(self)
        self.l3.setText("SetTemp:")
        self.l3.setAlignment(Qt.AlignLeft)
        self.l3.setFont(QtGui.QFont('SansSerif', 8))
        self.l3.setGeometry(35,210,50,20)

        #Progress Bar es un indicativo de la temperatura.
        self.pb = QtWidgets.QProgressBar(self)
        self.pb.setGeometry(65,280,50,200)
        self.pb.setValue((self.AutoclaveBog.temperature/150)*100)
        self.pb.setOrientation(Qt.Vertical)

        # CreacionLabel Indica la tempertarura máxima que puede alcanzar.
        self.l4 = QtWidgets.QLabel(self)
        self.l4.setText("150 " +str(chr(176)) + "C")
        self.l4.setAlignment(Qt.AlignLeft)
        self.l4.setFont(QtGui.QFont('SansSerif', 6))
        self.l4.setGeometry(75, 270, 50, 20)

        #CreacionBCD
        self.BCD = QtWidgets.QLCDNumber(self)
        self.BCD.setGeometry(50,490,50,60)
        self.BCD.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.BCD.display(self.AutoclaveBog.temperature)
        self.BCD.setDigitCount(5)

        # CreacionLabel para grados centígrados
        self.l5 = QtWidgets.QLabel(self)
        self.l5.setText(str(chr(176)) + "C")
        self.l5.setAlignment(Qt.AlignLeft)
        self.l5.setFont(QtGui.QFont('SansSerif', 16))
        self.l5.setGeometry(100, 508, 100, 100)

        # CreacionLabel, se muestra presión en la ventana
        self.l6 = QtWidgets.QLabel(self)
        self.l6.setText("Presi"+str(chr(243))+"n: ")
        self.l6.setAlignment(Qt.AlignLeft)
        self.l6.setFont(QtGui.QFont('SansSerif', 12))
        self.l6.setGeometry(20, 560, 100, 50)

        self.BCD1 = QtWidgets.QLCDNumber(self)
        self.BCD1.setGeometry(50, 590, 50, 60)
        self.BCD1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.BCD1.display(self.AutoclaveBog.pressure)
        self.BCD1.setDigitCount(5)
        
    
        # CreacionLabel para unidades de la presióñ
        self.l7 = QtWidgets.QLabel(self)
        self.l7.setText("atm")
        self.l7.setAlignment(Qt.AlignLeft)
        self.l7.setFont(QtGui.QFont('SansSerif', 16))
        self.l7.setGeometry(105, 610, 100, 100)

        # CreacionLabel para indicar el lugar de configurar la presión.
        self.l8 = QtWidgets.QLabel(self)
        self.l8.setText("SetPress:")
        self.l8.setAlignment(Qt.AlignLeft)
        self.l8.setFont(QtGui.QFont('SansSerif', 8))
        self.l8.setGeometry(170,610, 100, 20)
        
            # Se establece el lugar donde el texBox va a estar localizado
        self.tb2 = QtWidgets.QLineEdit(self)
        self.tb2.setGeometry(225,608, 50, 20)

            # Creacion Boton cambio de presión
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText("Ok.")
        self.b4.clicked.connect(self.cambioPress)
        self.b4.setGeometry(200,630, 60, 20)

        # Humedad Se crea la ventana en donde se ubica el indicativo para la humedad
        self.l9 = QtWidgets.QLabel(self)
        self.l9.setText("Humedad:")
        self.l9.setAlignment(Qt.AlignLeft)
        self.l9.setFont(QtGui.QFont('SansSerif', 12))
        self.l9.setGeometry(320, 560, 100, 50)

        self.BCD2 = QtWidgets.QLCDNumber(self)
        self.BCD2.setGeometry(350, 590, 50, 60)
        self.BCD2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.BCD2.display(self.AutoclaveBog.humidity*100)
        self.BCD2.setDigitCount(5)

        # CreacionLabel referente al porcentaje de la humedad.
        self.l10 = QtWidgets.QLabel(self)
        self.l10.setText("%")
        self.l10.setAlignment(Qt.AlignLeft)
        self.l10.setFont(QtGui.QFont('SansSerif', 16))
        self.l10.setGeometry(405, 610, 100, 100)

            # CreacionLabel se establece el lugar donde la humedad se va a configurar.
        self.l11 = QtWidgets.QLabel(self)
        self.l11.setText("SetHum:")
        self.l11.setAlignment(Qt.AlignLeft)
        self.l11.setFont(QtGui.QFont('SansSerif', 8))
        self.l11.setGeometry(470,610, 100, 20)
            # Se ubica el recuadro para obtener la información de la humedad.
        self.tb3 = QtWidgets.QLineEdit(self)
        self.tb3.setGeometry(525,608, 50, 20)
        
       
            # CreacionBoton2 para cambiar el valor de la humedad
        self.b5 = QtWidgets.QPushButton(self)
        self.b5.setText("Ok.")
        self.b5.clicked.connect(self.cambioHum)
        self.b5.setGeometry(500,630, 60, 20)

        # Alarmas de Temperatura
        self.l12 = QtWidgets.QLabel(self)
        self.l12.setText(str(chr(161)+"Alarma Temp"+str(chr(33))))
        self.l12.setAlignment(Qt.AlignLeft)
        self.l12.setFont(QtGui.QFont('SansSerif', 12))
        self.l12.setGeometry(200,20, 150, 20)

        self.l13 = QtWidgets.QLabel(self)
        self.l13.setAlignment(Qt.AlignCenter)
        self.l13.setGeometry(205, 30, 100,100)
        self.pixmap3 = QtGui.QPixmap("Alarma.png")

            # Se verificar cada 100 milisegundos el estado de las alarmas.
        self.timer = QTimer()
        self.timer.timeout.connect(self.alarmTemp)
        self.timer.timeout.connect(self.alarmPress)
        self.timer.start(100)
        
            # Se coloca un label para indicar que la alarma está presionada
        self.l14 = QtWidgets.QLabel(self)
        self.l14.setText(str(chr(161)+"Alarma Press"+str(chr(33))))
        self.l14.setAlignment(Qt.AlignLeft)
        self.l14.setFont(QtGui.QFont('SansSerif', 12))
        self.l14.setGeometry(400, 20, 150, 20)
        
        self.l15 = QtWidgets.QLabel(self)
        self.l15.setAlignment(Qt.AlignCenter)
        self.l15.setGeometry(405, 30, 100, 100)
        
        # Recolector de datos cada t_printData milisegundos.      
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.printData)
        self.timer2.start(t_printData)

        
        # Se verifica si la alarma de la presión se activa
    def alarmPress(self):
        if (self.AutoclaveBog.temperature >= self.Temp_maxima):
            self.l13.setPixmap(self.pixmap3)
        else:
            self.l13.clear()
        self.update()
        # Se verifica si la alarma de la temperatura está activada.
    def alarmTemp(self):
        if (self.AutoclaveBog.pressure >= self.Pressure_maxima):
            self.l15.setPixmap(self.pixmap3)
        else:
            self.l15.clear()
        self.update()
        
        # Esta función se encarga de recolectar el estado del autoclave 
    def printData(self):
        
        if self.AutoclaveBog.getTemp()>self.Temp_maxima:
            temMax=" :Si"
        else: temMax=" :No"
        
        
        if self.AutoclaveBog.getPressure()>self.Pressure_maxima:
            preMax=" :Si"
        else: preMax=" :No"
        
        
        
        now = datetime.now()
        data= str(now.year)+"/"+str(now.month)+"/"+str(now.day)+" "+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+\
        ", Estado: "+self.AutoclaveBog.getEstado() +\
        ", Temperatura: "+str(self.AutoclaveBog.getTemp()) + str(chr(176)) + "C"+\
        ", Presi"+str(chr(243))+"n: " +str(self.AutoclaveBog.getPressure())+" Atm "+\
        ", Humedad: "+str(self.AutoclaveBog.getHumidity())+" " + str(chr(37)) +\
        ", Temperatura "+ str(chr(62))+"= " + str(self.Temp_maxima) +temMax+\
        ", Presi"+str(chr(243))+"n " + str(chr(62))+"= " + str(self.Pressure_maxima) + preMax + "\n"
       
        self.escritura(data)
        print(data)
        self.update()
    
       #Realiza la escritura en .txt
    def escritura(self,data):
        try:
            archivo= open(self.guardarDatos, "a" )
            archivo.write(data)
            archivo.close()
        except IOError:
            pass
        # Reinicia un registro
    def reiniciarRegistro(self):
        try:
            archivo= open(self.guardarDatos, "w" )
            archivo.write("")
            archivo.close()
        except IOError:
            pass
        
        # Para cambiar de tempertura
    def cambioHum(self):
        input = self.tb3.text()
        input2 = float(input)
        self.BCD2.display(input2*100)
        self.AutoclaveBog.sethumidity(input2)
        self.update()
        
        # Se cambia de presión.
    def cambioPress(self):
        input = self.tb2.text()
        input2 = float(input)
        self.BCD1.display(input2)
        self.AutoclaveBog.setPressure(input2)
        self.update()
        
        # Se cambia de temperatura.
    def cambioTemp(self):
        input = self.tb1.text()
        input2 = float(input)
        self.BCD.display(input2)
        self.AutoclaveBog.setTemp(input2)
        self.pb.setValue((input2/150)*100)
        self.update()

        # Se cierra el enclave
    def cerrarEnc(self):
        if self.AutoclaveBog.close == 0:
            self.l2.setPixmap(self.pixmap1)
        self.AutoclaveBog.cerrar()
        self.update()
        
        # Se hace la simulación de un enclave abierto.
    def abrirEnc(self):
        if self.AutoclaveBog.open == 0:
            self.l2.setPixmap(self.pixmap2)
        self.AutoclaveBog.abrir()
        self.update()


if __name__ == '__main__':
    puerto = Serial("COM5", 9600)
    app = QApplication(sys.argv)
    wind = window()
    wind.show()
    sys.exit(app.exec()) # Se utliza para mantenerse en un ciclo infinito, siento sensible a los eventos.
    while (True):
        if (puerto.readable()):
            print(puerto.readline())
    