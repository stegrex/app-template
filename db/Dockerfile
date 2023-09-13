# syntax=docker/dockerfile:1
FROM mysql:latest

# Deploy Code
WORKDIR /app
COPY . .
COPY --chmod=755 startup.sh .
