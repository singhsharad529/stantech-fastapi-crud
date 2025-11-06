# Official Python runtime as a parent image
FROM python:3.11-slim

# Environment variables
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Working directory in the container
WORKDIR /app

# Install dependencies
# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
# This assumes your code (main.py, models.py, etc.) is in an 'app' directory
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# This will run when the container starts.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]