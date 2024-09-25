# Use gcc image from Docker Hub to compile C++ code
FROM gcc:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Compile the C++ program
RUN g++ -o main main.cpp

# Run the program
CMD ["./main"]

