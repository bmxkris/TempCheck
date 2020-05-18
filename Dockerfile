# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3.7.7-buster

# Set the working directory to /app
#WORKDIR /app

# Copy the current directory contents into the container at /app
#ADD . /app

COPY 15_dht11.py /.
COPY wrapper.sh /.

# Intall the rpi.gpio python module
RUN pip install --no-cache-dir rpi.gpio
RUN pip install pickledb

# Trigger Python script
CMD ./wrapper.sh 
#CMD ["python3", "-m","http.server"]
# To run this image use the command:
# docker container run -p 80:8000 --device /dev/gpiomem -d docker_tempcheck
# You can then go to a browser at the IP address of your device to get the temperature
# To get the temperatures db from the contain use: docker cp [CONTAINER ID]]:/temperatures.db .
# TODO: commit to git repo and store somewhere
# TODO: move everything to the /app directory
# + S - => 1 12 6 (which I think you can largely summarise as 3.3V, input channel, ground)
