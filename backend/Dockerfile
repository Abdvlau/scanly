# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables to prevent Python from writing .pyc files and to buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the image
COPY . /app/

# Set environment variables for Flask
ENV FLASK_ENV=development

# Expose the port that the Flask app runs on
EXPOSE 5001

# Command to run the Flask app
CMD ["python", "run.py"]
