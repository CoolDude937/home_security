# Use the official PostgreSQL image as the base
FROM postgres:latest

# Set the required environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=123456
ENV POSTGRES_DB=andy_database

# Copy the SQL initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/
