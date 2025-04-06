from flask import Flask, jsonify, request
import os
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Melda ECS Flask app is starting...")

# Middleware to add security headers
@app.after_request
def set_response_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response

# Main route
@app.route('/')
def hello():
    logger.info("Root path accessed.")
    return "Hello from Melda ECS Container"

# Health check route for ALB
@app.route('/health')
def health():
    logger.info("Health check requested.")
    return jsonify(status="healthy"), 200

# Optional: HTML route
@app.route('/html')
def html():
    return "<h1>Hello from <strong>Melda</strong> ECS Container</h1>"

# Start the server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
