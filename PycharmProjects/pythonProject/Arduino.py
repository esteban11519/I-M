import serial



if __name__ == '__main__':
    puerto = serial.Serial("COM5",9600)
    while(True):
        if(puerto.readable()):
            print(puerto.read())