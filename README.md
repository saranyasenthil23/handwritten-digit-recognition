 # ✍️ Handwritten Digit Recognition Web App

🚀 An end-to-end Deep Learning project that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) and provides an interactive drawing interface via a Streamlit web application.

---

## 🌟 Project Overview

This project demonstrates a complete machine learning pipeline:
- Model building using deep learning  
- Training on MNIST dataset  
- Model saving & loading  
- Interactive web UI using Streamlit  
- Real-time predictions  

Users can draw a digit and get instant predictions.

---

## 🖼️ Screenshots

### 🎨 Drawing Interface
![Drawing UI](images/ui.png)

### 🔢 Prediction Output
![Prediction](images/output.png)

👉 Store your screenshots inside a folder named `images/` in your project.

---

## 🎯 Problem Statement

Handwritten digit recognition is widely used in:
- Bank cheque processing  
- Postal systems  
- Form digitization  
- OCR applications  

This project solves it using CNN.

---

## 🧠 Model Architecture

- Convolutional Neural Network (CNN)  
- Conv2D + MaxPooling layers  
- Dense layers  
- Softmax output (0–9 classes)

---

## 📊 Dataset

- MNIST dataset  
- 60,000 training images  
- 10,000 testing images  
- 28x28 grayscale images  

---

## ⚙️ Tech Stack

- Python  
- TensorFlow / Keras  
- Streamlit  
- NumPy  
- Pillow  

---

## 🖥️ Features

- Draw digits using mouse  
- Instant prediction  
- Clean UI  
- Lightweight and fast  

--
## 🔄 Workflow

1. Load dataset  
2. Preprocess data  
3. Train CNN model  
4. Evaluate model  
5. Save model  
6. Build Streamlit UI  
7. Integrate model  
8. Predict in real-time  

--
🚧 Challenges & Solutions
TensorFlow version mismatch → Fixed by version alignment
Model loading error → Resolved using proper save format
Deployment issues → Fixed with clean dependencies

💡 Key Learnings
End-to-end ML pipeline
Debugging real-world issues
Building deployable apps
Dependency management

🔮 Future Improvements
Multi-digit recognition
Better UI/UX
Cloud deployment
