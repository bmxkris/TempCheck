#!/usr/bin/python

import RPi.GPIO as GPIO
from datetime import datetime
import time
import pickledb
import sys
import os

db = pickledb.load(os.path.join(sys.path[0], "temperartures.db"), True)

channel = 18
data = []
j = 0

while True:

	GPIO.setmode(GPIO.BCM)

	time.sleep(1)

	GPIO.setup(channel, GPIO.OUT)

	GPIO.output(channel, GPIO.LOW)
	time.sleep(0.02)
	GPIO.output(channel, GPIO.HIGH)

	GPIO.setup(channel, GPIO.IN)



	while GPIO.input(channel) == GPIO.LOW:
		continue

	while GPIO.input(channel) == GPIO.HIGH:
		continue

	while j < 40:
		k = 0
		while GPIO.input(channel) == GPIO.LOW:
			continue

		while GPIO.input(channel) == GPIO.HIGH:
			k += 1
			if k > 100:
				break

		if k < 8:
			data.append(0)
		else:
			data.append(1)

		j += 1

	print ("sensor is working.")
	# print data

	humidity_bit = data[0:8]
	humidity_point_bit = data[8:16]
	temperature_bit = data[16:24]
	temperature_point_bit = data[24:32]
	check_bit = data[32:40]

	humidity = 0
	humidity_point = 0
	temperature = 0
	temperature_point = 0
	check = 0

	for i in range(8):
		humidity += humidity_bit[i] * 2 ** (7 - i)
		humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
		temperature += temperature_bit[i] * 2 ** (7 - i)
		temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
		check += check_bit[i] * 2 ** (7 - i)

	tmp = humidity + humidity_point + temperature + temperature_point

	if check == tmp:
		f = open(os.path.join(sys.path[0], "index.html"), "w")
		f.write("<p>Last updated: " + datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)") + "</p><p>Temperature : " + str(temperature) + "</p><p> Humidity : " + str(humidity)+ "</p>" )
		f.close()
		db.set(str(time.time()) + "-temp", str(temperature))
		db.set(str(time.time()) + "-humidity", str(humidity))
		print("temperature : " + str(temperature) + ", humidity : " + str(humidity))
	else:
		print( "wrong")
		print( "temperature : " + str(temperature) + ", humidity : " + str(humidity) + " check : " + str(check) + " tmp : " + str(tmp))

	GPIO.cleanup()
	time.sleep(60)
