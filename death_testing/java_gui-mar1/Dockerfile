# Use Ubuntu as the base image for better library support
FROM ubuntu:20.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install Java and X11 libraries necessary for Java GUI applications
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    libxext6 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libfreetype6 \
    fontconfig \
    libx11-dev \
    x11-utils \
    x11-xserver-utils \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy your Java GUI application into the Docker image
COPY . /app

# Compile the Java application
# Replace MainMenu.java with the name of your Java file
RUN javac MainMenu.java

# Command to run the Java application
# Replace MainMenu with the main class name, if different
CMD ["java", "MainMenu"]

