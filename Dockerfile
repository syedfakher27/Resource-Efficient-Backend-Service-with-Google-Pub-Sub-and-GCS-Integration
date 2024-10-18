# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app

# Expose the port the app runs on
EXPOSE 8080

CMD ["python", "main.py"] 