# Import the Flask module
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define a route for the root URL ("/") with a function to handle requests
@app.route('/')
def hello():
    return 'Hello, World!'

# Start the Flask app if this file is run directly
if __name__ == '__main__':
    app.run(debug=True)
