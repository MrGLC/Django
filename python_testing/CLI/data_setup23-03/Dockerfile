# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
# Now including matplotlib and seaborn for plotting
RUN pip install pandas openpyxl numpy

# Run script.py when the container launches
CMD ["python", "script.py"]

