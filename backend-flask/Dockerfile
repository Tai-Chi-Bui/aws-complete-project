# Use the official Python 3.10 slim image based on Debian Buster
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /backend-flask

# Copy the requirements.txt file from the host to the container
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Copy the application code from the host to the container
COPY . .

# Set the FLASK_ENV environment variable to 'development'
ENV FLASK_ENV=development

# Expose the specified port (expected to be provided at runtime)
EXPOSE ${PORT}

# Command to run the Flask application when the container starts
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
