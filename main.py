from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import os
import openai

openai.api_key = ""





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
    qstn = mongo.db.qstn.find({})
    myQstn = [qst for qst in qstn]
    print(myQstn)
    return render_template("blog.html", myQstn= myQstn)

@app.route('/ecom.html')
def eco():
    return render_template("ecom.html")

@app.route('/market.html')
def mkt():
    qstn = mongo.db.qstn.find({})
    myQstn = [qst for qst in qstn]
    print(myQstn)
    return render_template("market.html", myQstn= myQstn)

@app.route('/news.html')
def news():
    qstn = mongo.db.qstn.find({})
    myQstn = [qst for qst in qstn]
    print(myQstn)
    return render_template("news.html", myQstn= myQstn)

@app.route('/social.html')
def soc():
    qstn = mongo.db.qstn.find({})
    myQstn = [qst for qst in qstn]
    print(myQstn)
    return render_template("social.html", myQstn= myQstn)

@app.route('/translate.html')
def translation():
    qstn = mongo.db.qstn.find({})
    myQstn = [qst for qst in qstn]
    print(myQstn)
    return render_template("translate.html", myQstn= myQstn)

@app.route('/api',methods=["GET","POST"])
def qa():
    if request.method =="POST":
        print(request.json)
        qstn = request.json.get("question")
        qst = mongo.db.qstn.find_one({"question": qstn})
        #print(qst)
        if qst:
            data={"question": qstn, "answer": f"{qst['answer']}"}
            return jsonify(data)
        else:
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                    {
                     "role": "user",
                     "content": qstn
                    }
                       ],
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
              )
            print(response)
            data={"question": qstn, "answer": response["choices"][0]["message"]["content"]}
            mongo.db.qstn.insert_one( {"question": qstn, "answer": response["choices"][0]["message"]["content"]} )
            return jsonify(data)
    data={"result":"Aditya hi data hai"}
    return jsonify(data)

app.run(debug=True)