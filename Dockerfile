# Use the official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Flask app into the image
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port 3000 for the container
EXPOSE 3000

# Run the Flask app
CMD ["python", "app.py"]
