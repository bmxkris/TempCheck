# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3.7.7-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Intall the rpi.gpio python module
RUN pip install --no-cache-dir rpi.gpio
RUN pip install pickledb

# Sort out the time
RUN apt-get install tzdata
ENV TZ Europe/London

# Trigger Python script
CMD ./wrapper.sh 
