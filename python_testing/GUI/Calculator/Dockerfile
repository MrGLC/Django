FROM python:3.12-slim

# Install dependencies required for Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    libx11-6 \
    && pip install numpy matplotlib \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY . /app

# Command to run the application
CMD ["python", "./calculator.py"]
