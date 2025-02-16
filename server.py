# This is my final Flask project


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("My Final Project")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args["textToAnalyze"]
    resp = emotion_detector(text_to_analyze)    
    if not resp['dominant_emotion']:
        return "<b>Invalid text! Please try again!</b>"

    return f"For the given statement, the system response is 'anger': {resp['anger']},\
     'disgust': {resp['disgust']}, 'fear': {resp['fear']}, 'joy': {resp['joy']}\
      and 'sadness': {resp['sadness']}. \
      The dominant emotion is <b>{resp['dominant_emotion']}.</b>" 

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
