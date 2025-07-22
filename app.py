import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
import PyPDF2

nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load("model/fake_news_model.pkl")
vectorizer = joblib.load("model/tfidf_vectorizer.pkl")

# Text cleaning
def clean_text(text):
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

# Predict function
def predict_news(news_text):
    cleaned = clean_text(news_text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)
    return "🟢 Real News" if prediction[0] == 1 else "🔴 Fake News"

# Streamlit UI
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detection App")

# Option 1: Text input
st.markdown("### Enter News Article Text:")
user_input = st.text_area("Type or paste the news article here")

if st.button("Predict Text Input"):
    if user_input.strip():
        result = predict_news(user_input)
        st.subheader(result)
    else:
        st.warning("Please enter some text first.")

# Option 2: File upload
st.markdown("### Or upload a file (.txt or .pdf):")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

if uploaded_file is not None:
    file_text = ""
    if uploaded_file.type == "text/plain":
        file_text = uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        for page in reader.pages:
            file_text += page.extract_text()

    if st.button("Predict Uploaded File"):
        if file_text.strip():
            result = predict_news(file_text)
            st.subheader(result)
        else:
            st.warning("Couldn't extract any text from the uploaded file.")
