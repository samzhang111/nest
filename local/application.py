from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import select
from database import db
from models import Post

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@127.0.0.1'
application.debug = True

db.init_app(application)

@application.route("/")
def main():
    r = db.Post.query.filter(Post.depth==0).first()
    return "Hello World!", r

if __name__ == "__main__":
    application.run(debug=True)

