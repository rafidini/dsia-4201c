# Import python 3.8 from DockerHub
FROM python:3.8-buster

# Define the application directory
WORKDIR /app

# Copy the file to the Docker image
COPY requirements.txt .

# Run the command to install python packages
RUN pip install -r requirements.txt

# Copy the application repository in the Docker image
COPY /app .

# Run the command to get the articles
RUN python step1.py && \
    python step2.py

# The command to launch the app
CMD ["python", "app.py"]