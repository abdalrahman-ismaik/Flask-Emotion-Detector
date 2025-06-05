import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }    
    
    response = requests.post(URL, json=Input_json, headers=Headers)
    text = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # Handle blank input or server error
    if response.status_code == 400 or not text_to_analyze.strip():
        return text
    
    reresponse_dict = response.json()

    if reresponse_dict['emotionPredictions'] is not None:
        emotions = reresponse_dict['emotionPredictions'][0]['emotion']
        text = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': max(emotions, key=emotions.get)
        }

    return text 
