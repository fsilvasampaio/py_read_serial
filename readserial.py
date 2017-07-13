'''
This simple script will get values from serial port.
Useful for debugging ;)

References:

http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard

http://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/

Author: Felipe Sampaio

Licence: GPL

'''

from time import sleep
import serial

# "raw_input" is used to read text (strings) from the user
# "port" variable will get the port address
port = raw_input('Tell me the port address:')

# Establish the connection on a specific port
ser = serial.Serial(port, 115200)

counter = 32 # Below 32 everything in ASCII is gibberish

while True:
     counter +=1
     ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     print ser.readline() # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
     if counter == 255:

     	counter = 32
