# TempCheck
Use docker, a Raspberry Pi and a DHT11 sensor to monitor temperature of a room

To build the docker image:
docker build -t "docker_tempcheck" .

To run this image use the command:
docker container run -p 80:8000 --device /dev/gpiomem -d docker_tempcheck

You can then go to a browser at the IP address of your device to get the temperature

To get the temperatures db from the contain use: 
docker cp [CONTAINER ID]:/app/temperartures.db .

The DHT11 has three pins: + S - which are wired to the following pins on the Raspberry Pi 1, 12 & 6 (which I think you can largely summarise as 3.3V, input channel 18 and ground)

