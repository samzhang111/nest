from flask import Flask

application = Flask(__name__)
application.debug = True

from application import views
