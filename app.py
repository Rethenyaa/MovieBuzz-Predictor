import streamlit as st
import pickle
import numpy as np

# Load model and label encoder
model = pickle.load(open('cine_model.pkl', 'rb'))
label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))

st.title("🎬 CineScope – Movie Success Predictor")

st.markdown("Enter movie features below to predict if it’s a **Flop**, **Average**, or **Hit**!")

# Input features
budget = st.number_input("💰 Budget (in USD)", min_value=100000, step=100000)
genre_action = st.checkbox("Action")
genre_comedy = st.checkbox("Comedy")
genre_drama = st.checkbox("Drama")
genre_romance = st.checkbox("Romance")
genre_scifi = st.checkbox("Science Fiction")
genre_thriller = st.checkbox("Thriller")

# Feature vector (must match training order)
log_budget = np.log1p(budget)
features = [budget, log_budget, 
            int(genre_action), int(genre_comedy), int(genre_drama),
            int(genre_thriller), int(genre_romance), int(genre_scifi)]

# Predict button
if st.button("Predict"):
    result = model.predict([features])[0]
    label = label_encoder.inverse_transform([result])[0]
    
    if label == 'Hit':
        st.success(f"🎉 Predicted: {label} – Likely to be a blockbuster!")
    elif label == 'Average':
        st.info(f"📊 Predicted: {label} – Might break even.")
    else:
        st.error(f"💣 Predicted: {label} – Likely to be a flop.")
