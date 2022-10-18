# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /project

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the app script to the working directory
COPY code/aboutme.py .

# server listening on port 1234
EXPOSE 1234

# command to run on container start
CMD [ "python", "./aboutme.py" ]