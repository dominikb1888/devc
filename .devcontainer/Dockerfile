# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app files into the container
COPY . /app

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose the desired port for the Flask app to listen on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]





