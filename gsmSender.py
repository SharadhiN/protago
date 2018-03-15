import serial
import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BCM)

# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT' + '\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

"""port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print rcv
time.sleep(1)"""

print "Text mode"
port.write('AT+CMGF=1' + '\r\n')  # Select Message format as Text mode
rcv = port.read(10)
print rcv
time.sleep(1)

print "SMS Indi"
port.write('AT+CNMI=2,1,0,0,0' + '\r\n')  # New SMS Message Indications
rcv = port.read(10)
print rcv
time.sleep(1)

# Sending a message to a particular Number


print "Number"
port.write('AT+CMGS="8105034525"' + '\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('Hello User' + '\r\n')  # Message
rcv = port.read(10)
print rcv

port.write("\x1A")  # Enable to send SMS
for i in range(10):
    rcv = port.read(10)
    print rcv
