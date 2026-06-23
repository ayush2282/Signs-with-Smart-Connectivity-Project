
from flask import Flask, render_template, jsonify
import random
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/data")
def data():
    weather=random.choice(["Sunny","Rain","Fog","Snow"])
    speed={"Sunny":80,"Rain":60,"Fog":40,"Snow":30}[weather]
    traffic=random.choice(["Low","Medium","High","Accident"])
    return jsonify(weather=weather,speed=speed,traffic=traffic)

if __name__=="__main__":
    app.run(debug=True)
