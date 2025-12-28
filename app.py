import streamlit as st
import pickle

# Load trained pipeline
model = pickle.load(open("text_classifier.pkl", "rb"))

st.set_page_config(page_title="Text Classification App", layout="centered")

st.title("📰Text Classifier")
st.write("Classifies text into **World, Sports, Business, or Sci/Tech**")

# Text input
text = st.text_area("Enter news text:")

if st.button("Predict"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([text])[0]
        st.success(f"📌 Predicted Category: **{prediction}**")
