from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger_score = response.get('anger') 
    disgust_score = response.get('disgust')
    fear_score = response.get('fear')
    joy_score = response.get('joy') 
    sadness_score = response.get('sadness') 

    # Identify dominant emotion
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]

    if dominant_score is None:
        return "Invalid input! Try again."
    else:
        # Return a formatted string with the sentiment label and score
        return (f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}. The dominant emotion is {dominant_emotion}"
        )
    
#This function initiates the rendering of the main applicationpage over the Flask channel
@app.route("/")
def render_index_page():
    """returns the index tenplate information"""
    return render_template('index.html')

#This functions executes the flask app and deploys it on localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)