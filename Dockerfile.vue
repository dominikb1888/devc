# Use the official Node.js image as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY vue/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY vue/ .

# Expose port 8080 for the Vue.js app to listen on
EXPOSE 8080

# Start the Vue.js app
CMD ["npm", "run", "dev"]
