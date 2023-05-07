import streamlit as st
import joblib

model = joblib.load("drug.pkl")

st.title("Drug Classification")

age = st.select_slider("Enter your Age : ",[i for i in range(18,100)])

sex = st.selectbox("Your Pronouns are : ",['he/him', 'she/her'])
if sex == "he/him":
    sex = 1
else:
    sex = 0

bp = st.selectbox("Enter your BP Levels : ", ['Low(<100)', 'Normal(100-200)', 'High(>200)'])
if bp == 'Low(<100)':
    bp = 0
elif bp == 'Normal(100-200)':
    bp = 1
else:
    bp = 3

chol = st.selectbox("Enter Your Cholestrol Levels : ", ['Normal', 'High'])
if chol == 'Normal':
    chol = 0
else:
    chol = 1

nak = st.select_slider("Enter your Sodium to Potassium Ratio : ", [i for i in range(6, 39)])

params = [[age, sex, bp, chol, nak]]

pred = model.predict(params)

predict = st.button("Predict")

if predict:
    if pred[0] == 0:
        st.markdown(f"Predicted Drug : DrugX")
    elif pred[0] == 1:
        st.markdown(f"Predicted Drug : DrugY")
    elif pred[0] == 2:
        st.markdown(f"Predicted Drug : DrugA")
    elif pred[0] == 3:
        st.markdown(f"Predicted Drug : DrugB")
    else:
        st.markdown(f"Predicted Drug : DrugC")
