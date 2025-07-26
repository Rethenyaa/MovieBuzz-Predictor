import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Load model and label encoder
model = pickle.load(open('cine_model.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

st.title("🎬 CineScope – Movie Success Predictor")
st.write("Enter movie features below to predict if it’s a **Flop**, **Average**, or **Hit**!")

budget = st.number_input("💰 Budget (in USD)", min_value=1000, step=1000)

genres = ['Action', 'Comedy', 'Drama', 'Romance', 'Science Fiction', 'Thriller']
selected_genres = st.multiselect("🎭 Select genres", genres)

if st.button("Predict"):
    if not selected_genres:
        st.warning("Please select at least one genre.")
    else:
        # One-hot encode the selected genres
        genre_vector = [1 if genre in selected_genres else 0 for genre in genres]

        # Final input for prediction
        input_data = [budget] + genre_vector
        input_array = np.array(input_data).reshape(1, -1)

        try:
            prediction = model.predict(input_array)
            label = le.inverse_transform(prediction)[0]
            st.success(f"🎉 The model predicts this movie will be a **{label}**!")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
