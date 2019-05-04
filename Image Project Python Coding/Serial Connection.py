

import serial


ser = serial.Serial('COM8', 9600)
while True:

    ser.write(1)

