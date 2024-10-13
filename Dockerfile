# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Copy the requirements.txt into the container and install the Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the Django application into the container
COPY . .

# Step 6: Set environment variables
ENV PYTHONUNBUFFERED 1

# Step 7: Expose the port the app runs on
EXPOSE 8000

# Step 8: Start the application
CMD ["gunicorn", "urlshortener.wsgi:application", "--bind", "0.0.0.0:8000"]
