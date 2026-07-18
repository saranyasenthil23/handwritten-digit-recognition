import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from streamlit_drawable_canvas import st_canvas
import keras

# --- PATCH START ---
original_init = keras.layers.Dense.__init__
def patched_init(self, *args, **kwargs):
    kwargs.pop('quantization_config', None)
    original_init(self, *args, **kwargs)
keras.layers.Dense.__init__ = patched_init
# --- PATCH END ---

# Your existing model loading code comes here:
model = keras.models.load_model("digit_model.keras") 


# Load model
model = tf.keras.models.load_model("digit_model.keras")

st.title("✍️ Handwritten Digit Recognizer")

st.write("Draw a digit below and click Predict")

# Create canvas
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Predict"):
    if canvas_result.image_data is not None:
        img = canvas_result.image_data

        # Convert to grayscale
        img = Image.fromarray((img[:, :, 0]).astype('uint8'))

        # Resize to 28x28
        img = img.resize((28, 28))

        # Convert to array
        img = np.array(img)

        # Normalize
        img = img / 255.0

        # Reshape
        img = img.reshape(1, 28, 28, 1)

        # Predict
        prediction = model.predict(img)
        digit = np.argmax(prediction)
        confidence = np.max(prediction)

        st.success(f"✅ Predicted Digit: {digit}")
        st.write(f"Confidence: {confidence*100:.2f}%")