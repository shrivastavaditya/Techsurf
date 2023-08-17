from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat.html')
def chat():
    return render_template("chat.html")

app.run(debug=True)