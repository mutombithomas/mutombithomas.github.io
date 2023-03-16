# This is a Dockerfile which needs to be named Dockerfile for docker to know it is
# It's purpose is to provide instructions for building a docker image
# A docker image is not quite a containerised verison of your model but more a snapshot of a docker container

# Docker base image: this is an official Python runtime as a parent image
FROM python:3.9-slim-buster

# the working directory in this dockerfile just specifying the location of where the files will be stored in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required Python packages
RUN pip install -r requirements.txt


CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]