import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
import cv2

app = Flask(__name__)
model = load_model('my_model.keras')
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html', show_result=False)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Preprocess the image
        img = cv2.imread(file_path)
        img = cv2.resize(img, (150, 150))
        img = np.expand_dims(img, axis=0)

        # Predict
        predictions = model.predict(img)[0]
        confidence = float(np.max(predictions)) * 100
        predicted_class = ["Glioma Tumor", "Meningioma Tumor", "No Tumor", "Pituitary Tumor"][np.argmax(predictions)]

        return render_template(
            'index.html',
            show_result=True,
            image_url=file_path,
            predicted_class=predicted_class,
            confidence=f"{confidence:.2f}"
        )

if __name__ == '__main__':
    app.run(debug=True)
