# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Reflex
RUN pip install reflex

# Expose the ports the app runs on
EXPOSE 3000
EXPOSE 8000

# Run reflex app
CMD ["rx", "run", "--no-watch"]
