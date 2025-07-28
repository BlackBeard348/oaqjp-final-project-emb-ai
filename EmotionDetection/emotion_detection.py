import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    """error handling"""
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
            formatted_response = response.json()

            emotions = formatted_response["emotionPredictions"][0]["emotion"]

            # Extract individual scores (optional if you already have emotions dict)
            anger_score = emotions.get("anger")
            disgust_score = emotions.get("disgust")
            fear_score = emotions.get("fear")
            joy_score = emotions.get("joy")
            sadness_score = emotions.get("sadness")

            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        anger_score = None
        disgust_score = None  
        fear_score = None 
        joy_score = None 
        sadness_score = None  
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        "dominant_emotion": dominant_emotion
    }