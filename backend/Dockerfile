# syntax=docker/dockerfile:1
FROM alpine:latest

# General Updates
RUN apk update

# Install Packages
RUN apk add vim
RUN apk add python3

# General Updates
RUN apk upgrade

# Update Python3 Dependencies
RUN python3 -m ensurepip --upgrade
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN pip3 install "fastapi[all]"
RUN pip3 install mysql-connector-python
RUN pip3 install openai

# Deploy Code
WORKDIR /app
COPY . .

# Run
ENTRYPOINT uvicorn app:app --host 0.0.0.0 --reload
