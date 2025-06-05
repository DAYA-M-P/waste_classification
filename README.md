# 🗑️ Waste Classification using CNN with Web App Interface

This project uses a Convolutional Neural Network (CNN) to classify waste into categories (e.g., recyclable or organic). It also includes a Flask web application that allows users to upload images and get real-time waste classification results.

---

## 📌 Project Objective

To build an AI-powered tool that classifies waste from images to promote sustainable waste management. The solution includes both a machine learning model and an interactive web interface.

---

## 🧠 Model Overview

- Model Type: Convolutional Neural Network (CNN)
- Framework: TensorFlow / Keras
- Input Size: 224x224 RGB images
- Output Classes:
  - **0**: Recyclable ♻️
  - **1**: Organic 🌱

---

## 🕸️ Web Interface

The Flask-based web application allows users to:

- Upload an image of waste
- View the predicted category (Recyclable / Organic)
- Display the uploaded image with the result

---

## 🛠️ Tech Stack

- Python
- Flask
- TensorFlow / Keras
- OpenCV
- HTML / CSS (for frontend)

---
## 📂 File Structure

wasteclassification.ipynb # Jupyter Notebook (model training)
app.py # Flask web application (your .py file)
model.pkl # Trained model saved with pickle
static/uploads/ # Folder for uploaded images
templates/index.html # HTML template for web UI


---


---

## 🚀 How to Run the Project

### Step 1: Clone the Repository


git clone https://github.com/your-username/waste-classification.git
cd waste-classification

---
### Step 2: Install Dependencies

pip install -r requirements.txt

If requirements.txt doesn't exist, use:

pip install flask tensorflow opencv-python numpy


### Step 3: Train or Use Pretrained Model
You can either:

Run wasteclassification.ipynb to train and export model.pkl, or

Use the included model.pkl

### Step 4: Run the Web App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser.

📸 Example
Upload an image like this:


Result: "This image shows organic waste 🌱"

👤 Author
DAYA M P

GitHub Profile

📄 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

Would you like me to:
- Save this as a downloadable `README.md` file?
- Generate the missing `index.html` template?
- Create `requirements.txt` for easy setup?

Let me know how you'd like to proceed!

```bash

