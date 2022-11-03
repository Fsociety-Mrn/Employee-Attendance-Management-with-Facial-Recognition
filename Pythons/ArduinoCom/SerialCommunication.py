import serial
import time

<<<<<<< HEAD
port = "COM4"
=======
port = "COM7"
>>>>>>> 779772bb028bcbf1591f62c5c133dfbd5f45dcb9
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


