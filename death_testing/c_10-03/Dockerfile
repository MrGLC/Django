# Use an official gcc runtime as a parent image
FROM gcc:latest

# Set the working directory in the container
WORKDIR /usr/src/myapp

# Copy the current directory contents into the container at /usr/src/myapp
COPY . /usr/src/myapp

# Compile the C program
RUN gcc -o myprogram myprogram.c

# Run the program when the container launches
CMD ["./myprogram"]

