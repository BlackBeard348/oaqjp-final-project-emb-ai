''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on localhost:5001.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

""" This is the GET route for retrieving the data and providing the response"""
@app.route("/emotionDetector")
def sent_emotion():
    """Retrieve the text to analyze and return emotion scores"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Unpack the values properly
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid input! Try again."

    return (
        f"Anger: {anger}, Disgust: {disgust}, Fear: {fear}, "
        f"Joy: {joy}, Sadness: {sadness}. Dominant emotion: {dominant_emotion}"
    )

#This function initiates the rendering of the main applicationpage over the Flask channel
@app.route("/")
def render_index_page():
    """returns the index tenplate information"""
    return render_template('index.html')

#This functions executes the flask app and deploys it on localhost:5001
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
