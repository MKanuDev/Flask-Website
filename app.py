from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST"])
def contact():
	name = request.form.get("name")
	message = request.form.get("message")

	with open("messages.txt", "a") as file:
	    file.write(f"name: {name}\n")
	    file.write(f"message: {message}\n")
	    file.write(f"Date: {datetime.now()}\n")
	    file.write("--------------------\n")

	return "Message save! Thank you & be blessed, " + name

if __name__ == "__main__":
	app.run(debug=True)
