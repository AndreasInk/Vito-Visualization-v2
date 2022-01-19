import pandas as pd
import streamlit as st

st.image("./Vito.png")
st.header("Vito")
st.subheader("Detecting Infectious Diseases With Wearables")
st.caption("Vito is an app that centralizes various studies to slow the spread of Covid-19 by utilizing biometrics from smartwatches.")

st.write("")
st.subheader("Data Visualization")

df = pd.DataFrame()
option = st.radio("Select Datapoint", ['Heart Rate', 'Respiratory Rate', 'Heart Rate Variability'], 1)

if option == 'Heart Rate':
    st.subheader("Heart Rate")
    st.caption("Measured in Beats Per Minute (BPM), this measurement can indicate stress when measured while asleep, thus, increasing prior to symptom onset of Covid-19.")
    st.table()
    
if option == 'Respiratory Rate':
    st.subheader("Respiratory Rate")
    st.caption("Measured in Breaths Per Minute (BPM), this measurement tends to increase prior and upon symptom onset.")
    st.table()

if option == 'Heart Rate Variability':
    st.subheader("Heart Rate Variability")
    st.caption("A measure of the variation in the interval between heart beats, this measurement tends to decrease prior and upon symptom onset.")
    st.table()
    



