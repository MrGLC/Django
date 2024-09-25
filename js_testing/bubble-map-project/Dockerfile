# Use the Nginx image from Docker Hub
FROM nginx:alpine

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy a new configuration file from the current directory
COPY nginx.conf /etc/nginx/conf.d

# Copy the HTML file into Nginx's serve directory
COPY . /usr/share/nginx/html

# Expose port 80 to the outside once the container has launched
EXPOSE 80

