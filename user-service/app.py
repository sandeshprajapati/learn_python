# app.py
import sys
from flask import Flask
from config import Config
from models.user import db
from controllers.user_controller import user_controller

app = Flask(__name__)

# Configure the app with external config file
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register the controllers (routes)
app.register_blueprint(user_controller)

if __name__ == '__main__':
    # Create all database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)

sys.dont_write_bytecode = True
