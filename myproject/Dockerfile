# ===============================
#   DJANGO STUDENT MANAGEMENT
#   Production Dockerfile
# ===============================
FROM python:3.11-slim

# Prevent Python from writing .pyc files & enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    pkg-config \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY myproject/requirements.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY myproject ./

# Set environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Expose port
EXPOSE 8000

# Start container: run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT"]