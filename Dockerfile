# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables to avoid buffering and ensure Python runs in unbuffered mode
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Command to run the FastAPI server using Uvicorn
CMD ["uvicorn", "api.create_app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
