class Autoclave:
    def __init__(self, temp, open, close, presion, humedad):
        self.temperature = temp
        self.open = open
        self.close = close
        self.pressure = presion
        self.humidity = humedad

    def abrir(self):
        if self.open == 0:
            self.open = 1
            self.close = 0
        print("self.open")

    def cerrar(self):
        if self.close == 0:
            self.open = 0
            self.close = 1
        print("self.close")

    def setTemp(self,temp):
        self.temperature = temp

    def setPressure(self,pres):
        self.pressure = pres

    def sethumidity(self,hum):
        self.humidity = hum
        
    def getTemp(self):
        return self.temperature

    def getPressure(self):
        return self.pressure

    def getHumidity(self):
        return self.humidity
    
    def getEstado(self):
        if self.open==1:
            return "Abierto"
        else: return "Cerrado"        