from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from credentials import user, pw

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@aae5w8f5ejqw45.csi1cndzkahd.us-east-1.rds.amazonaws.com'%(user, pw)

db = SQLAlchemy(application)

@application.route("/")
def hello():
    return "Testing!"

if __name__ == "__main__":
    application.run()

