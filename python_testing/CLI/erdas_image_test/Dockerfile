# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install GDAL dependencies
RUN apt-get update && apt-get install -y \
    libgdal-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install GDAL Python bindings matching the system's GDAL version
RUN GDAL_VERSION=$(gdal-config --version) && \
    pip install numpy && \
    pip install GDAL==$GDAL_VERSION

# Set environment variables to help Python find GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PYTHONUNBUFFERED=1

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Command to run when starting your container
CMD ["python", "./main.py"]

