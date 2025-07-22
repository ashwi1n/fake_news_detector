# 📰 Fake News Detection App (NLP Project)

This Streamlit app uses Natural Language Processing (NLP) to detect whether a news article is fake or real.

## 🔍 Features

- Enter news manually or upload `.txt`/`.pdf` files.
- Predicts if the content is 🟢 Real News or 🔴 Fake News.
- Built using Logistic Regression, TF-IDF, and NLTK.

## 📁 Project Structure

- `app.py` – Main Streamlit app.
- `model/` – Pretrained model & vectorizer.
- `data/` – Dataset used to train.
- `requirements.txt` – Dependencies.

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
