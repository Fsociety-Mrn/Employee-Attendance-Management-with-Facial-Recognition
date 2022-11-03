import serial
import time

port = "COM7"
Arduino = serial.Serial(port ,9600, timeout=1)

def SerialWrite(i):
    
# while True:
    time.sleep(1)
    b = "%s" %i
    Arduino.write(bytes(b, 'utf-8'))

    #the Arduino waits for this and can seperate the numbers 
    Arduino.write(b'\n')

def SerialRead():
    Arduino.flush()
    return Arduino.read_until().decode().strip()

# while True:
#     print(SerialRead())


