# Use the nginx image
FROM nginx:alpine

# Remove the default nginx HTML file
RUN rm /usr/share/nginx/html/index.html

# Copy the index.html file into the container
COPY index.html /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

