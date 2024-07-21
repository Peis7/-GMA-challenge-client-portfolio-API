# Use an official Python runtime as the base image
FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl

# Set the working directory in the container to /app
WORKDIR /src

# Copy the current directory (our Flask app) into the container at /app
COPY  /src .

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available for the app
EXPOSE 5001

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]