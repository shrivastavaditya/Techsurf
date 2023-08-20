from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"





app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://adityaryk:aditya@cluster0.dqf0sje.mongodb.net/news"
mongo = PyMongo(app)


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
    qstn = mongo.db.qstn.find({})
    myQstn = [qst for qst in qstn]
    print(myQstn)
    return render_template("news.html")

@app.route('/social.html')
def soc():
    return render_template("social.html")

@app.route('/translate.html')
def translation():
    return render_template("translate.html")

@app.route('/api',methods=["GET","POST"])
def qa():
    if request.method =="POST":
        print(request.json)
        qstn = request.json.get("question")
        qst = mongo.db.qstn.find_one({"question": qstn})
        print(qst)
        if qst:
            data={"result": f"{qst['answer']}"}
            return jsonify(data)
        else:
            response = openai.Completion.create(
               model="text-davinci-003",
               prompt=qstn,
               temperature=0.7,
               max_tokens=256,
               top_p=1,
               frequency_penalty=0,
               presence_penalty=0
            )
            data={"question": qstn, "answer": response["choices"][0]["text"]}
            mongo.db.qstn.insert_one( {"question": qstn, "answer": response["choices"][0]["text"]} )
            return jsonify(data)
    data={"result":"Aditya hi data hai"}
    return jsonify(data)

app.run(debug=True)