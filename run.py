from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive information from environment variables
API_KEY = os.getenv('API_KEY')
CSE_ID = os.getenv('CSE_ID')

# Use these variables in your application


from app import app

if __name__ == '__main__':
    app.run(debug=True)
