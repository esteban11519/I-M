class Autoclave: # Se crea la clase autoclave
    def __init__(self, temp, open, close, presion, humedad):
        
        # Se definen 5 características del objeto
        
        self.temperature = temp
        self.open = open
        self.close = close
        self.pressure = presion
        self.humidity = humedad

    # Se define el método de abrir 
    def abrir(self):
        if self.open == 0:
            self.open = 1
            self.close = 0
        print("self.open")
    
    # Se define el método de cerrar
    def cerrar(self):
        if self.close == 0:
            self.open = 0
            self.close = 1
        print("self.close")

    # Se configura un método para ajustar la temperatura
    def setTemp(self,temp):
        self.temperature = temp
        
    # Se ajusta la presión
    def setPressure(self,pres):
        self.pressure = pres
        
    # Se ajusta la humedad
    def sethumidity(self,hum):
        self.humidity = hum
    
    # Permite obtener la temperatura
    def getTemp(self):
        return self.temperature
    
    # Se obtiene la presión
    def getPressure(self):
        return self.pressure

    # Se obtiene la humedad
    def getHumidity(self):
        return self.humidity
    
    # Permite saber si está abierto o no
    def getEstado(self):
        if self.open==1:
            return "Abierto"
        else: return "Cerrado"        