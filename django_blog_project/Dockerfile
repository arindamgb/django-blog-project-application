# This Dockerfile resides inside the main project folder
# At the same level as manage.py file

# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set environment variables for Python and Docker
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Run Gunicorn with your WSGI application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "django_blog_project.wsgi:application"]
