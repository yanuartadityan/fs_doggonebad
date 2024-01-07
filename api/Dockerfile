# Python base image
FROM python:3.11-slim

# set the work directory
WORKDIR /app

# prevent python from making .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# create pipenv
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
