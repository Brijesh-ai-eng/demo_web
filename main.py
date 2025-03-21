import streamlit as st 
import pickle

st.subheader("Whether Prediction")
pn=st.number_input("Enter precipitation")
maxt=st.number_input("Enter maxt")
mint=st.number_input("Enter mint")
wind=st.number_input("Enter wind speed")
button=st.button("Done")

if button:
    model=pickle.load(open("wp.pkl","rb"))
    res=model.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"""
    Whether Condition: {res}
    """)
