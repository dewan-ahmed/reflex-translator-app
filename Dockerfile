# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment
RUN python -m virtualenv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Make sure the virtual environment is used for the CMD
ENV PATH="/app/venv/bin:$PATH"

# Expose the ports the app runs on
EXPOSE 3000
EXPOSE 8000

# Run reflex app
CMD ["reflex", "run"]
