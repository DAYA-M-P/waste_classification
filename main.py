import os
import numpy as np
import cv2
import pickle
from flask import Flask, render_template, request

# Suppress TensorFlow and other warnings (optional)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Load model
with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def predict_func(img):
    if img is None:
        return "Error: Image not loaded properly"

    # Preprocess
    img = cv2.resize(img, (224, 224))
    img = np.reshape(img, [-1, 224, 224, 3])
    img = img / 255.0

    # Predict
    result = np.argmax(model.predict(img))

    if result == 0:
        return "This image shows recyclable waste ♻️"
    elif result == 1:
        return "This image shows organic waste 🌱"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template("index.html", res="No image uploaded")

        file = request.files['image']
        if file.filename == '':
            return render_template("index.html", res="No image selected")

        # Save and read image
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        img = cv2.imread(filepath)

        # Get prediction
        result = predict_func(img)

        return render_template("index.html", res=result, img_path=filepath)

    return render_template("index.html", res="")

if __name__ == '__main__':
    app.run(debug=True)
