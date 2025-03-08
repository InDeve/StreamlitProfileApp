''' Adapted from Nicholas Renotte: https://github.com/nicknochnack/CommentToxicity/blob/main/Toxicity.ipynb '''

import streamlit as st

st.title("Check if a comment's toxic")
loading_msg = st.empty()
loading_msg.info("Loading Model...")

from tensorflow.keras.models import load_model
from tensorflow.keras.layers import TextVectorization
import pandas as pd

import os

MAX_FEATURES = 200000  # Number of words in our vocab

@st.cache_resource
def loadModel():
    """Load the reassembled model into memory."""
    return load_model("ml_models/toxicity.keras")

@st.cache_resource
def load_resources():
    df = pd.read_csv("ml_models/train.csv")

    vectorizer = TextVectorization(max_tokens=MAX_FEATURES, output_sequence_length=1800, output_mode='int')
    vectorizer.adapt(df['comment_text'].values)  # Adapt vectorizer
    
    return vectorizer

# Load everything once
vectorizer = load_resources()

@st.cache_data
def score_comment(comment):
    """Vectorizes and predicts toxicity of the comment."""
    LABELS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult']
    
    vectorized_comment = vectorizer([comment])  # Vectorize comment
    results = model.predict(vectorized_comment)[0]  # Extract first row

    toxic_labels = [LABELS[i].replace("_", " ").capitalize() for i, val in enumerate(results) if val > 0.5]

    if not toxic_labels:
        return "**✅ No toxicity detected in this comment!**"

    return "**⚠️ Toxicity Detected:**\n\n" + "\n".join([f"- **{label}**" for label in toxic_labels])

model = loadModel()

loading_msg.empty()

comment = st.text_input("Write a comment:")

if comment:
    st.markdown(score_comment(comment))
