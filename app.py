import streamlit as st
import joblib
import numpy as np

# Cargar modelo entrenado
model = joblib.load("best_model.txt")

# Configuración de la página
st.set_page_config(page_title="Predicción de CO en el aire", page_icon="🌱", layout="centered")

st.markdown("<h1 style='text-align: center; color: green;'>🌱 Predicción de CO en el aire 🌱 </h1><br>", unsafe_allow_html=True)


# Entradas de usuario
col1, col2, col3 = st.columns(3)

with col1:
    temp = st.number_input("🌡️ Temperatura (°C)", value=20.0)

with col2:
    hum = st.number_input("💧 Humedad (%)", value=50.0)

with col3:
    nox = st.number_input("🌫️ NOx (ppb)", value=100.0)

X_input = np.array([[temp, hum, nox]])

# Predicción
pred = model.predict(X_input)[0]

# Mostrar resultado según el nivel de CO
if pred < 2.0:
    st.markdown(f"<div style='background-color:#ccffcc; padding:20px; border-radius:10px;'>"
                f"<h2 style='color:green; text-align:center;'>✅ CO bajo: {pred:.2f} mg/m³ ✅</h2>"
                f"</div>", unsafe_allow_html=True)
elif pred < 4.0:
    st.markdown(f"<div style='background-color:#ffffcc; padding:20px; border-radius:10px;'>"
                f"<h2 style='color:orange; text-align:center;'>⚠️ CO moderado: {pred:.2f} mg/m³ ⚠️</h2>"
                f"</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='background-color:#ffcccc; padding:20px; border-radius:10px;'>"
                f"<h2 style='color:red; text-align:center;'>🚨 CO alto: {pred:.2f} mg/m³ 🚨</h2>"
                f"</div>", unsafe_allow_html=True)
