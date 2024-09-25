# Use an image with gcc
FROM ubuntu:latest

# Install C++ compiler and necessary libraries
RUN apt-get update && apt-get install -y \
    g++ \
    libexiv2-dev \  
    libpoppler-cpp-dev \  
    pkg-config  

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Compile the C++ program (update this command as necessary)
# Ensure to check if pkg-config commands need to be enclosed with $()
RUN g++ -o myapp main.cpp $(pkg-config --cflags --libs exiv2) $(pkg-config --cflags --libs poppler-cpp)

# Command to run the application
CMD ["./myapp"]

