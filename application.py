from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ebroot:jowran8I@aae5w8f5ejqw45.csi1cndzkahd.us-east-1.rds.amazonaws.com'
db = SQLAlchemy(application)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()

