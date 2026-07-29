
import streamlit as st
import pandas as pd
import joblib
import yaml

st.set_page_config(page_title="Surge | Regression", layout="wide")
st.title("📈 Surge: Regression App")

try:
    with open("configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    model = joblib.load(config['data']['model_path'])
except:
    st.error("Please run `python src/train.py` first.")
    st.stop()

col1, col2 = st.columns(2)
with col1:
    st.header("Inputs")
    f1 = st.slider("Feature 1", 0.0, 200.0, 100.0)
    f2 = st.slider("Feature 2", 0.0, 100.0, 30.0)
    if st.button("Predict"):
        input_df = pd.DataFrame([{'f1': f1, 'f2': f2}])
        pred = model.predict(input_df)[0]
        st.session_state['pred'] = pred

with col2:
    if 'pred' in st.session_state:
        st.header("Prediction Result")
        st.info(f"**Target Value:** {st.session_state['pred']:.2f}")
