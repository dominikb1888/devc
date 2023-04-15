# Use the official Python image as the base image
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9-buster

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
