from flask import Flask, render_template
application = Flask(__name__)
application.debug=True

@application.route("/")
def index():
    return "<html>What?</html>"

if __name__ == '__main__':
    application.run(port=80, host='0.0.0.0', debug=True)
