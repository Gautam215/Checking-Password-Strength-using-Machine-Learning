"""Streamlit app for checking password strength with a character-level model."""

from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


DATA_PATH = Path(__file__).resolve().parent / "Password Strength.csv"


@st.cache_data
def load_data(data_path: str, data_mtime_ns: int, data_size: int) -> pd.DataFrame:
    return pd.read_csv(data_path, on_bad_lines="skip")


@st.cache_resource
def get_model(data_path: str, data_mtime_ns: int, data_size: int):
    data = load_data(data_path, data_mtime_ns, data_size).dropna(
        subset=["password", "strength"]
    )
    data = data[data["strength"].isin([0, 1, 2])]

    vectorizer = TfidfVectorizer(analyzer="char")
    features = vectorizer.fit_transform(data["password"].astype(str))
    model = LogisticRegression(solver="newton-cholesky")
    model.fit(features, data["strength"].astype(int))
    return vectorizer, model


st.title("Password Strength Checker")

if not DATA_PATH.is_file():
    st.error(f"Dataset not found: {DATA_PATH.name}")
    st.stop()

data_stat = DATA_PATH.stat()
vectorizer, model = get_model(
    str(DATA_PATH), data_stat.st_mtime_ns, data_stat.st_size
)

user_inp = st.text_input("Enter password here", type="password")

if st.button("Check Strength"):
    if user_inp:
        prediction = int(model.predict(vectorizer.transform([user_inp]))[0])
        if prediction == 0:
            st.error("Weak Password")
        elif prediction == 1:
            st.warning("Medium Password")
        else:
            st.success("Strong Password")
    else:
        st.info("Please enter a password.")
