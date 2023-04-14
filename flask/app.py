from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@db/{os.environ['POSTGRES_DB']}" # Update with your own database connection detail

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))

    def __init__(self, content):
        self.content = content

@app.route('/api/hello')
def hello():
    # Retrieve message from database
    message = Message.query.get(1)
    if message:
        return jsonify(message=message.content)
    else:
        return jsonify(message='No message found in the database.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

