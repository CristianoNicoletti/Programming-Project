
# Entry point for the Flask backend application
from flask import Flask, jsonify
from routes import register_routes

# Create the Flask app instance
app = Flask(__name__)

# Register all API routes (endpoints) with the app
register_routes(app)

# Run the Flask development server if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)

