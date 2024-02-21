# This Dockerfile resides out of the main project folder
# NOT at the same level as manage.py file

# Pull base image
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set work directory called `app`
RUN mkdir /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copy local project
COPY . .

# Expose port 8000
EXPOSE 8000

# set the WORKDIR at the same level as manage.py file
WORKDIR /app/django_blog_project

# Use gunicorn on port 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_blog_project.wsgi"]
