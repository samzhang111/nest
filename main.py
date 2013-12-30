from flask import Flask, render_template
app = Flask(__name__)
app.debug=True

@app.route("/")
def index():
    return "<html>What?</html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
