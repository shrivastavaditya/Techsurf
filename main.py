from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/chat.html')
def chat():
    return render_template("chat.html")

@app.route('/technical.html')
def tech():
    return render_template("technical.html")

@app.route('/academic.html')
def aca():
    return render_template("academic.html")

@app.route('/blog.html')
def blog():
    return render_template("blog.html")

@app.route('/ecom.html')
def eco():
    return render_template("ecom.html")

@app.route('/market.html')
def mkt():
    return render_template("market.html")

@app.route('/news.html')
def news():
    return render_template("news.html")

@app.route('/social.html')
def soc():
    return render_template("social.html")

@app.route('/translate.html')
def translation():
    return render_template("translate.html")

app.run(debug=True)