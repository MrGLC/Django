# Use a full Python image that includes dependencies for tkinter
FROM python:3.9

# Install tkinter explicitly
RUN apt-get update && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN pip install mysql-connector-python

# Command to run the application
CMD ["python", "./main.py"]

