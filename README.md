# Brain-Tumor-Detection
🧠 Brain Tumor Detection using Deep Learning

This project is a deep learning-based web application that automatically detects the presence and type of brain tumors from MRI images. It classifies images into four categories: Glioma Tumor, Meningioma Tumor, Pituitary Tumor, and No Tumor using a Convolutional Neural Network (CNN) trained on a labeled dataset.

Built using TensorFlow/Keras for model development and Flask for web deployment, the app allows users to upload MRI scans via a browser interface and returns the predicted tumor type along with a confidence score.

The project consists of two main components:

Model Training (BT.ipynb): A Jupyter notebook that handles the training of a CNN model on a brain tumor dataset.

Web Application (app.py): A Flask-based interface where users can upload MRI images and receive predictions in real-time.

📂 Project Structure
├── app.py                  # Flask app for image upload and prediction <br>
├── BT.ipynb                # Jupyter notebook for training the model  <br>
├── my_model.keras          # Trained model file (not included, must be generated)  <br>
├── templates/         <br>
│   └── index.html          # HTML template for the web UI       <br>
├── static/  <br>
│   └── uploads/            # Folder to store uploaded images    <br>

Model Details
 Input size: 150x150 RGB images
 Output: 4 classes
 Framework: TensorFlow / Keras
 Loss: Categorical Crossentropy
 Metrics: Accuracy

📌 Features
Upload MRI scans through the browser

Classifies the image into one of four categories

Displays predicted class and confidence

Clean, minimal web UI

📁 Dataset
You can use datasets like the Brain Tumor Dataset from Kaggle for training.
