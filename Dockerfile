# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 3000 8000

# Run the app using Reflex when the container launches
CMD ["rx", "serve", "--host", "0.0.0.0", "--port", "3000"]
