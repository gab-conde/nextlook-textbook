from flask import Flask

# Create app
app = Flask(__name__)

# Debug reloads the app when changes are made to the code
if __name__ == '__main__':
    app.run(debug=True)