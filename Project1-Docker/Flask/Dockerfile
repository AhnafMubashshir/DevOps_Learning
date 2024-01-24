
# # Use an official Python runtime as a parent image
# FROM python:3.8-slim

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# # Make port 80 available to the world outside this container
# EXPOSE 80

# # Define environment variable
# ENV NAME World

# # Run app.py when the container launches
# CMD ["python", "app.py"]

FROM python:3.9.10-alpine3.14
WORKDIR /srv
RUN pip install --upgrade pip
RUN pip install flask
COPY . /srv
ENV FLASK_APP=app
EXPOSE 80
CMD ["python","app.py"]