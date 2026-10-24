from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        # Capture the data sent from the input field with name="name"
        name_value = request.form.get("name")
        return f"Received POST request! Hello, {name_value}! 🎉"
        
    # If it's a regular GET request, just render the page
    return render_template("flask_practice.html")

if __name__ == '__main__':
    app.debug = True
    app.run()