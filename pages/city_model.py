import streamlit as st

st.title("City Classification")
st.text("A Machine learning model trained on images of cities and towns.\n"
        "Upload an image of either one, and this app will try to identify it.")
st.image("assets/buildings-647400_640.jpg")

# ''' lOADING MESSAGE '''
loading_msg = st.empty()
loading_msg.info("Loading Model...")

import tensorflow as tf
from keras.models import load_model

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import cv2 # Used for computer vision

# ''' MODEL LOADING '''
@st.cache_resource
def loadModel():
   model = load_model("ml_models/CityTownClassifier.keras", compile=False)
   return model


# ''' CORE FUNCTION '''
@st.cache_data
def Classify(image):
  '''
  Putting the image read, resize, and predicition into this function
  '''
  model = loadModel()
  # Read an image the model hasn't seen before
  img_bytes = image.read()                                  # get the bytes of the uploaded data
  img_np_array = np.frombuffer(img_bytes, np.uint8)         # turn bytes into an array
  img_cv2 = cv2.imdecode(img_np_array, cv2.IMREAD_COLOR)    # read the array of bytes

  # Get the image into the right dimensions
  resize = tf.image.resize(img_cv2, (256,256))

  # Predict the classification
  yhat = model.predict(np.expand_dims(resize/255, 0))

  yhat_val = yhat[0][0]

  if round(yhat_val, 2) > 0.6:
    st.info("The machine's prediction is... a Town!")
    plt.title(f'Town')
  else:
    st.info("The machine's prediction is... a City!")
    plt.title(f'City')
  plt.grid(False)
  plt.axis(False)
  plt.imshow(cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB))
  st.pyplot(plt)

# ''' USER INTERFACE '''
loading_msg.empty()

upload_image = st.file_uploader("Upload an image: ", type=['jpeg','jpg','bmp', 'png'])
if upload_image is not None:
    
    #st.write(image)
    Classify(upload_image)