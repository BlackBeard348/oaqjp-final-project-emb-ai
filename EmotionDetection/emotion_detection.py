import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    """error handling"""
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
           response = emotion_detector(text_to_analyze)
  File "/home/project/oaqjp-final-project-emb-ai/EmotionDetection/emotion_detection.py", line 48, in emotion_detector
    'anger': anger_score,
UnboundLocalError: local variable 'anger_score' referenced before assignment
127.0.0.1 - - [30/Jul/2025 06:17:11] "GET /emotionDetector?textToAnalyze= HTTP/1.1" 500 -
        emotions = formatted_response["emotionPredictions"][0]['emotion']

        anger_score = formatted_response["emotionPredictions"][0]['emotion']['anger']
        disgust_score = formatted_response["emotionPredictions"][0]['emotion']['disgust']
        fear_score = formatted_response["emotionPredictions"][0]['emotion']['fear']
        joy_score = formatted_response["emotionPredictions"][0]['emotion']['joy']
        sadness_score = formatted_response["emotionPredictions"][0]['emotion']['sadness']

        # Find the dominant emotion and its score
        dominant_emotion = max(emotions, key=emotions.get)  # gives the emotion name
        dominant_score = emotions[dominant_emotion]         # gives the score


    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None


    # Return the label and score in a dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        "dominant_emotion": dominant_emotion
    }