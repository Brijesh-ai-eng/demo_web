import streamlit as st 


name=st.text_input("Enter Your Name : ")
fname=st.text_input("Enter Your Father's Name : ")
address=st.text_area("Enter Your Address : ")
classdata=st.selectbox("Enter Your Class : ",(1,2,3,4,5))
button=st.button("Done")

if button:
    st.markdown(f"""
                Name : {name}
                Father's Name : {fname}
                Address : {address}
                Class : {classdata}
                """)