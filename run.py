

from app import app
"""
This script serves as the entry point for running the Flask application.

It imports the Flask app instance from the 'app' module and starts the development server
when executed directly.

Usage:
    python run.py

The server will start using the default Flask configuration.
"""

if __name__ == '__main__':
    app.run()

