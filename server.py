from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please provide a valid text input.", 400

    response = emotion_detector(text_to_analyze)
    
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again.", 400

    # Format the response string
    emotions = {
        'anger': response.get('anger', 0),
        'disgust': response.get('disgust', 0),
        'fear': response.get('fear', 0),
        'joy': response.get('joy', 0),
        'sadness': response.get('sadness', 0)
    }
    dominant_emotion = response['dominant_emotion']

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return jsonify({
        "raw_response": response,
        "formatted_response": formatted_response
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
