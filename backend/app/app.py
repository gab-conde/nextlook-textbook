from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create app
app = Flask(__name__)

# Debug reloads the app when changes are made to the code
if __name__ == '__main__':
    app.run(debug=True)