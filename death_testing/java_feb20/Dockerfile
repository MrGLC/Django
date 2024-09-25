# Use an official OpenJDK runtime as a parent image
FROM openjdk:11

# Set the working directory in the container
WORKDIR /usr/src/myapp

# Copy the local code to the container
COPY . .

# Compile the Java program
RUN javac Tablet.java

# Run the Java program when the container launches
CMD ["java", "Tablet"]

