import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 

    # Sends and converts the request
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    """error handling"""
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        
        emotions = formatted_response["emotionPredictions"][0]['emotion']
        
        anger_score = emotions.get('anger')
        disgust_score = emotions.get('disgust')
        fear_score = emotions.get('fear')
        joy_score = emotions.get('joy')
        sadness_score = emotions.get('sadness')
        
        # Finds the dominant emotion through max()
        dominant_emotion = max(emotions, key=emotions.get)

        # Returns the score 
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
    }

    # If the response status code is 400, set label and score to None
    elif response.status_code == 400:
        # Return None for all emotions for blank or invalid input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
