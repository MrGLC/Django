# Use an official OpenJDK runtime as a parent image
FROM openjdk:11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Compile the Java program
RUN javac ArrayShift.java

# Run the Java program when the container launches
CMD ["java", "ArrayShift"]

