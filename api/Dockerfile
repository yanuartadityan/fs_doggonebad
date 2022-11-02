# Python base image
FROM python:3.9.15-slim

# set the work directory
WORKDIR /app

# prevent python from making .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy pip-dependencies to WORKDIr
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .