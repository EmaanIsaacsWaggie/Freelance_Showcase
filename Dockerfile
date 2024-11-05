# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port (if applicable)
EXPOSE 8000

# Command to run your application (adjust as necessary)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
