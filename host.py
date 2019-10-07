from flask import Flask


app = Flask(__name__)

@app.route("/administer")
def hello():
	return "Hello World"
app.run(host="0.0.0.0")