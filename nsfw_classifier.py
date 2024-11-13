from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image

local_model_path = "./model/nsfw-classifier"

app = Flask(__name__)

# use this to download the model locally from hugginface
# pipe = pipeline("image-classification", model="giacomoarienti/nsfw-classifier")
# pipe.save_pretrained(local_model_path)

# Load the local NSFW classifier model
pipe = pipeline("image-classification", model=local_model_path)

@app.route('/nsfw_classifier', methods=['POST'])
def nsfw_classifier():
    # Check if an image is part of the request
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    # Load image from the request
    image_file = request.files['image']
    image = Image.open(image_file)
    
    # Get classification results
    results = pipe(image)

    # Initialize response dictionary for specific labels
    response = {"neutral_score": None, "porn_score": None}

    # Extract scores for 'neutral' and 'porn' labels
    for result in results:
        if result['label'] == 'neutral':
            response['neutral_score'] = result['score']
        elif result['label'] == 'porn':
            response['porn_score'] = result['score']

    # Ensure scores are available in the response
    if response["neutral_score"] is None and response["porn_score"] is None:
        return jsonify({"error": "Model response did not include required labels"}), 500

    # Return the scores as JSON
    return jsonify(response)

@app.route('/hello', methods=['GET'])
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

# curl -X POST -F "image=@./data/image2.png" http://127.0.0.1:5000/nsfw_classifier 