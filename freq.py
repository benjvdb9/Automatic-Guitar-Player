import RPi.GPIO as gpio
from time import sleep

source = 7 

gpio.setmode(gpio.BCM)
gpio.setup(source, gpio.OUT)

i = 0
while i<9000:
	gpio.output(source, gpio.HIGH)
	sleep(0.0005)
	gpio.output(source, gpio.LOW)
	sleep(0.0005)
	i+=1

gpio.output(source, gpio.LOW)
gpio.cleanup()
