import serial
import sys
import webbrowser

def GPS_Info():
    global NMEA_buff
    global lat_in_degrees
    global long_in_degrees

    print("Time : "+str(NMEA_buff[0][0:2])+":"+str(NMEA_buff[0][2:4])+":"+str(NMEA_buff[0][4:6]))

    lat_in_degrees = convert_to_degrees(float(NMEA_buff[1]))
    long_in_degrees = convert_to_degrees(float(NMEA_buff[3]))

def convert_to_degrees(raw_value):
    degrees = int(raw_value/100.00)
    precision = (raw_value/100.00 - int(raw_value/100.00))/0.6
    position = "%.4f" %(degrees + precision)
    return position

NMEA_buff = 0
lat_in_degrees = 0
long_in_degrees = 0

try:
    while True:
        received_data = (str)(serial.Serial("/dev/ttyAMA0").readline())
        if received_data.find('$GPGGA,') == 0:
			GPGGA_buffer = received_data.split("$GPGGA,",1)[1]
			NMEA_buff = (GPGGA_buffer.split(','))
			GPS_Info()
			print("Latitude(deg)  : "+lat_in_degrees+"\n"+"Longitude(deg) : "+long_in_degrees)
			map_link = 'https://maps.google.com/maps?daddr='+lat_in_degrees+','+long_in_degrees
			print("<<< Press ctrl+c to plot location on google maps >>>\n")
			print("------------------------------------------------------------\n")

except KeyboardInterrupt:
    webbrowser.open(map_link)
    sys.exit(0)
